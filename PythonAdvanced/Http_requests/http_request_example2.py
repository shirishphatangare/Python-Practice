
import requests
from requests.exceptions import HTTPError

for url in ['https://www.google.com/search?q=hello', 'https://api.github.com/invalid','https://reactjs.org/docs/hooks-effect.html']:
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        print("----------Response: Byte Format------------")
        # .content gives you access to the raw bytes of the response payload
        print(response.content)
        print("----------Response: Text Format------------")
        print(response.text)
        print("----------Response: Json Format------------")
        print(response.json())
        # Headers:The response headers can give you useful information, such as
        # the content type of the response payload and a time limit on how long
        # to cache the response.
        print("----------Response: Header Information------------")
        print(response.headers)
        #returns a dictionary-like object, allowing you to access header values by key.
        print("Header Content Type:",response.headers['Content-Type'])
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
