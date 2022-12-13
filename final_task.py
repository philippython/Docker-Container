import requests

# API_ENDPOINTs for getting job openings
ARBIETNOW_API_ENDPOINT = "https://arbeitnow.com/api/job-board-api"
REED_UK_ENPOINT = "https://www.reed.co.uk/developers"
THE_MUSE_ENDPOINT = "https://www.themuse.com/developers/api/v2"

#  use this link to access reed uk api docs https://www.reed.co.uk/developers/Jobseeker
# To work with reed Uk APi we need API key for authentication
# I would be storing my API_KEY as a variable but ideally we would need to keep it in our environment file .env
# To get your api key simply register with a correct gmail to get the API KEY sent to you address
REED_UK_API_KEY = "bc012ea7-ab28-47f0-bdfe-20cd57dae1a4"

job_title = input("What Job are you in search of ? Enter a Job title e.g Python developer")

#  making get request to arbietnow ,  read docs to understand better
response_arbietnow = requests.get(ARBIETNOW_API_ENDPOINT)
print(response_arbietnow.json())

