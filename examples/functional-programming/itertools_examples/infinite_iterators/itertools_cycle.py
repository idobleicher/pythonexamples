#cycle(iterable) :-
# This iterator prints all values in order from the passed container.
# It restarts printing from beginning again when all elements are printed in a cyclic manner.

from itertools import  cycle

count = 0
for i in cycle([1,2,3,4]) :
    count += 1
    if count > 20:
        break
    else:
        print(i)

#1
# 2
# 3
# 4
# 1
# 2
# 3
# 4
# 1
# 2
# 3
# 4
# 1
# 2
# 3
# 4
# 1
# 2
# 3
# 4