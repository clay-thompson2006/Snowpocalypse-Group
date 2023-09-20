from twilio.rest import Client

account_sid = "AC823b7b5840f23f6cf0c953566d304dc9"
auth_token = "c5b77ab69eb741e0228f0de412f59d63"
client = Client(account_sid, auth_token)

sender_phone_number = "+18559663985"  # Your Twilio phone number
recipient_phone_number = "+1 330 446 0711"  # Recipient's phone number

message = client.messages.create(
    body="Mr. Sekol This is your alarm to tell you that there might be a snow day so have fun with the puppers and have a great day.",
    from_=sender_phone_number,
    to=recipient_phone_number
)

print("SMS sent with SID:", message.sid)
