#Example: Handle non-ASCII characters from JSON data while writing it into a file
#The json.dumps() method has ensure_ascii parameter. The ensure_ascii is by-default true.
# The output is guaranteed to have all incoming non-ASCII characters escaped.
# If ensure_ascii is false, these characters will be output as-is.

import json

unicode_string1 = u"\u0042"
print("unicode String is ", unicode_string1)

# set ensure_ascii=False
print("JSON character encoding by setting ensure_ascii=False")
print(json.dumps(unicode_string1, ensure_ascii=False))
print("JSON character encoding by setting ensure_ascii=True")
print(json.dumps(unicode_string1))


unicode_string2 = u"\u00F8"
print("unicode String is ", unicode_string2)

# set ensure_ascii=False
print("JSON character encoding by setting ensure_ascii=False")
print(json.dumps(unicode_string2, ensure_ascii=False))
print("JSON character encoding by setting ensure_ascii=True")
print(json.dumps(unicode_string2))