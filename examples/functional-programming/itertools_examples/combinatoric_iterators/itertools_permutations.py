# . permutations(iter, group_size) :-
# This iterator prints all possible permutation of all elements of iterable.
# The size of each permuted group is decided by group_size argument.

import itertools

# using permutations to compute all possible permutations
print ("All the permutations of the given container is : ")
print (list(itertools.permutations('GfG',2)))

# All the permutations of the given container is :
# [('G', 'f'), ('G', 'G'), ('f', 'G'), ('f', 'G'), ('G', 'G'), ('G', 'f')]
