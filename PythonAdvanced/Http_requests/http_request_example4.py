import requests
#When making a request to a URL/URI, different 'methods' can be used.
# These tell the server what sort of action you want to perform.
# HTTP defines actions like GET, POST, PUT, DELETE and many others.
#To use these different methods, simply replace the .get with .post/.put/.delete
# or whatever method you are using.

#POST request method requests that a web server accepts the data enclosed in the body
# of the request message, most likely for storing it
print("------Parameters Posted-----")
payload = {'user_name': 'admin', 'password': 'password'}
#Post requests
#In cases where you want to send some form-encoded data
# (like a HTML form would submit), we can pass key-value pairs as we used above to
# the data parameter. The dictionary of your data will be form-encoded when the
# request is made.
res = requests.post("http://httpbin.org/post", data=payload) # payload is form-encoded dict
print("URL Payload",res.url)
print(res.text)

print("--------------Passing Data as JSON------------------------------")
res = requests.post('http://httpbin.org/post', json=payload) # payload is json object
# The Content-Type header will automatically be set to application/json when passing data to json
print("URL Payload(JSON Data)",res.url)
print("JSON Data:",res.text)

print("--------------Passing Raw Data------------------------------")
#where you want to specify exactly what is in the body manually, simply provide the string to the body parameter
sample_data="This is raw data being passed"
res = requests.post('http://httpbin.org/post', data=sample_data) # payload is raw text
print("Manual Data(Body)",res.url)
print("Manual Data:",res.text)

print("--------------Delete Method------------------------------")
#Sending Files with delete requests
res = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print("Delete Requests:",res.status_code)# == 400 # Check for HTTP 200 (OK)

print("--------------Head Request------------------------------")
res = requests.head('https://jsonplaceholder.typicode.com/posts/1')
print("Head Requests:",res.status_code)# == 400 # Check for HTTP 200 (OK)

"""
Put Vs Post
1)- PUT request is made to a particular resource. If the Request-URI refers to an already 
existing resource, an update operation will happen, otherwise create operation 
should happen if Request-URI is a valid resource URI (assuming client is allowed 
to determine resource identifier).
Example – PUT /article/{article-id}
- POST method is used to request that the origin server accept the entity enclosed in the
request as a new subordinate of the resource identified by the Request-URI in the Request-Line. 
It essentially means that POST request-URI should be of a collection URI.
Example – POST /articles

2)-PUT method is idempotent. So if you send retry a request multiple times, 
that should be equivalent to single request modification.
- POST is NOT idempotent. So if you retry the request N times, you will end up having 
N resources with N different URIs created on server.

3)-Use PUT when you want to modify a single resource which is already a part of 
resources collection. PUT overwrites the resource in its entirety. 
Use PATCH if request updates part of the resource.
- Use POST when you want to add a child resource under resources collection.

4)-As a practice,use PUT for UPDATE operations and POST for CREATE operations.
"""