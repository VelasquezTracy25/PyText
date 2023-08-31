from twilio.rest import Client
import config

client = Client(account_sid, auth_token)
client1 = Client(account_sid, auth_token)


call = client1.messages.create(
    to="12104730194",
    from_="+18664251786",
    body="This is a test"
)

# call.date
