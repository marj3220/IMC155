import access_tokens
from twilio.rest import Client

class AlertSender():
    def __init__(self) -> None:
        account_sid = access_tokens.account_sid
        auth_token = access_tokens.auth_token
        self.client = Client(account_sid, auth_token)
    
    def sendAlert(self, message: str):
        message = self.client.messages.create(
                            body =  "Indice de gel dans la zone 3", #Message you send
                            from_ = access_tokens.api_phone_number,
                            to =    access_tokens.your_phone_number)#Your phone number
        message.sid