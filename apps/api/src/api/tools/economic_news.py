import json
from pydantic import BaseModel,Field
from openai.types.chat import ChatCompletionToolParam

from apps.api.src.api.schemas.market_schemas import EconomicNews
from apps.api.src.api.core.enum import NewsRisk

class EconomicNewsArgs(BaseModel):
    symbol :str = Field(
            description="trading symbol such as : EURUSD EMIN100 SQ BTCUSDT ...... "
        )
    
async def get_economic_news(args : EconomicNewsArgs) -> EconomicNews:
    return EconomicNews(
        news_name="CPI",
        risk=NewsRisk.VeryRisky,
        confidence=90,
    )
    
ECONOMIC_NEWS_TOOL: ChatCompletionToolParam = {
    "type": "function",
    "function": {
        "name": "get_economic_news",
        "description": "get the most affected news of the traded symbol and give the risk and the confedance",
        "parameters": EconomicNewsArgs.model_json_schema(),
    },
}