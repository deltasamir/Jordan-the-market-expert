from fastapi import APIRouter

from apps.api.src.api.schemas.chat import ChatResponse,ChatRequest
from apps.api.src.api.services.llm import


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("",response_model=ChatResponse,)

async def Chat(request=ChatRequest):
    
    answer = await