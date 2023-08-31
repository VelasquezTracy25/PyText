from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)
client1 = Client(config.account_sid, config.auth_token)


call = client1.messages.create(
    to="12104730194",
    from_="+18664251786",
    body="This is a test.. again"
)

print("Message Sent")

# call.date
