from operator import itemgetter
import os
import json
from typing import Any , cast
from openai.types.chat import ChatCompletionMessageParam

from api.services.config import client, MODEL
from api.schemas.market_schemas import Price
from api.tools.registry import TOOLS, TOOLS_FUNCTIONS, TOOL_SCHEMAS

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
  
    messages: list[ChatCompletionMessageParam] = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT,
    },
    {
        "role": "user",
        "content": user_message,
    },
]
    response = await client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
    )
    assistant_message = response.choices[0].message

      # ------ NO TOOL CALL ------
    if not assistant_message.tool_calls:
        return assistant_message.content or ""

    # ------ ADD ASSISTANT TOOL CALL TO CONVERSATION ------
    messages.append(
        {
            "role": "assistant",
            "content": assistant_message.content,
            "tool_calls": [
                {
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments,
                    },
                }
                for tool_call in assistant_message.tool_calls
            ],
        }
    )

    for tool_call in assistant_message.tool_calls:
        tool_name = tool_call.function.name

        function = TOOLS_FUNCTIONS.get(tool_name)
        schema = TOOL_SCHEMAS.get(tool_name)

        if function is None or schema is None:
            tool_result = {"error": f"Unknown tool {tool_name}"}
        else:
            try:
                raw_arguments = json.loads(tool_call.function.arguments)
                validated_arguments = schema.model_validate(raw_arguments)

                result = await function(validated_arguments)
                tool_result = json.loads(result.model_dump_json())
            except Exception as exc:
                tool_result = {"error": str(exc)}

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(tool_result),
            }
        )

    final_response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        tools=TOOLS,
        tool_choice="auto",
    )

    return final_response.choices[0].message.content or ""