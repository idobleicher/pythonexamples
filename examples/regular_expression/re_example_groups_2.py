# There are several kinds of special groups.
# Two useful ones are named groups and non-capturing groups.
# Named groups have the format (?P<name>...), where name is the name of the group, and ... # is the content.
# They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.

# Non-capturing groups have the format (?:...).
# They are not accessible by the group method, so they can be added to an existing regular expression without breaking the numbering.
import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   #abc

   print(match.groups())
  # ('abc', 'ghi')


pattern = r"(a)(b(?:c)(d)(?:e))?"
match = re.match(pattern, "abcdefghi")
if match:
   print(len(match.groups()))
   #3


