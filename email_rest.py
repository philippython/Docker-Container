from smtplib import SMTP
import requests
import os


API_ENDPOINT = 'https://user-mangement-api.herokuapp.com/'
SMTP_HOST = "smtp.gmail.com"
MAIL_SENDER = "odulajaphilip@gmail.com"
MAIL_SENDER_PASSWORD="kyvycjacqhjasctx"
# MAIL_SENDER = os.getenv("SENDER_EMAIL")
# MAIL_SENDER_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")
print("running")

# setting up mail configuration
def send_update(status, json):
    with SMTP(SMTP_HOST) as connection:
        connection.starttls()
        connection.login(user=MAIL_SENDER, password=MAIL_SENDER_PASSWORD)

        # previous code no parameter in sendmail called subject
        # connection.sendmail(from_addr=MAIL_SENDER, to_addrs=MAIL_SENDER, subject=f"Post Request Update:{status}", msg=json)

        connection.sendmail(from_addr=MAIL_SENDER,
                            to_addrs=MAIL_SENDER, 
                            msg=f"Subject:Post Request Update:{status}\n\n{json}")

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
    send_update("Successful", add_user_request.json())
else:
    send_update("Failed", add_user_request.json())
    

# 200 succus
# 400 bad request 
# 404 not found
# 500 the server is having issues
