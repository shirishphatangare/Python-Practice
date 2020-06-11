#Example of an If statement
#input(): fetches values from users and returns a string
mynumber = int(input("Please enter an integer value:"))
if mynumber<0:
    print("Negative Integer")
elif mynumber==0:
    print("Its Zero")
else:
    print("Its a Positive Number")

#Notes
#1. Python doesnt have blocks. It relies on indentation
#2. Every flow control statement typically ends with a colon
#3. == is a comparison operator
#4. No parentheses in if, elif or else

#Assignment: Find out the largest of the 3 numbers thats been taken as input from the user

mynumber1 = int(input("Please enter first integer value: "))
mynumber2 = int(input("Please enter second integer value: "))
mynumber3 = int(input("Please enter third integer value: "))

num_list = [mynumber1,mynumber2,mynumber3]

max_number = num_list[0];

for number in num_list[1:]:
    if number > max_number:
        max_number = number

print("Maximum number is: ", max_number)

# pip install camelcase
from camelcase import CamelCase

c = CamelCase()
s = 'this is a sentence that needs CamelCasing!'
print(c.hump(s))
# This is a Sentence That Needs CamelCasing!