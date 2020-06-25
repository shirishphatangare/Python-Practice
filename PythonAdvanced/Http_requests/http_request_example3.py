#Query String Parameters
#- to customize a GET request is to pass values
#- helpful when you are searching for a webpage for some results or a specific image.
# You can provide these query strings as a dictionary of strings using the params
# keyword in the GET request.

import requests

#Passing Parameters in URL
print("-------Parameters in URL-------------")
resp = requests.get("https://httpbin.org/get?name=Abigail")
print(resp.text)

# Example use case: Search GitHub's repositories
print("-------Multiple Parameters-------------")

response = requests.get('https://pixabay.com/en/photos/',
    params={'q': 'Puppies', 'order': 'popular', 'min_width': '800', 'min_height': '600'})

# Print complete URL with params
print(response.url)
