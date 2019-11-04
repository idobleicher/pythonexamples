# count(start, step) :- This iterator starts printing from the “start” number and prints infinitely.
# If steps are mentioned, the numbers are skipped else step is 1 by default.

from itertools import count

for i in count(5,2):
    if i > 20:
        break
    else:
        print(i)
# #5
# 7
# 9
# 11
# 13
# 15
# 17
# 19

