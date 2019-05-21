# The next two metacharacters are ^ and $.
# These match the start and end of a string, respectively.

import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
   print("Match 1")
#Match 1

if re.match(pattern, "gray"):
   print("Match 2")
#Match 2

if re.match(pattern, "stingray"):
   print("Match 3")