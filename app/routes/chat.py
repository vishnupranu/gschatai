
from fastapi import APIRouter
from app.llm import generate_reply

router = APIRouter()

@router.post("/chat")
async def chat(data: dict):
    user_input = data.get("message")
    reply = generate_reply(user_input)
    return {"reply": reply}
