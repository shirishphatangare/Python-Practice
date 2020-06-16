#Example:Check for a Positive Numbers
import re;

print("-------Positive Values---------")
#Positive Values
pattern = '^\d+$'
str_true = ('123', '1',)
str_false = ('abc', '1.1',)

for t in str_true:
    print(t,":",re.match(pattern, t))
for f in str_false:
    print(f,":",re.match(pattern, f))

print("-------Negative Values---------")
#Negative Values
pattern = '^-\d+$'
str_true = ('-123', '-1',)
str_false = ('123', '-abc', '-1.1',)

for t in str_true:
    print(t,":",re.match(pattern, t))
for f in str_false:
    print(f,":",re.match(pattern, f))

print("-------Integer Check---------")
#Integers
pattern = '^-{0,1}\d+$'
str_true = ('-123', '-1', '1', '123',)
str_false = ('123.0', '-abc', '-1.1',)

for t in str_true:
    print(t,":",re.match(pattern, t))
for f in str_false:
    print(f,":",re.match(pattern, f))