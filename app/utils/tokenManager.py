# # app/utils/token_manager.py
# import httpx
# # from app.models import OAuthToken
# # from sqlmodel.ext.asyncio.session import AsyncSession
# from app.utils.encryption import encrypt_token, decrypt_token
# import os

# async def get_valid_token(user_id: str, session: AsyncSession) -> str:
#     token = await session.get(OAuthToken, user_id)
#     if token and not token.is_expired:
#         return decrypt_token(token.access_token)
#     elif token and token.refresh_token:
#         # Refresh the token
#         new_token_data = await refresh_access_token(token.refresh_token)
#         if new_token_data:
#             token.access_token = encrypt_token(new_token_data["access_token"])
#             token.expires_in = new_token_data.get("expires_in")
#             token.refresh_token = new_token_data.get("refresh_token")
#             token.created_at = datetime.utcnow()
#             await session.commit()
#             return decrypt_token(token.access_token)
#     # Token does not exist or cannot be refreshed
#     return None

# async def refresh_access_token(refresh_token: str) -> dict:
#     token_url = "https://auth.monday.com/oauth2/token"
#     client_id = os.getenv("CLIENT_ID")
#     client_secret = os.getenv("CLIENT_SECRET")

#     data = {
#         "grant_type": "refresh_token",
#         "refresh_token": refresh_token,
#         "client_id": client_id,
#         "client_secret": client_secret,
#     }

#     async with httpx.AsyncClient() as client:
#         response = await client.post(token_url, data=data)
#         if response.status_code == 200:
#             return response.json()
#     return None
