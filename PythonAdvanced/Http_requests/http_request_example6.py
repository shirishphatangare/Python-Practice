#Sending Cookies and Headers
#Cookies are used as state management, and as such as usually set by the server to be stored and returned by the client.
#Access the cookies and headers that the server sends back to you using req.cookies and req.headers
#Requests also allow you to send your own custom cookies and headers with a request.
#To add HTTP headers ,pass them in a dict to the headers parameter.
#send your own cookies to a server using a dict passed to the cookies parameter.

import requests
url = 'https://httpbin.org/cookies/set/abc/123'
headers = {'user-agent': 'your-own-user-agent/0.0.1'}
cookies = {'last-visit-month': 'April'}
res = requests.get(url, headers=headers, cookies=cookies)
print("--------Cookies and Headers Passed--------")
print(res.text)
print("Fetching the Cookiee(visit-month):",res)

#Cookies can also be passed in a Cookie Jar to allow you to use those cookies over multiple paths.
print("--------Cookie Jar--------")
jar = requests.cookies.RequestsCookieJar()
jar.set('first_cookie', 'first', domain='httpbin.org', path='/cookies')
jar.set('second_cookie', 'second', domain='httpbin.org', path='/others')
jar.set('third_cookie', 'third', domain='httpbin.org', path='/cookies')

url = 'http://httpbin.org/cookies'
res = requests.get(url, cookies=jar)
print(res.text)

# printing request cookies
print(jar)
print(res.cookies)

#Loop through the jar
print("----Looping through Cookies: For Loop")
#Get all http response cookies by invoking res.cookies property.
for cookie in res.cookies:
    print('cookie domain = ' + cookie.domain)
    print('cookie name = ' + cookie.name)
    print('cookie value = ' + cookie.value)
    print('*************************************')

#The RequestsCookieJar class also provide methods such as items(), iteritems(), iterkeys(),
# itervalues(), keys(), values() to loop all cookie’s key or values in response
# ( each cookie has a key and a value. ).
print("----Looping through Cookies: items")
for item in res.cookies.items():
    print(item)
