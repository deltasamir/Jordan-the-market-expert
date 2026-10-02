import json
from pydantic import BaseModel,Field
from openai.types.chat import ChatCompletionToolParam


from apps.api.src.api.schemas.market_schemas import Price

#market tool argument

class MarketDataArgs(BaseModel):
    symbol :str = Field(
        description="trading symbol such as : EURUSD EMIN100 SQ BTCUSDT ...... "
    )
    
    time_frame:str = Field(
        description="trading time frame such as : 1D 4H 1H 15M 5M ....."
    )
    
async def get_market_data(args : MarketDataArgs) -> Price:
    return Price(
         current_price=1.1742,
        change=0.42,
        price_high=1.1765,
        price_low=1.1688,
    )
    
MARKET_DATA_TOOL: ChatCompletionToolParam = {
    "type": "function",
    "function": {
        "name": "get_market_data",
        "description": (
            "Get current price information for a trading instrument "
            "including current price, daily change, daily high and daily low."
        ),
        "parameters": MarketDataArgs.model_json_schema(),
    },
}