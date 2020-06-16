# RE Defines  total of 14 metacharacters
"""
\   Used to drop the special meaning of character
    following it (discussed below)
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline - zero or more occurrences
+   One or more occurrences
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
{}  Indicate number of occurrences of a preceding RE to match.
()  Enclose a group of REs
"""

#The basic rules of regular expression search for a pattern within a string are:
#1. The search proceeds through the string from start to end, stopping at the first match found
#2.All of the pattern must be matched, but not all of the string
#3. If match = re.search(pat, str) is successful, match is not None and match.group() is the matching text

import re
#Examples: Basic Search
  ## Search for pattern 'iii' in string 'piiing'.
  ## All of the pattern must match, but it may appear anywhere.
  ## On success, match.group() is matched text.
match = re.search(r'iii', 'piiing') # found, match.group() == "iii"
match = re.search(r'igs', 'piiing') # not found, match == None

  ## . = any char but \n
match = re.search(r'..g', 'piiing') # found, match.group() == "iig"

  ## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123ng') # found, match.group() == "123"
match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"