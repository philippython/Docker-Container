"""
I would be sending API requests to the following websites

- Amazon.com
- Github.com
- stackoverflow.com

Using the requests module
"""
import requests 

website_list = ["https://github.com/", "https://stackoverflow.com/", "https://amazon.com/"]
# making requests to all websites using Mapping

#  the code below sends a requests to all websites in the website_list
connectivity_mapper = map(lambda url : requests.get(url).status_code, website_list)

#  getting all status_code of request made
status_codes = list(connectivity_mapper)