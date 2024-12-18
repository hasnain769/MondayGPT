# app/routers/auth.py
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
import os
import urllib.parse
import json
import httpx
from google.cloud import firestore
from dotenv import load_dotenv  # Import to load .env file
from fastapi.responses import JSONResponse

router = APIRouter()

# Load environment variables from .env file
load_dotenv()

# Initialize Firestore client
db = firestore.AsyncClient()

@router.get("/auth/login",responses={
        302: {
            "description": "Redirects to the Monday.com OAuth2 authorization page.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "detail": {
                                "type": "string",
                                "example": "Redirecting to the authorization page."
                            }
                        }
                    }
                }
            }
        },
        400: {
            "description": "Bad Request due to missing headers.",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "detail": {
                                "type": "string",
                                "example": "Missing openai-conversation-id in headers."
                            }
                        }
                    }
                }
            }
        }
    }
)
async def login(request: Request):
    # Extract the openai_conversation_id from the request headers
    openai_conversation_id = request.headers.get("openai-conversation-id")
    print("----Openai converstation id: ",openai_conversation_id)
    if not openai_conversation_id:
        raise HTTPException(status_code=400, detail="Missing openai-conversation-id in headers.")

    client_id = os.getenv("CLIENT_ID")
    redirect_uri = os.getenv("REDIRECT_URI")
    auth_url = "https://auth.monday.com/oauth2/authorize"

    # Include openai_conversation_id in state to retain it across requests
    state = json.dumps({"openai_conversation_id": openai_conversation_id})

    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "state": state,
    }

    url = f"{auth_url}?{urllib.parse.urlencode(params)}"
    print("Url: ", url)
    
    # Return the URL in a JSON response
    return JSONResponse(content={"url": url})

@router.get("/auth/callback")
async def callback(request: Request, code: str, state: str):
    print("----state----: ",state)
    try:
        # Extract openai_conversation_id from state
        state_data = json.loads(state)
        openai_conversation_id = state_data["openai_conversation_id"]
    except (json.JSONDecodeError, KeyError):
        raise HTTPException(status_code=400, detail="Invalid state parameter")

    # Token exchange
    token_url = "https://auth.monday.com/oauth2/token"
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    redirect_uri = os.getenv("REDIRECT_URI")

    data = {
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, data=data)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Token exchange failed")
        token_data = response.json()
        
        print("Acces token",token_data["access_token"])
    # Store the token in Firestore using openai_conversation_id as the document ID
    await save_token_to_firestore(
        openai_conversation_id=openai_conversation_id,
        access_token=token_data["access_token"],
        refresh_token=token_data.get("refresh_token"),
        expires_in=token_data.get("expires_in"),
        token_type=token_data.get("token_type"),
        scope=token_data.get("scope"),
    )

    return 

# Helper function to save the token in Firestore
async def save_token_to_firestore(openai_conversation_id: str, access_token: str, refresh_token: str, expires_in: int, token_type: str, scope: str):
    token_data = {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "expires_in": expires_in,
        "token_type": token_type,
        "scope": scope,
        "created_at": firestore.SERVER_TIMESTAMP  # Automatically sets the server timestamp
    }
    
    # Save to Firestore under the `tokens` collection, using openai_conversation_id as the document ID
    try:
        doc_ref = db.collection("tokens").document(openai_conversation_id)
        await doc_ref.set(token_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save token: {e}")
