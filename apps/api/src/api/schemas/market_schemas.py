from pydantic import BaseModel,Field 
from api.core.enum import NewsRisk,MarketTrend,MarketSetup
class Price(BaseModel):
    current_price:float 
    change:float = Field(
        description="Percentage price change during the day. Can be positive or negative."
    )
    price_high:float=Field(description="the highest point price reach during the day ")
    price_low:float=Field(
        description="the lowest point price reach during the day "
    )
    
class MarketStructure(BaseModel):
    trend:MarketTrend=Field(
        description="Market trend eg : Bullish or bearish or ranging"
    )
    
class EconomicNews(BaseModel):
    news_name:str=Field(
        description="the name of the most affected news of the market that day eg : cpi ...."
    )
    risk:NewsRisk
    confidence:float=Field(
        ge=0,
        le=100,
        description="confidence in percentage eg 60% ....."
    )
    
class Setup(BaseModel):
    setup:MarketSetup=Field(
        description="The market setup that should be watched, "
                    "for example long, short, or no trade."
    )
    

