"""

3.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Sample: Suppose the following input is supplied to the program:
Hello world
Practice makes perfect

--->Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""
print("Enter sequence of lines to be capitalized: ")
output = []

while True:
    input_line = input()

    #if(input_line.strip() != ""):
    if (input_line.strip()):
        output.append(input_line.upper())
    else:
        break

print("Capitalized output is: ")
print("\n".join(output))
