import os
from twilio.rest import Client

class TwilioTextEngine:
    def __init__(self):
        self.client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))

    def sendMessageTo(self, message: str, to: int) -> None:
        """_summary_

        Args:
            message (str): _description_
            to (int): _description_
        """        
        try:
            self.client.messages.create(
            body= message,
            from_="+18888235621",
            to=f'+1{to}'
            )
        except Exception as e:
            print({e})