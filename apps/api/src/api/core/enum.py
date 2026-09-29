from enum import Enum

class NewsRisk(str,Enum):
    Low ="low"
    Medium = "medium"
    High = "high"
    VeryRisky = "very risky"
    
class MarketTrend(str,Enum):
    Bullish="bullish"
    Bearish="bearish"
    Ranging="ranging"

class MarketSetup(str,Enum):
    Long="long"
    Short="Short"