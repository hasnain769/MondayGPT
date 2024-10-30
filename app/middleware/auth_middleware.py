# app/middleware/auth_middleware.py

from fastapi import Request, Response
from fastapi.responses import JSONResponse  # Correct import for JSONResponse
from google.cloud import firestore

class AuthMiddleware:
    def __init__(self, app):
        self.app = app
        self.db = firestore.AsyncClient()

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            request = Request(scope, receive)

            # Logging (optional)
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

            # Extract conversation_id
            conversation_id = request.query_params.get("conversation_id") or request.headers.get("openai-conversation-id")
            print(f"\nExtracted conversation_id: {conversation_id}")
            print("--- End of Request ---\n")

            # Bypass checks for documentation endpoints
            if request.url.path in ["/monday/docs", "/monday/openapi.json", "/monday/redoc"]:
                await self.app(scope, receive, send)
                return

            if conversation_id:
                # Check if access token exists in Firestore
                token_doc = await self.db.collection("tokens").document(conversation_id).get()
                if token_doc.exists:
                    # Get the token value from Firestore
                    token = token_doc.to_dict().get("token")

                    if token:
                        # Set the Authorization header
                        scope["headers"] = [
                            (b"authorization", f"Bearer {token}".encode())
                        ] + scope["headers"]

                    # Forward the request
                    await self.app(scope, receive, send)
                    return

            # Return 401 Unauthorized if no valid token is found
            response = JSONResponse(
                status_code=401,
                content={"detail": "Unauthorized. Please authenticate first."}
            )
            await response(scope, receive, send)
        else:
            # Handle non-HTTP requests
            await self.app(scope, receive, send)
