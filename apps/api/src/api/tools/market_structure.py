import json
from pydantic import BaseModel,Field

from apps.api.src.api.schemas.market_schemas import MarketStructure
from apps.api.src.api.core.enum import MarketTrend

class MarketStructureArgs(BaseModel):
    symbol :str = Field(
        description="the trading symbols that we want to see the mmarket structure like : GBPUSD BTCUSD NQ EMIN100 ...."
    )
    timeframe:str = Field(
        description="trading time frame such as : 1D 4H 1H 15M 5M ....."
    )

async def get_market_structure(args:MarketStructureArgs) -> MarketStructure:
    return MarketStructure(
        trend=MarketTrend.Bullish
    )
    
MARKET_STUCTURE_TOOL = {
    "type":"function",
    "name":"get_market_structure",
    "description":(
        "trading trend such bullish , bearish , ranging ",
        "trend en the specified time frame "
    ),
    "parameter":MarketStructureArgs.model_json_schema()
}