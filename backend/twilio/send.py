#!/usr/bin/env python3
import sys
import os
from dotenv import load_dotenv, find_dotenv
from twilio.rest import Client

# Loads .env variables 
load_dotenv(find_dotenv())


# Send: Wrapper to send sms message to desired number
def Send(receiver: str, content: str) -> None:
    load_dotenv(find_dotenv())
    client = Client(os.environ.get("SID"), os.environ.get("TOKEN"))
    client.messages.create(body=content, from_=os.environ.get("Sender"), to=receiver)


if __name__ == "__main__":
    client = Client(os.environ.get("SID"), os.environ.get("TOKEN"))
    try:
        receiver = sys.argv[1]
        content = sys.argv[2]
        client.messages.create(body=content, from_=os.environ.get("Sender"), to=receiver)
    except:
        print("err: some value is missing")
