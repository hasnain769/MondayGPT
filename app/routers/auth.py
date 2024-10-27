# app/routers/auth.py
from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from sqlmodel.ext.asyncio.session import AsyncSession
# from app.database import get_session
import os
import urllib.parse

router = APIRouter()

@router.get("/auth/login")
async def login(request: Request):
    client_id = os.getenv("CLIENT_ID")
    redirect_uri = os.getenv("REDIRECT_URI")
    auth_url = "https://auth.monday.com/oauth2/authorize"

    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "state": "secure_random_state",
    }

    url = f"{auth_url}?{urllib.parse.urlencode(params)}"
    return RedirectResponse(url)

# app/routers/auth.py (continued)
import httpx
# from app.utils.encryption import encrypt_token
# from app.models import OAuthToken

@router.get("/auth/callback")
async def callback(request: Request, code: str, state: str ):
    print("callback") ##add this when add db : session: AsyncSession = Depends(get_session)
    if state != "secure_random_state":
        # Handle invalid state parameter
        return RedirectResponse("/error?message=Invalid state parameter")

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
        token_data = response.json()
    print("token",token_data)
    if response.status_code != 200:
        # Handle token exchange error
        return RedirectResponse("/error?message=Token exchange failed")

    # # Encrypt and store the token securely
    # encrypted_token = encrypt_token(token_data["access_token"])
    # token = OAuthToken(
    #     user_id="unique_user_identifier",
    #     access_token=encrypted_token,
    #     expires_in=token_data.get("expires_in"),
    #     token_type=token_data.get("token_type"),
    #     scope=token_data.get("scope"),
    #     refresh_token=token_data.get("refresh_token"),
    # )
    # session.add(token)
    # await session.commit()

    return RedirectResponse("/dashboard")
