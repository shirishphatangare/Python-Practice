"""
2. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Sample:  Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

input_data = input("Enter random words to be sorted alphabetically (comma-separated): ").split(',')
input_data.sort()
#print("Sorted output is: ", *input_data)    # Unpacking do not give comma separated output
print("Sorted output is: ", (",").join(input_data))