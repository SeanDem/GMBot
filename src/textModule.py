import os
from twilio.rest import Client

class TextEngine:
    def __init__(self):
        self.client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))

    def sendMessageTo(self, message: str, to: int) -> None:
        self.client.messages.create(
        body= message,
        from_="+18888235621",
        to=f'+1{to}'
        )