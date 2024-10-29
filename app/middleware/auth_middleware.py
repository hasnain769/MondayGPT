# app/middleware/auth_middleware.py
from fastapi import Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from google.cloud import firestore

class AuthMiddleware:
    def __init__(self, app):
        self.app = app
        self.db = firestore.AsyncClient()

    async def __call__(self, scope, receive, send):
        # Check if the scope has the type 'http'
        if scope["type"] == "http":
            request = Request(scope, receive)

            # Nicely formatted logging for headers and query parameters
            print("\n--- Incoming Request ---")
            print(f"Method: {request.method} | Path: {request.url.path}")
            print(f"Client IP: {scope['client'][0]} | Port: {scope['client'][1]}")

            print("\nHeaders:")
            for key, value in request.headers.items():
                print(f"    {key}: {value}")

            print("\nQuery Parameters:")
            if request.query_params:
                for key, value in request.query_params.items():
                    print(f"    {key}: {value}")
            else:
                print("    None")

            # Extract conversation_id from query parameters or headers
            conversation_id = request.query_params.get("conversation_id") or request.headers.get("openai-conversation-id")
            print(f"\nExtracted conversation_id: {conversation_id}")
            print("--- End of Request ---\n")

            # Bypass checks for /auth/login and /auth/callback
            if request.url.path in ["/auth/login", "/auth/callback", "/docs"]:
                await self.app(scope, receive, send)
                return

            if conversation_id:
                # Check if access token exists in Firestore
                token_doc = await self.db.collection("tokens").document(conversation_id).get()
                if token_doc.exists:
                    # Forward the request to the appropriate route if token exists
                    await self.app(scope, receive, send)
                    return

            # Redirect to the auth/login path if no valid token is found
            response = RedirectResponse(url="/auth/login")
            await response(scope, receive, send)
        else:
            # Handle non-HTTP requests (if any)
            await self.app(scope, receive, send)