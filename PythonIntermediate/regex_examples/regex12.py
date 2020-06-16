#Example:Time Validation
import re;

#12-Hour Format
print("--------12-Hour Format-----------")
pattern = r'^(1[012]|[1-9]):[0-5][0-9](\s)?(?i)(am|pm)$'
str_true = ('2:00pm', '7:30 AM', '12:05 am',)
str_false = ('22:00pm', '14:00', '3:12', '03:12pm',)

for t in str_true:
    print(t,":",re.match(pattern, t))
for f in str_false:
    print(f,":",re.match(pattern, f))

#24-Hour Format
print("--------24-Hour Format-----------")
pattern = r'^([0-1]{1}[0-9]{1}|20|21|22|23):[0-5]{1}[0-9]{1}$'
str_true = ('14:00', '00:30',)
str_false = ('22:00pm', '4:00',)

for t in str_true:
    print(t,":",re.match(pattern, t))
for f in str_false:
    print(f,":",re.match(pattern, f))

