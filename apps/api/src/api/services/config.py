import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("YOUR_OPEN_ROUTER_API_KEY")
)

conversation = "You are a profitional trader market analyzer "

MODEL = "openai/gpt-4o"
