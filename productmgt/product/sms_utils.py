from twilio.rest import Client

def send_otp_via_sms(mobile_number, otp):
    # Your Twilio credentials
    account_sid = "YOUR_TWILIO_ACCOUNT_SID"
    auth_token = "YOUR_TWILIO_AUTH_TOKEN"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Your OTP code is {otp}",
        from_="+1234567890",   # your Twilio phone number
        to=mobile_number
    )
    return message.sid
