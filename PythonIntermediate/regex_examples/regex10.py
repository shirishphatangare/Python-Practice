#Example:Date Validation (Format: mm/dd/yyyy)
import re;

pattern = '^(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(19|20)\d{2}$'
str_true = ('01/08/2014', '12/30/2014',)
str_false = ('22/08/2014', '-123', '1/8/2014', '1/08/2014', '01/8/2014')

for t in str_true:
    print(t,":",re.match(pattern, t))
for f in str_false:
    print(f,":",re.match(pattern, f))

