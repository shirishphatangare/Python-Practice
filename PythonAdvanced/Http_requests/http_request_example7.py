import requests

#Working with Request Sessions
#- Eventually, you will run into situations where you must persist a user session.
#-Session object allows one to persist certain parameters across requests.
# It also persists cookies across all requests made from the Session instance and
# will use urllib3’s connection pooling. So if several requests are being made to the
# same host, the underlying TCP connection will be reused, which can result in a
# significant performance increase. A session object all the methods as of requests.

# Let’s say you first have to log in/authenticate, which sets a browser cookie that
# must be sent with each subsequent request.
#- Using httpbin , we will save a cookie and then try to retrieve it.

with requests.Session() as session:
    res = session.get('https://httpbin.org/cookies/set/uname/FakeUser')
    print('res: {}'.format(res.text))
    #The returned request.sessions.Session object provide a lot of attributes
    # and method for you to access such as web page by url, headers, cookies
    # value in the same session.
    res = session.get('https://httpbin.org/cookies')
    print('res: {}'.format(res.text))
    print(session.cookies)
    print('actual cookies: {}'.format(session.cookies.get_dict()))

#The Session object uses urllib3’s connection pooling. This means that the underlying
# TCP connection will be reused for all the requests made to the same host.
#This can significantly boost the performance.
print("------------Multiple Connections-------------")

ssn = requests.Session()
reqZero = ssn.get('http://httpbin.org/cookies/set/uname/FakeUser')
ssn.cookies.update({'visit-month': 'June'})
print(reqZero.text)

reqOne = ssn.get('http://httpbin.org/cookies')
print(reqOne.text)
# prints information about "visit-month" cookie

reqTwo = ssn.get('http://httpbin.org/cookies', cookies={'visit-year': '2020'})
print(reqTwo.text)
# prints information about "visit-month" and "visit-year" cookie

reqThree = ssn.get('http://httpbin.org/cookies')
print(reqThree.text)
# prints information about "visit-month" cookie