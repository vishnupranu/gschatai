
from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(title="MyGPT Enterprise")

app.include_router(chat_router)
