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
        return "CON Welcome to My Service\n1. Account\n2. Payments\n3. Exit"

    if request.text == "1":
        return "CON Account Menu\n1. Balance\n2. Profile"

    if request.text == "2":
        return "CON Payment Menu\n1. Pay Bill\n2. Send Money"

    if request.text == "3":
        return "END Thank you for using My Service"

    return "END Invalid option"