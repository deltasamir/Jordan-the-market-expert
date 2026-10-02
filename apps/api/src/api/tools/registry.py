from api.tools.market_data import (
    MarketDataArgs,
    MARKET_DATA_TOOL,
    get_market_data
)

from api.tools.market_structure import(
    MarketStructureArgs,
    MARKET_STUCTURE_TOOL,
    get_market_structure
)

from api.tools.economic_news import (
    EconomicNewsArgs,
    ECONOMIC_NEWS_TOOL,
    get_economic_news
)

from api.tools.setup import (
    SetupArgs,
    SETUP_TOOLS,
    get_setup
)


TOOLS = [
    MARKET_DATA_TOOL,
    ECONOMIC_NEWS_TOOL,
    MARKET_STUCTURE_TOOL,
    SETUP_TOOLS
]

TOOLS_FUNCTIONS = {
    "get_market_data" : get_market_data,
    "get_economic_news" :get_economic_news,
    "get_market_structure" : get_market_structure,
    "get_setup" : get_setup
}

TOOL_SCHEMAS = {
    "get_market_data" : MarketDataArgs,
    "get_economic_news" : EconomicNewsArgs,
    "get_market_structure" : MarketStructureArgs,
    "get_setup" : SetupArgs
}

