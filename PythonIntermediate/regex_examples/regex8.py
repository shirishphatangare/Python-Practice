#Example: Check for a valid URL
"""
Checks for an string  if a URL ...

    starts with https://, or http://, or www.
    or ends with a dot extension
"""
import re;

pattern = '^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'

#pattern = '^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*\/?$' # optimized

str_true = ('https://github.com',
            'http://github.com',
            'www.github.com',
            'github.com',
            'test.de',
            'https://github.com/rasbt',
            'test.jpeg'  # !!!
            )

str_false = ('testmailcom', 'http:testmailcom',)

for t in str_true:
    print(t,":",re.match(pattern, t))
for f in str_false:
    print(f,":",re.match(pattern, f))