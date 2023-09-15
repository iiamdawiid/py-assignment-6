# In-Class Exercise 3 
# Print each persons name and twitter handle, using groups, should look like:

# ===================
# Full Name / Twitter
# ===================

# Derek Hawkins / @derekhawkins
# Erik Sven-Osterberg / @sverik

# Ryan Butz / @ryanbutz

# Example Exampleson / @example

# Ripal Pael / @ripalp

# Darth Vader / @darthvader
import re

print("===================\nFull Name / Twitter\n===================")

with open("names.txt") as file:
    data = file.readlines()
    
pattern = re.compile("([A-Z][a-z]+), ([\w -]*)([A-Z][a-z]+).*\s(@[a-zA-Z0-9]+$)")

for info in data:
    match = pattern.search(info)

    if match:
        print('\n', f"{match.group(3)} {match.group(2)}{match.group(1)} / {match.group(4)}")