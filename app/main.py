# app/main.py
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from app.routers import auth
import uvicorn
import os
app = FastAPI()

app.include_router(auth.router)

app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))

app.get("/")
async def hello():
    return{"message":"hello"}

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    # Log the exception
    # Return a user-friendly error message
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred. Please try again later."},
    )

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
