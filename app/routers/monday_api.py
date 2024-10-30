# app/routers/monday_api.py
from fastapi import APIRouter, FastAPI, Depends, HTTPException, Header, Request
from app.middleware.auth_middleware import AuthMiddleware
import httpx

# Create a sub-application specifically for the monday routes
monday_app = FastAPI(
    title="MondayGPT app backend",
    version="0.0.2",
    servers=[{
        "url": "/monday",
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

@monday_app.get("/boards", tags=["monday"], responses={
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
                                            "id": {
                                                "type": "string",
                                                "description": "Board ID"
                                            },
                                            "name": {
                                                "type": "string",
                                                "description": "Board name"
                                            },
                                            "description": {
                                                "type": ["string", "null"],
                                                "description": "Board description"
                                            },
                                            "columns": {
                                                "type": "array",
                                                "items": {
                                                    "type": "object",
                                                    "properties": {
                                                        "id": {
                                                            "type": "string",
                                                            "description": "Column ID"
                                                        },
                                                        "title": {
                                                            "type": "string",
                                                            "description": "Column title"
                                                        },
                                                        "type": {
                                                            "type": "string",
                                                            "description": "Column type"
                                                        }
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
                        "account_id": {
                            "type": "integer",
                            "description": "Account ID"
                        }
                    },
                    "required": ["data", "account_id"]
                }
            }
        }
    },
    401: {
        "description": "Unauthorized access due to invalid or missing token. login please.",
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "detail": {
                            "type": "string",
                            "example": "Call to /auth/login"
                        }
                    }
                }
            }
        }
    },
    422: {
        "description": "Validation Error",
        "content": {
            "application/json": {
                "schema": {
                    
                }
            }
        }
    }
})
async def get_board_details(request: Request):
    """
    Retrieve board details from Monday.com using the Authorization token set by middleware.
    """
    # Access the Authorization header set by the middleware
    authorization = request.headers.get("Authorization")

    # Since the middleware handles authentication and redirects unauthorized requests,
    # we can safely assume that 'authorization' is present and properly formatted.
    headers = {
        "Authorization": authorization,
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                MONDAY_GRAPHQL_API_URL,
                headers=headers,
                json={"query": BOARD_DETAILS_QUERY},
            )
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        except httpx.HTTPStatusError as exc:
            # Log the error details if necessary
            raise HTTPException(
                status_code=exc.response.status_code,
                detail=f"Failed to fetch board details: {exc.response.text}"
            )
        except httpx.RequestError as exc:
            # Handle network-related errors
            raise HTTPException(
                status_code=503,
                detail=f"Network error occurred while fetching board details: {exc}"
            )

    # Return the JSON response from Monday.com
    return response.json()