"""
I would be sending API requests to the following websites

- Amazon.com
- Github.com
- stackoverflow.com

Using the requests module
"""
from requests import *

website_list = ["https://examplxyzzzze.com/", "https://fakbookyryk.com/", "https://amazyxson.com/"]

# use the list below to test for invalid websites
# ["https://example.com/", "https://fakbook.com/", "https://amazon.com/"]

# requests header
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
}

def requester(url):

    try:
        response = get(url, headers=header)
    except exceptions.ConnectionError:
        return 404
    else:
        return response.status_code

success_response = [requester(url) for url in website_list if requester(url) == 200]
error_response =  [url for url in website_list if requester(url) != 200]

print(success_response, error_response)
# return connectivity information
if error_response == len(website_list):
    print("This computer is connected to the internet")

# elif error_response == len(website_list):
#     print('This computer is completely offline and not connected to the internet')

# else:
#     retry_one = [url for url in error_response if requester(url) != 200]

#     # checks if we still get an invalid connection 
#     if not retry_one:
#         print("This computer is now connected to the internet")
#     else:
#         retry_two = [url for url in retry_one if requester(url) != 200]
#         # checks if we still get an invalid connection 
#         if not retry_two:
#             print('='*20, 'THE WEBSITE BELOW ARE PROBABLY OFFLINE', '='*20)
#             for website in retry_two:
#                 print(website)


