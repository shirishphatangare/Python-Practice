"""
1. Create a list named "l" with the following values ([1, 4, 9, 10, 23]). Using the Python
documentation about lists (https://docs.python.org/3.5/tutorial/introduction.
html#lists) solve the following exercises:
1. Using list slicing get the sublists [4, 9] and [10, 23].
2. Append the value 90 to the end of the list "l". Check the difference between list
concatenation and the "append" method.
3. Calculate the average value of all values on the list. You can use the "sum" and
"len" functions.
4. Remove the sublist [4, 9].
"""

# 1. Using list slicing
l = [1, 4, 9, 10, 23]
print(l[1:3])
print(l[3:])

# 2. Append the value 90 to the end of the list "l"
l.append(90)
print(l)

# concatenation operator (+)
list_1 = [1,2,3]
list_2 = [4,5,6]
print(list_1 + list_2)

# concatenation using unpacking operator (*)
list_1 = [1,2,3]
list_2 = [4,5,6]
result = [*list_1,*list_2]
print(result)

# Concatenation using List Comprehension
list_1 = [1,2,3]
list_2 = [4,5,6]
result = [element for lis in [list_1, list_2] for element in lis]
print(result)

# Concatenation using List extend() function
list_1 = [1,2,3]
list_2 = [4,5,6]
list_1.extend(list_2) # extend() function returns None. Output will be in list_1
print(list_1)

# Concatenation using itertools.chain() method
import itertools

list_1 = [1,2,3]
list_2 = [4,5,6]
print(list(itertools.chain(list_1,list_2)))

# 3. Calculate the average value of all values on the list. - for loop
list = [1, 4, 9, 10, 23]
sum_of_elements = 0;
no_of_elements = len(list)

for i in range (0,no_of_elements):
    sum_of_elements += list[i]

print("Average of all values on the list is: ", sum_of_elements / no_of_elements)


# 3. Calculate the average value of all values on the list. - sum(iterable, start) function
list = [1, 4, 9, 10, 23]
no_of_elements = len(list)
print("Average of all values on the list is: ", sum(list) / no_of_elements)

# General Tip: Use globals().clear() to clear all console variables if causing problems

# 4. Remove the sublist [4, 9].
list = [1, 4, 9, 10, 23]
# Deleting a sublist
del list[1:3]
print(list)

# Extracting a sublist
new_list = list[1:3]
print(new_list)