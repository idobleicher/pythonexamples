import re

pattern = r"spam"
string_to_check= " eggspamsausagespam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")
#No match

# The function re.search finds a match of a pattern anywhere in the string.
if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

#The function re.findall returns a list of all substrings that match a pattern
print(re.findall(pattern, "eggspamsausagespam"))
#['spam', 'spam']

#The function re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list.
