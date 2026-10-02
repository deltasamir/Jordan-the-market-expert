import json
from pydantic import BaseModel,Field 
from openai.types.chat import ChatCompletionToolParam

from apps.api.src.api.schemas.market_schemas import Setup
from apps.api.src.api.schemas.market_schemas import MarketSetup
class SetupArgs(BaseModel):
    symbol : str = Field(
        description="trading symbol such as : EURUSD EMIN100 SQ BTCUSDT ...... "
    )
    
    trend : str 
    
async def get_setup(args : SetupArgs):
    return Setup(
        setup=MarketSetup.Long
    )
    
SETUP_TOOLS: ChatCompletionToolParam = {
    "type": "function",
    "function": {
        "name": "get_setup",
        "description": "Market setup: long or short, based on market data and trend.",
        "parameters": SetupArgs.model_json_schema(),
    },
}

    