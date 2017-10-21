from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc5173ddda5dea6f7c9b4398c0f80d545"
# Your Auth Token from twilio.com/console
auth_token  = "87e59826d7f49301f6bebedf32d21d51"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16623715507", 
    from_="+16622004204",
    body="I am the sms")

print(message.sid)


#9403040786