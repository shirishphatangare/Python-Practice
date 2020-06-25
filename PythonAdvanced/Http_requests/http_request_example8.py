#Authentication Using Python Requests
#-refers to giving a user permissions to access a particular resource
#-To achieve this authentication,authentication data through Authorization header
# or a custom header defined by server

# import requests module
import requests
from requests.auth import HTTPBasicAuth

# Making a get request
response = requests.get('https://api.github.com/user,',
                        auth=HTTPBasicAuth('user', 'pass'))

# print request object
print(response)

"""
Types of Authentication
1)Digest Authentication
- Can be implemented as:

from requests.auth import HTTPDigestAuth
url = 'https://httpbin.org/digest-auth/auth/user/pass'
requests.get(url, auth=HTTPDigestAuth('user', 'pass'))

2)OAuth 1 Authentication
- several web APIs use OAuth
- requests-oauthlib library allows Requests users to easily make OAuth 1 authenticated requests
 
import requests
from requests_oauthlib import OAuth1
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET','USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)

- Requests is designed to allow other forms of authentication to be easily and quickly plugged in.

"""