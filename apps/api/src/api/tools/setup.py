import json
from pydantic import BaseModel,Field 

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
    
SETUP_TOOLS = {
    "type":"function",
    "name":"get_setup",
    "description":"Market setup : long short , based on the market market data trend , market data",
    "parameter":SetupArgs.model_json_schema()
}

    