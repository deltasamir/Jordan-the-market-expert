from fastapi import FastAPI

from apps.api.src.api.routes.chat import router as chat_router

model_name = "Jordan The market expert"
app = FastAPI(
    title= model_name
)

app.include_router(chat_router)
