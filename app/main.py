# app/main.py
from fastapi import FastAPI
from app.routers.monday_app import monday_api
import uvicorn
import os

from app.routers.auth import auth

app = FastAPI(
    title="MondayGPT app backend",
    version="0.0.2",
    servers=[{
        "url": "",
        "description": "Backend server for Monday GPT to authorize users"
    }]
)

# Include other routers as usual
app.include_router(auth.router)

# Include the monday_app with middleware as a sub-application for /monday routes
app.mount("/monday", monday_api.monday_app)

# @app.get("/")
# async def hello():
#     return {"message": "hello"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
