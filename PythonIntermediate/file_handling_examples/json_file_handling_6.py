#Example: Skip nonbasic types while writing JSON into a file using skipkeys parameter
#If Python dictionary contains a custom Python object as one of the keys and if we try to convert it into a JSON format, you will get a TypeError
# i.e., Object of type "Your Class" is not JSON serializable.

#If this custom object isn’t required in JSON data, you can skip it using a skipkeys=true
# argument of the json.dump() method.
#If skipkeys=true is True, then dict keys that are not of a basic type
# (str, int, float, bool, None) will be skipped instead of raising a TypeError

import json

class PersonalInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print("Developer name is " + self.name, "Age is ", self.age)

dev = PersonalInfo("John", 36)

developer_Dict = {
    PersonalInfo: dev,
    "salary": 9000,
    "skills": ["Python", "Machine Learning", "Web Development"],
    "email": "jane.doe@pynative.com"
}

print("Writing JSON data into file by skipping non-basic types")

with open("resources/developer.json", "w") as write_file:
    json.dump(developer_Dict, write_file, skipkeys=True)
    #json.dump(developer_Dict, write_file) # Error - TypeError: keys must be str, int, float, bool or None

print("Done")