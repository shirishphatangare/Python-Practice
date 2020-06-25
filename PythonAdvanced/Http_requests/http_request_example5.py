import requests
from requests.exceptions import Timeout

try:
    # By default, requests will wait indefinitely on the response, so you should almost always
    # specify a timeout duration to prevent these things from happening.
    response = requests.get('https://api.github.com', timeout=1) # no. of seconds
    # If the request times out, then the function will raise a Timeout exception:

    # You can also pass a tuple to timeout with the first element being a connect timeout
    # (the time it allows for the client to establish a connection to the server), and the
    # second being a read timeout (the time it will wait on a response once your client has
    # established a connection):    #
    # requests.get('https://api.github.com', timeout=(2, 5))
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')