#Example: Write Indented and pretty printed JSON data into a file using the dump method
#If the user wants to read JSON file so it must be readable and well organized,
# so whosever consumes this will have a better understanding of a structure of a data.
# The dump() method provides the following arguments to pretty-print JSON data.

#The indent parameter specifies the spaces that are used at the beginning of a line.
#The separator argument of a json.dump method you can specify any separator between key and
# value.
#The sort_keys to sort JSON data by keys.

import json

developer = {
    "name": "jane doe",
    "salary": 9000,
    "skills": ["Raspberry pi", "Machine Learning", "Web Development"],
    "email": "JaneDoe@pynative.com"
}

with open("resources/developerPrettyPrint.json", "w") as write_file:
    json.dump(developer, write_file, indent=4, separators=(", ", ": "), sort_keys=True)
print("Done writing pretty printed JSON data into a file")