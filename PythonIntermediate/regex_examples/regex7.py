#Example:Checking for valid email addresses
import re;

pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
str_true = ('test@mail.com',)
str_false = ('testmail.com', '@testmail.com', 'test@mailcom')

for t in str_true:
    print(t,":",re.match(pattern, t))
for f in str_false:
    print(f,":",re.match(pattern, f))