from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class USSDRequest(BaseModel):
    sessionId: str
    phoneNumber: str
    serviceCode: str
    text: str


@app.post("/ussd")
async def ussd(request: USSDRequest):

    if request.text == "":
        return "CON Welcome to our service\n1. Check Balance\n2. Buy Airtime\n3. Exit"

    return "END Thank you for using our service"