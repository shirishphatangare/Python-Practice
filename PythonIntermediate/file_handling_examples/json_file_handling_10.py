#Example: Convert JSON String to Python dictionary using json.loads()

import json

developerJsonString = """{
    "name": "jane doe",
    "salary": 9000,
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "JaneDoe@pynative.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
"""

print("Started converting JSON string document to Python dictionary")
developerDict = json.loads(developerJsonString)

print("Printing key and value")
print(developerDict["name"])
print(developerDict["salary"])
print(developerDict["skills"])
print(developerDict["email"])
print(developerDict["projects"])

print("Done converting JSON string document to a dictionary")