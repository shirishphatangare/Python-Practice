"""
1. Compiling Regular Expressions
- Regular expressions are compiled into Pattern objects, which have methods for various
operations such as searching for pattern matches or performing string substitutions.
Syntax:  re.compile(pattern, flags=0)
- Compile a regular expression pattern, returning a pattern object.
- The regular expression is passed to re.compile() as a string.
- Regular expressions are handled as strings because regular expressions aren’t
part of the core Python language, and no special syntax was created for expressing them.
- Regular expression patterns are compiled into a series of bytecodes which are
then executed by a matching engine written in C.

"""
import re

pattern = re.compile("hello")
print(pattern)

#to ignore letter case in the regex pattern.
pattern = re.compile("hello", flags=re.I)
print(pattern)

#If you are using the same regular expression multiple times, it is recommended to compile it for improved performance.
"""
Pattern objects have several methods and attributes.
- match():Determine if the RE matches at the beginning of the string.
- search():Scan through a string, looking for any location where this RE matches.
- findall():Find all substrings where the RE matches, and returns them as a list.
- finditer():Find all substrings where the RE matches, and returns them as an iterator.
"""

print("----------------Pattern Match Using: Match-------------------")
match = pattern.match("hello world")
print("Match Output: ",match)


#If a match is found, a Match object is returned, containing information about
# the match: where it starts and ends, the substring it matched,
print("Match Span:",match.span())
print("Match Start:",match.start())
print("Match End:",match.end())
print(pattern.match("say hello", pos=4))
print("Trying to match a part of the string:", pattern.match("say hello", pos=4) is None)
print(pattern.match("say hello", pos=5))
print("Trying to match a part of the string:", pattern.match("say hello", pos=5) is None)

#A match is checked only at the beginning (by default).
#Checking starts from pos index of the string. (default is 0)
print(pattern.match("hello", endpos=4) is None)

print("----------------Pattern Match Using: Search-------------------")
#Search: A match is checked throughtout the string.#Same behaviour of pos and endpos as the match() function.
#- match checks for a match only at the beginning of the string, while search checks
# for a match anywhere in the string

Substring = 'string'
String = '''Lets learn Regular Expressions through re package  
         regex is very useful for string matching. 
          string is fast too.'''

print("Matching Substring using Match:",re.match(Substring, String, re.IGNORECASE)) # Only at the beginning
print("Matching Substring using Search:",re.search(Substring, String, re.IGNORECASE)) # Anywhere in the string but only the first match

target = "Price: $189.90"
expression = "Price: \$189\.900"
print(re.search(expression, target)) # Finds None

target = "Price: $183.90, $89.90, $894.90, $189.90, $1894.90"
expression = "\$189\.90"
result = re.search(expression, target)

print("Returned Match Object:", result) # Finds one match
print("Group 0 in Match Object", result.group(0))
#print(result.group(1)) # Error IndexError: no such group

target1 = "Price: $183.90, $89.90, $894.90, $189.90, $1894.90"
expression1 = "\$(189\.90)"
result1 = re.search(expression1, target1)

print("Returned Match Object:", result1) # Finds one match
print("Group in Match Object", result1.group())
print("Group 0 in Match Object", result1.group(0)) # Group 0 matches with entire expression
print("Group 1 in Match Object", result1.group(1)) # Group 1 matches with first thing in brackets


print("--------------Finding Overlapping Matches:findall-----------------")
#Note:  match(), search() and finditer() return Match object(s) where as findall() returns a list of strings.
#In a module level function, you can simply pass a string as your regex pattern
print("Module Level Match:",re.match("hello", "hello"))
print("Find All Values:",re.findall("hello", "say hello hello"))

#Finds all non-overlapping substrings where the match is found, and returns them as an iterator of the Match objects.
print("-------------Finding Overlapping Matches:finditer-----------------")
matches = pattern.finditer("say hello hello") # expression for compiled pattern is "hello"
for match in matches:
    print(match.span())

#A different style while matching special characters
print("-------Pattern Search for Metacharacters-------")
txt = "This book costs $15."
pattern = re.compile("$15") # $ has special meaning of end of line in Regex
print(pattern.search(txt))
pattern = re.compile("\$15")
print("After Escaping the Sequence:",pattern.search(txt))


print("-------Special meaning of $ in regex-------")
txt = "15"
pattern = re.compile("^15$") # $ has meaning of end of the String and ^ is start of the string in Regex
print(pattern.search(txt))
