from fastapi import APIRouter, Depends, HTTPException, Header
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.utils.token_manager import get_valid_token
import httpx
import os

router = APIRouter()

# GraphQL API endpoint for Monday.com
MONDAY_GRAPHQL_API_URL = "https://api.monday.com/v2"

# The GraphQL query
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
@router.get("/monday/boards", tags=["monday"])
async def get_board_details(
    authorization: str = Header(..., alias="Authorization", description="Bearer token for Monday.com API")
):
    # Check if the header is in the format 'Bearer <token>'
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid or missing access token. Expected format: 'Bearer <token>'")

    # Prepare headers with the valid token
    headers = {
        "Authorization": authorization,
        "Content-Type": "application/json",
    }

    # Make the request to Monday.com GraphQL API
    async with httpx.AsyncClient() as client:
        response = await client.post(
            MONDAY_GRAPHQL_API_URL,
            headers=headers,
            json={"query": BOARD_DETAILS_QUERY},
        )

    # Check if the request was successful
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch board details")

    # Return the response JSON
    return response.json()
# @router.get("/monday/boards", tags=["monday"])
# # async def get_board_details(session: AsyncSession = Depends(get_session)):------> change after db integrations
# async def get_board_details():

#     # # Retrieve the access token for the user (assuming user_id is available in session or context)
#     # access_token = await get_valid_token(user_id="unique_user_identifier", session=session)
#     access_token ='eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjQyOTE1MzU1MSwiYWFpIjozMzI0NDIsInVpZCI6Njc4NzM0MjgsImlhZCI6IjIwMjQtMTAtMjhUMTc6Mzg6MTkuNTM0WiIsInBlciI6Im1lOnJlYWQsYm9hcmRzOnJlYWQsYm9hcmRzOndyaXRlLHVzZXJzOndyaXRlIiwiYWN0aWQiOjI2MjA3NzI5LCJyZ24iOiJhcHNlMiJ9.CaeALfzZgTAf3Q0QNwkJLicU4O8bo74kdyv7ABoia7Y'
#     if not access_token:
#         raise HTTPException(status_code=401, detail="Invalid or expired access token")

#     # Make the request to Monday.com GraphQL API
#     headers = {
#         "Authorization": access_token,
#         "Content-Type": "application/json",
#     }
    
#     async with httpx.AsyncClient() as client:
#         response = await client.post(
#             MONDAY_GRAPHQL_API_URL,
#             headers=headers,
#             json={"query": BOARD_DETAILS_QUERY},
#         )

#     # Check if the request was successful
#     if response.status_code != 200:
#         raise HTTPException(status_code=response.status_code, detail="Failed to fetch board details")

#     # Return the response JSON
#     return response.json()