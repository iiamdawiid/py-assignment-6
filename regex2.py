# Other Assignment
import re

with open("regex_test.txt") as names:
    data = names.readlines()

# struggled with this one as well to get it to work properly 
pattern = re.compile('^[A-Z][a-zA-Z]*(?: [A-Z][a-zA-Z]*)*$')

for name in data:
    match = re.match(pattern, name.strip())
    if match:
        print(match.group())
    else:
        print("None")
