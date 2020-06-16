#Python CSV Module
#-Python provides a CSV module to handle CSV files.
#-To read/write data, you need to loop through rows of the CSV.
# -You need to use the split method to get data from specified columns.

#Documentation: https://docs.python.org/3/library/csv.html

#Some of the functions are:
#csv.field_size_limit – return maximum field size
#csv.get_dialect – get the dialect which is associated with the name
#csv.list_dialects – show all registered dialects
#csv.reader – read data from a csv file
#csv.register_dialect - associate dialect with name
#csv.writer – write data to a csv file
#csv.unregister_dialect - delete the dialect associated with the name the dialect registry
#csv.QUOTE_ALL - Quote everything, regardless of type.
#csv.QUOTE_MINIMAL - Quote fields with special characters
#csv.QUOTE_NONNUMERIC - Quote all fields that aren't numbers value
#csv.QUOTE_NONE – Don't quote anything in output

import csv

#Example 1: Reading the file
print("----Reading a CSV File---")
with open('resources/myData.csv','rt')as csv_file: # t means Text mode
  data = csv.reader(csv_file)
  for row in data:
        print(row)


#Example 2: Reading the file into a Dictionary
print("--------Read a CSV as a Dictionary---------------")
#You can also use DictReader to read CSV files.
# The results are interpreted as a dictionary where the header row is the key, and other rows are values.
reader = csv.DictReader(open("resources/myData.csv"))
for raw in reader:
    print(raw)

#Example 3: Writing to a CSV File
print("--------Writing to a CSV File---------------")
#to store in a CSV file you have to use writer() function.
#To iterate the data over the rows(lines), use the writerow() function.
with open('resources/writeData.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #way to write to csv file
    writer.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
    writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
    writer.writerow(['Java', 'James Gosling', '1995', '.java'])
    writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])


#Example 4: Writing to a CSV File mapping output to the Dictionary
print("--------Writing to a CSV File---------------")
with open('resources/HPCharacters.csv', 'w', newline='') as csvfile:
    #The fieldnames parameter is a sequence of keys that identify the order in which values in
    # the dictionary passed to the writerow() method are written to file
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': 'Harry', 'last_name': 'Potter'})
    writer.writerow({'first_name': 'Ron', 'last_name': 'Weasley'})
    writer.writerow({'first_name': 'Dolores', 'last_name': 'Umbridge'})
    writer.writerow({'first_name': 'Albus', 'last_name': 'Dumbeldore'})
    writer.writerow({'first_name': 'Hermoine', 'last_name': 'Granger'})
    writer.writerow({ 'last_name': 'Griffindor','first_name': 'Godrick'})

#Example:Reading a file with an alternate format:
print("--------Reading a file with an alternate format---------------")
import csv
with open('resources/passwd.csv', newline='') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)