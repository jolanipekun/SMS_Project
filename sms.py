# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC9dd1e950a2376ac6aaa0513062de3dca'
auth_token = '9f554d592486f6e642701c5cb3684c4d'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+447401093404',
                              body='Hi there; I can not believe this works',
                              to='+44 7305 648467'
                          )


print(message.sid)
