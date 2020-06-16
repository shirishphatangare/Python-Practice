#Example: use parse_float and parse_int kwarg in json.load()

import json

def roundFloats(salary):
    return round(float(salary), 2)

def salartToDeduct(leaveDays):
    salaryPerDay = 465
    return int(leaveDays) * salaryPerDay

print("Load float and int values from JSON and manipulate it")
print("Started Reading JSON file")

with open("resources/developerDetails.json", "r") as read_file:
    developer = json.load(read_file, parse_float=roundFloats,
                          parse_int=salartToDeduct)
    # after parse_float
    print("Salary: ", developer["salary"])

    # after parse_int
    print("Salary to deduct: ", developer["leavedays"])
    print("Done reading a JSON file")