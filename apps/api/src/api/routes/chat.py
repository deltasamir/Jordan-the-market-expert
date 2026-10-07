from fastapi import APIRouter

from api.schemas.chat import ChatResponse,ChatRequest
from api.services.llm import run_llm


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("",response_model=ChatResponse,)

async def Chat(request=ChatRequest):
    
    answer = await run_llm(request)
    
    return ChatResponse(
        answer=answer
    )