from smtplib import SMTP_SSL
from email.message import EmailMessage
from dotenv import load_dotenv
import ssl
import requests
import json
import os

# the load_dotenv function takes in dotenv_path parameter which is the .env file location
load_dotenv(dotenv_path=".env")

API_ENDPOINT = 'https://user-mangement-api.herokuapp.com/'
SMTP_HOST = "smtp.gmail.com"
MAIL_SENDER = os.getenv("SENDER_EMAIL")
MAIL_SENDER_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75\
            Safari/537.36'
           }



# Function below sends mail and request update using ssl and smtp
def send_update(status, response):
    mail = EmailMessage()
    mail.to, mail['from'] = MAIL_SENDER , MAIL_SENDER
    mail.set_content(json.dumps(response))

    context = ssl.create_default_context()
    # change port number from 587 to 465 
    with SMTP_SSL(SMTP_HOST, port=465, context=context) as connection:
        connection.login(user=MAIL_SENDER, password=MAIL_SENDER_PASSWORD)

        connection.sendmail(from_addr=MAIL_SENDER,
                            to_addrs=MAIL_SENDER, 
                            msg= f"Subject:Post Request Update:{status}\n\n{mail.as_string()}")

data = {
        "firstname": "tunji",
        "lastname": "yusuff",
        "email": "demo@gmail.com",
        "phone": 352537458,
        "sex": "male",
        "country": "Nigeria",
}

add_user_request = requests.post(url=f'{API_ENDPOINT}/add_user', data=data)
if add_user_request.status_code == 200:
    print(add_user_request.json())
    send_update("Successful", add_user_request.json())
else:
    send_update("Failed", add_user_request.json())
    
# Make request to every other endpoint

# 200 success
# 400 bad request 
# 404 not found
# 500 the server is having issues
