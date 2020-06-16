#Repetition
#+ -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
#* -- 0 or more occurrences of the pattern to its left
#? -- match 0 or 1 occurrences of the pattern to its left

#Note: First the search finds the leftmost match for the pattern, and second it tries to use up
# as much of the string as possible -- i.e. + and * go as far as possible

import re

## i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiig') # found, match.group() == "piii"
print(match.group())

## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"
print(match.group())

## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # found, match.group() == "1 2   3"
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found, match.group() == "12  3"
match = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, match.group() == "123"

## ^ = matches the start of string, so this fails:
match = re.search(r'^b\w+', 'foobar') # not found, match == None
## but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar') # found, match.group() == "bar"

#Example:Suppose you want to find the email address inside the string 'xyz alice-b@google.com purple monkey'.
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print("Email Match Found:",match.group())  ## 'b@google'

#The search does not get the whole email address in this case because the \w does not match the '-' or '.' in the address.
# We'll fix this using the regular expression features
match = re.search(r'[\w-]+@[\w.]+', str)
if match:
    print("Complete Email:",match.group()) ## 'alice-b@google.com'