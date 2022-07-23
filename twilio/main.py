#!/usr/bin/env python3
from creds import T_SID, T_TOKEN, SenderNumber
from twilio.rest import Client

# send_sms: sms message
def send_sms(client, body: str, sender: str, receiver: str):
    client.messages.create(body=body,from_=sender,to=receiver)

def receive_sms():
    pass

if __name__ == "__main__":
    client = Client(T_SID, T_TOKEN)
    print(type(client))