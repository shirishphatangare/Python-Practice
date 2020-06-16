#Python JSON Parsing using json.load and loads()
#Using the json.load() and json.loads() method, you can turn JSON encoded/formatted data into
# Python Types this process is known as JSON decoding.

#json.load() method (without “s” in “load”) used to read JSON encoded data from a file and
# convert it into Python dictionary.
#json.loads() method, which is used for parse valid JSON String into Python dictionary.

# Example: Read JSON data from a file and convert it into dict using json.load()

import json

print("Started Reading JSON file")
with open("resources/developer.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    developer = json.load(read_file)
    print('Data type of the variable:',type(developer))

    print("--------Decoded JSON Data From File----------")
    for key, value in developer.items():
        print(key, ":", value)
    print("Done reading json file")