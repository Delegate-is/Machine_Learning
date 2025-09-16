# Uppercase and lowercase in a string
s = "Hello232 MAX2 dEEL34"
u = 0
l = 0
d = 0
for i in s:
    if i.isupper():
        u += 1
    if i.islower():
        l += 1
    if i.isdigit():
        d += 1
        
print(f"Total uppercase = {u}")
print(f"Total lowercase = {l}")
print(f"Total digits = {d}")

import string
import random
# Program to generate OTP on user_request and send code to mobile no
user_r = input("Would you like to generate OTP or not? y/n  :")
length = int(input("Enter a length: "))
l= length
if user_r == 'y':
    result = "".join(random.choices(string.digits + string.ascii_uppercase, k=l))
    print(result)
else:
    print("Okey, don't worry")
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
