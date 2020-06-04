"""
Take the following python dictionary:

ages = {
"Peter": 10,
"Isabel": 11,
"Anna": 9,
"Thomas": 10,
"Bob": 10,
"Joseph": 11,
"Maria": 12,
"Gabriel": 10,
}

1. How many students are in the dictionary? Search for the "len" function.
2. Implement a function that receives the "ages" dictionary as parameter and return
the average age of the students. Traverse all items on the dictionary using the
"items" method as above.
3. Implement a function that receives the "ages" dictionary as parameter and returns
the name of the oldest student.
4. Implement a function that receives the "ages" dictionary and a number "n" and
returns a new dict where each student is n years older. For instance, new_ages(ages,10) returns a copy of "ages" where each student is 10 years older.

"""

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

# 1
print("Length of dictionary is: ", len(ages))

# 2
def get_average_ages(ages):
    sum_of_elements = 0

    # items() method returns a list of a given dictionary’s (key, value) tuple pair.
    for item in ages.items():
        sum_of_elements += item[1]   # access tuple element by index

    return sum_of_elements / len(ages)

print("Average age is: ", get_average_ages(ages))

# 3
def get_oldest_student(ages):
    max_age = max(ages.values())
    student_names = [k for k, v in ages.items() if v == max_age] # list comprehension
    return student_names

print("Oldest student name is: ", get_oldest_student(ages))

#4
def new_ages(ages,n):
    student_names = [(k1, v1) for k1, v1 in ages.items() if n == v1] # list comprehension to create a list of tuples
    return dict(student_names) # convert list of tuples to dictionary using dict() method

print("New ages list is: ", new_ages(ages,10))