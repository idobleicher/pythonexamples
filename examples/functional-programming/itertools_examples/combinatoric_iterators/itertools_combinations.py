 #  combinations(iterable, group_size) :-
 #  This iterator prints all the possible combinations(without replacement) of the container passed in arguments
 #  in the specified group size in sorted order.
 #
 #  combinations_with_replacement(iterable, group_size) :-
 #  This iterator prints all the possible combinations(with replacement) of the container passed
 #  in arguments in the specified group size in sorted order.

 # importing "itertools" for iterator operations
import itertools

# using combinations() to print every combination  (without replacement)
print("All the combination of container in sorted order(without replacement) is : ")
print(list(itertools.combinations('1234', 2)))
#All the combination of container in sorted order(without replacement) is :
#[('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4'), ('3', '4')]

#compare to permutations: print(list(itertools.permutations('1234', 2)))
#[('1', '2'), ('1', '3'), ('1', '4'), ('2', '1'), ('2', '3'), ('2', '4'), ('3', '1'), ('3', '2'), ('3', '4'), ('4', '1'), ('4', '2'), ('4', '3')


# using combinations_with_replacement() to print every combination with replacement
print("All the combination of container in sorted order(with replacement) is : ")
print(list(itertools.combinations_with_replacement('1234', 2)))
# [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('2', '2'), ('2', '3'), ('2', '4'), ('3', '3'), ('3', '4'), ('4', '4')]
