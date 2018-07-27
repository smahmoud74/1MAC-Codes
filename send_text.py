from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACcd44e77adc8f816d46751b7cc9fb520d"
# Your Auth Token from twilio.com/console
auth_token  = "1e38375ddd84a99e00ff5beb1cbaa023"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+9647901481428", 
    from_="+1651358",
    body="Hello from Sinan!")

print(message.sid)
