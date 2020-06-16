
#Function compile():Regular expressions are compiled into pattern objects, which have methods for
# various operations such as searching for pattern matches or performing string substitutions.

# Module Regular Expression is imported using __import__().
import re

# compile() creates regular expression character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'.
p = re.compile('[a-e]')

# findall() searches for the Regular Expression and return a list upon finding
print(p.findall("Ay Hello, said Mr. Peter Patter"))

#Note:First occurrence is ‘e’ in “Hello” and not ‘A’, as it being Case Sensitive.
#Next Occurrence is ‘a’ in “said”, then ‘d’ in “said”, followed by ‘e’ in “Peter” and so on.
