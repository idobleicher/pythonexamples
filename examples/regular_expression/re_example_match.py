import re

#The  example checks if the pattern "spam" matches the string and prints "Match" if it does.
#match function can be used to determine whether it matches at the beginning of a string.

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
   print("Match")
else:
   print("No match")

# Match