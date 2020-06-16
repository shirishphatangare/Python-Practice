#Regular expressions are a powerful language for matching text patterns.
# The Python "re" module provides regular expression support.

#Documentation : https://docs.python.org/3/library/re.html
#Learning material Recommendation: https://developers.google.com/edu/python/regular-expressions

#Syntax: match = re.search(pat, str)
#The re.search() method takes a regular expression pattern and a string and searches for that pattern
# within the string. If the search is successful, search() returns a match object or None
# The search is usually immediately followed by an if-statement to test if the search succeeded


#Example: searches for the pattern 'word:' followed by a 3 letter word
import re

str = 'an example  word:The exp! word:cat .!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print('found group -- ', match.group()) ## 'found word:cat' - group() method acts group(0)
  print('found group(0) -- ', match.group(0))
else:
  print('did not find')