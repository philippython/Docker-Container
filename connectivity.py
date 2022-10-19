"""
I would be sending API requests to the following websites

- Amazon.com
- Github.com
- stackoverflow.com

Using the requests module
"""
from requests import *

website_list = ["https://github.com/", "https://stackoverflow.com/", "https://amazon.com/"]
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

success_response = [requester(url) if requester(url) == 200 else None for url in website_list]
error_response =  [requester(url) if requester(url) != 200 else None for url in website_list]
print(success_response)
print(error_response)
