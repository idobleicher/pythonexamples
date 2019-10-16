import itertools as it

#chain kes any number of iterables as arguments and “chains” them together. For example:
list(it.chain('ABC', 'DEF'))
#['A' 'B' 'C' 'D' 'E' 'F']

list(it.chain([1, 2], [3, 4, 5, 6], [7, 8, 9]))
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

iterables =[ [1, 2], [3, 4, 5, 6], [7, 8, 9]]
print (list(it.chain.from_iterable(iterables)))
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
