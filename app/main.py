# app/main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse  # Import JSONResponse
from starlette.middleware.sessions import SessionMiddleware
from app.routers import auth
from app.routers import monday_api
from app.middleware.auth_middleware import AuthMiddleware
import uvicorn
import os

app = FastAPI()

# Add AuthMiddleware
app.add_middleware(AuthMiddleware)

# Include your routers
app.include_router(auth.router)
app.include_router(monday_api.router)

# Add session middleware
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))

@app.get("/")
async def hello():
    return {"message": "hello"}

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred. Please try again later."},
    )

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
