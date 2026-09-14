from fastapi import FastAPI
from pydantic import BaseModel
import httpx


# Initialize FastAPI app
app = FastAPI()


# Define the USSD request model
class USSDRequest(BaseModel):
    sessionId: str
    phoneNumber: str
    serviceCode: str
    text: str


# Backend URL
BACKEND_URL = "http://127.0.0.1:9000/ussd"


# Define the USSD gateway endpoint
@app.post("/ussd")
async def ussd(request: USSDRequest):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            BACKEND_URL,
            json=request.model_dump()
        )

    return response.text