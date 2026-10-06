from fastapi import FastAPI

from .routes.chat import router as chat_router

model_name = "Jordan The market expert"
app = FastAPI(
    title= model_name
)

app.include_router(chat_router)
