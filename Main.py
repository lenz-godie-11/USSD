from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
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
@app.post("/ussd", response_class=PlainTextResponse)
async def ussd(request: USSDRequest):

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:

            response = await client.post(
                BACKEND_URL,
                json=request.model_dump()
            )

        response.raise_for_status()

        return response.text

    except httpx.RequestError:
        return "END Service temporarily unavailable. Please try again later."

    except httpx.HTTPStatusError:
        return "END Service temporarily unavailable. Please try again later."