import os
import json
from typing import Any

from services.config import client, conversation
from apps.api.src.api.schemas.market_schemas import Price
from tools.registry import TOOLS

# model name
model_name: str = "Jordan"

SYSTEM_PROMPT = """
You are a market analysis assistant.

Your job is to analyze financial markets using the available tools.

Rules:

- Never invent market prices.
- Never invent economic news.
- Use tools when real market information is required.
- Base factual market information on tool results.
- Clearly distinguish market data from interpretation.
- If the available data is insufficient, say so.
- Do not claim certainty about future market direction.
"""


async def run_llm(user_message: str):
     response = await client.chat.completions.create(
       model="openai/gpt-4o",
       messages=[
          {"role": "system", "content": SYSTEM_PROMPT},
          {"role": "user", "content": user_message},
       ],
     tools=TOOLS,
)
     
     
     