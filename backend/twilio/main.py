#!/usr/bin/env python3
from backend.twilio.creds import T_SID, T_TOKEN, SenderNumber
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# send_sms: send sms messages
def send_sms(body: str, sender: str, receiver: str):
    # default send via sms
    client = Client(T_SID, T_TOKEN)
    client.messages.create(body=body,from_=sender,to=receiver)

# TODO: fill out webhook / endpoint for both twilio and sanic thing

# docs: https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply-python
# receive_sms: how to receive and handle sms messages
def receive_sms():
    # agent that takes in sms messages
    resp = MessagingResponse()
    # response to incoming sms messages
    resp.message("asdf")
    # return a string of the response
    return str(resp)

if __name__ == "__main__":
    send_sms('', "Test msg", SenderNumber, "8453213926")
