import asyncio
from fastapi import FastAPI
from controllers.Tariffs_controllers import router as traffic_router
from controllers.Payment_controller import router as payment_router
from controllers.Bank_status_controller import router as bank_status_router
import uvicorn
import os
from dotenv import load_dotenv

app = FastAPI(title="Test Kvitto", swagger_ui_parameters={"syntaxHighlight": {"theme": "obsidian"}})

app.include_router(traffic_router)
app.include_router(payment_router)
app.include_router(bank_status_router)

load_dotenv()

if __name__ == "__main___":
    uvicorn.run("main:app", host="127.0.0.1", port=os.getenv("APP_PORT"), reload=True)