# product(iter1, iter2) :-
# This iterator prints the cartesian product of the two iterable containers passed as arguments.

import itertools

# using product() to print the cartesian product
print ("The cartesian product of the containers is : ")
print (list(itertools.product('AB','12')))

# The cartesian product of the containers is :
# [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]
