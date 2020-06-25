#HTTP Requests in Python
"""
we can use several HTTP libraries like:
- httplib
- urllib
- requests
"""

#- The requests library is the de facto standard for making HTTP requests in Python.
#- It abstracts the complexities of making requests behind a beautiful, simple API so that you
# can focus on interacting with services and consuming data in your application.
#-Requests play a major role is dealing with REST APIs, and Web Scrapping.

#Getting Started With requests
#Command Line: pip install requests

#1. The GET Request
#HTTP methods such as GET and POST, determine which action you’re trying to perform
# when making an HTTP request.
#- To make a GET request, invoke requests.get() : requests.get('https://api.github.com').

#2. The Response
#A Response is a powerful object for inspecting the results of the request.
# response = requests.get('https://api.github.com')

#3.Status Codes
#The first bit of information that you can gather from Response is the status code.
# A status code informs you of the status of the request.
# E.g. a 200 OK status - request was successful,
# a 404 NOT FOUND status - resource you were looking for was not found.
# List of other status code: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# Get the status code using the Response object: response.status_code
# If you use a Response instance in a conditional expression, it will evaluate to True if
# the status code was between 200 and 400, and False otherwise.


import requests

# Extracting data from URL - #This function then returns a requests.models.Response object.
response = requests.get('https://reactjs.org/docs/hooks-effect.html')
print("Type of Object received from get(): ",type(response))
# print check if an error has occurred
print("Check for Error: ",response.raise_for_status())

"""
Some attributes of Response are:
.content: The raw content of the response - umformatted
.text: The text content of the response - formatted
.status_code: The status code of the response; e.g. 200 OK, 404 Not Found, 418 Short and Stout...
.headers: The headers of the response
.cookies: The cookies returned in the response. You can access cookie value like you would use a dict: response.cookies['logged_in'].
"""
print("Content: ",response.text)
print("Text: ",response.content)
print("Encoding: ",response.encoding)
print("Response Code: ",response.status_code)
# Returns a text corresponding to the status code
print("Reason for the Response Code: ",response.reason)

# Elapsed returns a timedelta object with the time elapsed from sending the request to
# the arrival of the response. It is often used to stop the connection
# after a certain point of time is “elapsed”
print("Elapsed: ",response.elapsed)
print("URL: ",response.url)
print("History: ",response.history)
print("Headers: ",response.headers['Content-Type'])

"""
Tto access the actual content:
- response.text: content you are accessing is text
- response.content: non-text responses, you can access them in binary form
- response.json():  access the json-encoded content of the response
- response.raw: get the raw response from the server. pass stream=True in the request to get the raw response
"""

print("-----------------JSON------------------")
# If a site returns a JSON response, you can call .json() on the Response object to
# convert the JSON object in the response to a Python dictionary.
request = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = request.json()
print('Title: ' + data['title'])


