# app/routers/monday_api.py
from fastapi import APIRouter, FastAPI, Depends, HTTPException, Header, Request
from app.middleware.monday_auth_middleware import AuthMiddleware
import httpx
from fastapi import Body
from typing import List
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx

# Create a sub-application specifically for the monday routes
monday_app = FastAPI(
    title="MondayGPT app backend",
    version="0.0.2",
    servers=[{
        "url": "",
        "description": "Backend server to execute Actions for users on [monday.com](https://monday.com) i.e (CRUD)."
    }]
)
monday_app.add_middleware(AuthMiddleware)

router = APIRouter()

# GraphQL API endpoint for Monday.com
MONDAY_GRAPHQL_API_URL = "https://api.monday.com/v2"

BOARD_DETAILS_QUERY = """
query {
    boards {
        id
        name
        description
        columns {
            id
            title
            type
        }
    }
}
"""


security = HTTPBearer()

# Update OpenAPI to include Bearer Authentication in securitySchemes
@monday_app.get(
        
    "/boards", 
    tags=["monday"], 
    responses={
        200: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "boards": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {"type": "string", "description": "Board ID"},
                                                "name": {"type": "string", "description": "Board name"},
                                                "description": {"type": ["string", "null"], "description": "Board description"},
                                                "columns": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "object",
                                                        "properties": {
                                                            "id": {"type": "string", "description": "Column ID"},
                                                            "title": {"type": "string", "description": "Column title"},
                                                            "type": {"type": "string", "description": "Column type"}
                                                        },
                                                        "required": ["id", "title", "type"]
                                                    }
                                                }
                                            },
                                            "required": ["id", "name", "columns"]
                                        }
                                    }
                                },
                                "required": ["boards"]
                            },
                            "account_id": {"type": "integer", "description": "Account ID"}
                        },
                        "required": ["data", "account_id"]
                    }
                }
            }
        },
        401: {
            "description": "Unauthorized access due to invalid or missing token.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "detail": {"type": "string", "example": "Authorization required. Call to /auth/login."}
                        }
                    }
                }
            }
        },
        422: {"description": "Validation Error"}
    },
    # Apply security scheme in the OpenAPI documentation
    dependencies=[Depends(security)]
)
async def get_board_details(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Retrieve board details from Monday.com using the Authorization token.
    """
    # Extract and format the token as Bearer <access_token>
    token = credentials.credentials
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                MONDAY_GRAPHQL_API_URL,
                headers=headers,
                json={"query": BOARD_DETAILS_QUERY},
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(
                status_code=exc.response.status_code,
                detail=f"Failed to fetch board details: {exc.response.text}"
            )
        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=503,
                detail=f"Network error occurred while fetching board details: {exc}"
            )

    return response.json()


CREATE_MULTIPLE_ITEMS_MUTATION_TEMPLATE = """
mutation {{
    {mutations}
}}
"""

ITEM_CREATION_ALIAS_TEMPLATE = """
    item_{index}: create_item(board_id: {board_id}, item_name: "{item_name}") {{
        id
        name
    }}
"""


@monday_app.post(
    "/boards/{board_id}/items", 
    tags=["monday"], 
    responses={
        200: {
            "description": "Items created successfully",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "data": {
                                "type": "object",
                                "properties": {
                                    "created_items": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "id": {"type": "string"},
                                                "name": {"type": "string"}
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        401: {
            "description": "Unauthorized access due to invalid or missing token",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "detail": {"type": "string", "example": "Authorization required. Call to /auth/login."}
                        }
                    }
                }
            }
        },
        422: {
            "description": "Validation Error",
            "content": {
                "application/json": {
                    "schema": {}
                }
            }
        }
    },
    dependencies=[Depends(security)]
)
async def create_items(
    board_id: int,
    item_names: List[str] = Body(...),
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """
    Create multiple items on a specified board, using the provided Authorization token.
    """
    # Extract and format the token as Bearer <access_token>
    token = credentials.credentials
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    # Construct the GraphQL mutations for each item
    mutations = "\n".join([
        ITEM_CREATION_ALIAS_TEMPLATE.format(index=i, board_id=board_id, item_name=name)
        for i, name in enumerate(item_names)
    ])

    # Format the complete mutation query
    mutation_query = CREATE_MULTIPLE_ITEMS_MUTATION_TEMPLATE.format(mutations=mutations)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                MONDAY_GRAPHQL_API_URL,
                headers=headers,
                json={"query": mutation_query}
            )
            response.raise_for_status()

            # Process the response data to extract created items
            response_data = response.json().get("data", {})
            created_items = [
                {"id": item["id"], "name": item["name"]}
                for item in response_data.values() if item and "id" in item and "name" in item
            ]

            if not created_items:
                raise HTTPException(status_code=422, detail="No items were created.")

        except httpx.HTTPStatusError as exc:
            raise HTTPException(
                status_code=exc.response.status_code,
                detail=f"Failed to create items: {exc.response.text}"
            )
        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=503,
                detail=f"Network error occurred while creating items: {exc}"
            )

    return {"data": {"created_items": created_items}}