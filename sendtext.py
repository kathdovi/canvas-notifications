from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC84869c6273365b25abc7f71947391674"
# Your Auth Token from twilio.com/console
auth_token  = "523fde5645063b82470cdcaaf48cf97f"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19177929969", 
    from_="+12016769712",
    body="You have an assignment due in 3 hours!")

print(message.sid)
