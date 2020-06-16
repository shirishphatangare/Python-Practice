#Example: Compact encoding to save file space by changing JSON key-value separator
#If the user wants to read JSON file so it must be readable and well organized,
# We can write JSON data into a file by changing JSON key-value separator. You can change JSON
# representation as per your needs. Using the separator argument of a json.dump() method you
# can specify any separator between key and value.
#
# To limit the JSON file size we can remove extra spacing between JSON key-value and use the compact encoding (separators=(',', ':')).
# Using this separator we can remove the whitespaces from JSON to make the JSON more compact and save bytes from being sent
# via HTTP.

import json

developer_dict = {
    "name": "jane doe",
    "salary": 9000,
    "skills": ["Raspberry pi", "Machine Learning", "Web Development"],
    "companies": ["Google", "Facebook", "IBM"],
    "email": "JaneDoe@pynative.com"
}

print("Started writing compact JSON data into a file")
with open("resources/developerDetailCompact.json", "w") as write_file:
    json.dump(developer_dict, write_file, separators=(',', ':'))
print("Done writing compact JSON data into json file")