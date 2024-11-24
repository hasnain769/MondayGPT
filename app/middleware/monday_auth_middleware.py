# app/middleware/auth_middleware.py

from fastapi import Request, Response
from fastapi.responses import JSONResponse
import asyncio

class AuthMiddleware:
    def __init__(self, app):
        self.app = app
        # self.db = firestore.AsyncClient()  # Commenting out Firestore client initialization

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            request = Request(scope, receive)

            # Read the request body
            body = await request.body()
            body_str = body.decode('utf-8')  # Decode the body to string for logging

            # Logging the full request
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

            print("\nBody:")
            print(body_str)  # Log the request body
            print("--- End of Request ---\n")

            # Pass the request to the app without performing token checks
            await self.app(scope, receive, send)

            # All below lines are commented out
            """
            # Extract conversation_id
            conversation_id = request.query_params.get("conversation_id") or request.headers.get("openai-conversation-id")
            print(f"\nExtracted conversation_id: {conversation_id}")

            # Bypass checks for documentation endpoints
            if request.url.path in ["/monday/docs", "/monday/openapi.json", "/monday/redoc"]:
                await self.app(scope, receive, send)
                return

            if conversation_id:
                try:
                    # Check if access token exists in Firestore
                    token_doc = await self.db.collection("tokens").document(conversation_id).get()
                    print(f"Fetched token document for conversation_id {conversation_id}: {token_doc}")

                    if token_doc.exists:
                        # Get the token value from Firestore
                        token_data = token_doc.to_dict()
                        print(f"Token data retrieved: {token_data}")

                        # Extract the access token
                        token = token_data.get("access_token")
                        
                        if token:
                            # Set the Authorization header
                            scope["headers"] = [
                                (b"authorization", f"Bearer {token}".encode())
                            ] + scope["headers"]
                            print(f"Authorization token set for conversation_id {conversation_id}")

                            # Rebuild the request with the original body for downstream processing
                            new_scope = {
                                **scope,
                                'type': 'http',
                                'method': request.method,
                                'path': request.url.path,
                                'headers': scope['headers'],
                                'body': body,
                            }

                            # Ensure that the path starts with '/monday'
                            if not new_scope['path'].startswith("/monday"):
                                new_scope['path'] = f"/monday{new_scope['path']}"

                            # Forward the request
                            print(f"Forwarding request to: {new_scope['path']}")

                            await self.app(new_scope, receive, send)
                            return
                        else:
                            print(f"No valid token found in data for conversation_id: {conversation_id}")
                    else:
                        print(f"Token document does not exist for conversation_id: {conversation_id}")
                except Exception as e:
                    print(f"Error accessing Firestore: {e}")

            # Return 401 Unauthorized if no valid token is found or token is None
            response = JSONResponse(
                status_code=401,
                content={"detail": "Unauthorized. No valid token found."}
            )
            await response(scope, receive, send)
            """
        else:
            # Handle non-HTTP requests
            await self.app(scope, receive, send)
