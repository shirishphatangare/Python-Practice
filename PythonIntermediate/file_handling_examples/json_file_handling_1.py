#The built-in Python json module provides us with methods and classes that are used to
# parse and manipulate JSON in Python.
#Python comes with a built-in module called json for working with JSON data.

#The json.dump() method (without “s” in “dump”) used to write Python serialized object as JSON formatted data into a file.
# The file type can be anything including text, JSON or even binary file.

#The json.dumps() method encodes any Python object into JSON formatted String.

#Mapping between JSON and Python entities while Encoding
#To encode Python objects into JSON equivalent json module uses the following conversion table. The json.dump() and json.dumps() the method performs the translations when encoding.
# PYTHON	JSON
#dict ---> object
#list, tuple ---> array
#str --->	string
#int, float, int & float-derived Enums --->	number
#True --->	true
#False --->	false
#None --->	null

import json

# Example: use the Python json module to write Python serialized objects as JSON formatted data into file and string.
# Consider a scenario when you receive an HTTP request to send developer detail. you fetched developer data from
# the database table and store it in a Python dictionary or any Python object,
# Now you need to send that data back to the requested application so you need to convert
# Python dictionary object into a JSON formatted string to send as a response in JSON string.
# To do this you need to use json.dumps().
def SendJsonResponse(resultDict):
    print("Convert Python dictionary into JSON formatted String")
    developer_str = json.dumps(resultDict)
    print(developer_str)

# sample developer dict
developer_Dict = {
    "name": "Jane Doe",
    "salary": 9000,
    "skills": ["Python", "Machine Learning", "Web Development"],
    "email": "jane.doe@pynative.com"
}
SendJsonResponse(developer_Dict)

