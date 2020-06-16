#Example:Checking for a valid user name that has a certain minimum and maximum length.
#Allowed characters: letters (upper-case and lower-case), numbers, dashes, underscores
import re;

min_len = 5  # minimum length for a valid username
max_len = 15  # maximum length for a valid username

pattern = r"^(?i)[a-z0-9_-]{%s,%s}$" % (min_len, max_len)

# remove `(?i)` to only allow lower-case letters

str_true = ('user123', '123_user', 'Username')
str_false = ('user', 'username1234_is-way-too-long', 'user$34354')

for t in str_true:
    print(t,":",re.match(pattern, t))
for f in str_false:
    print(f,":",re.match(pattern, f))