#Encode and Write JSON data to a file using json.dump()
#We can use it in the following cases.
#1.To write the JSON response in a file: Most of the time, when you execute a GET request,
# you receive a response in JSON format, and you can store JSON response in a file for future
# use or for an underlying system to use.
#2.For example, you have data in a list or dictionary or any Python object, and you want to
# encode and store it in a file in the form of JSON.

import json

# assume you have the following dictionary
developer = {
    "name": "jane doe",
    "salary": 9000,
    "email": "JaneDoe@pynative.com"
}
print("Started writing JSON data into a file")
with open("resources/developer.json", "w") as write_file:
    json.dump(developer, write_file) # encode dict into JSON
print("Done writing JSON data into .json file")