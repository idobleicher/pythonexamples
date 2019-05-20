# There are also several combinatoric functions in itertool, such as product and permutation.
from itertools import product, permutations

# These are used when you want to accomplish a task with all possible combinations of some items.
letters = ("A", "B")
print(list(product(letters, range(2))))
# [('A', 0), ('A', 1), ('B', 0), ('B', 1)]


print(list(permutations(letters)))
# [('A', 'B'), ('B', 'A')]

a={1, 2}
result_product=list(product(range(3), a))
print(result_product)
# [(0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2)]

