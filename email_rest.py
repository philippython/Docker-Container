from smtplib import SMTP_SSL
from email.message import EmailMessage
from dotenv import load_dotenv
import ssl
import requests
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
def send_update(status, json):
    mail = EmailMessage()
    mail.to, mail.subject , mail['from'] = MAIL_SENDER, f"Subject:Post Request Update:{status}" , MAIL_SENDER
    mail.set_content(json)

    context = ssl.create_default_context()
    with SMTP_SSL(SMTP_HOST, port=465, context=context) as connection:
        connection.starttls()
        connection.login(user=MAIL_SENDER, password=MAIL_SENDER_PASSWORD)

        connection.sendmail(from_addr=MAIL_SENDER,
                            to_addrs=MAIL_SENDER, 
                            msg=mail.as_string())

data = {
        "firstname": "tunji",
        "lastname": "yusuff",
        "email": "demo@gmail.com",
        "phone": 352537458,
        "sex": "male",
        "country": "Nigeria",
}

add_user_request = requests.post(url=f'{API_ENDPOINT}/add_user', data=data)
print(add_user_request.json())
if add_user_request.status_code == 200:
    print(add_user_request.json())
    send_update("Successful", add_user_request.json())
else:
    send_update("Failed", add_user_request.json())
    

# 200 succus
# 400 bad request 
# 404 not found
# 500 the server is having issues
