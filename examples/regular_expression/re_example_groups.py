#A group can be created by surrounding part of a regular expression with parentheses.
#This means that a group can be given as an argument to metacharacters such as * and ?.

import re

#(spam) represents a group in the example.
pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")