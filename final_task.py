import requests

# API_ENDPOINTs for getting job openings
ARBIETNOW_API_ENDPOINT = "https://arbeitnow.com/api/job-board-api"
REED_UK_ENPOINT = "https://www.reed.co.uk/developers"
THE_MUSE_ENDPOINT = "https://www.themuse.com/developers/api/v2"

#  use this link to access reed uk api docs https://www.reed.co.uk/developers/Jobseeker
# To work with reed Uk APi we need API key for authentication
# I would be storing my API_KEY as a variable but ideally we would need to keep it in our environment file .env
# To get your api key simply register with a correct gmail to get the API KEY sent to you address example in API_KEY.PNG image
REED_UK_API_KEY = "bc012ea7-ab28-47f0-bdfe-20cd57dae1a4"

job_title = input("What Job are you in search of ? Enter a Job title e.g Python developer  ")
users_email = input("Enter e-mail address to get Job postings info")

#  making get request to arbietnow ,  read docs to understand better
response_arbietnow = requests.get(ARBIETNOW_API_ENDPOINT)
json_response = response_arbietnow.json() # the json response is quite ambiguous so we need to find a way to make it more readable

#  Do we all know that if we make a get request to this https://arbeitnow.com/api/job-board-api endpoint by simply typing it on google? 
#  so when you enter this endpoint on google is the same thing as making a get request wwith the requests module above
#  but in a situation whereby we have ambigous response and we need to visulaize easily we can use google 
#  using google we can copy the response and paste to http://jsonviewer.stack.hu/ which helps use pretify our resposnse

# images of google response and the pretified data are in pretify.png and google.png


# task 1 : now that you can visualise the response check if there are any roles relating to the user's requests and send
#  Job title and Job application link to user's email with subject " Job openings  ""

# Do the exact same thing for the rest of the endpoints don't forget to add API KEY if required andd you can't access an API with
#  API key via google you need to test using other softwares like postman

