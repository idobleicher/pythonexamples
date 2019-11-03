# The module itertools is a standard library that contains several functions that
# are useful in functional programming.

# One type of function it produces is infinite iterators.

# The function count counts up infinitely from a value.

from itertools import count, cycle , repeat

for i in count(3):
  print(i)
  if i >=5:
    break
  #3
  # 4
  # 5



# The function cycle infinitely iterates through an iterable (for instance a list or string).


for i in  cycle('ABCD'):
    print(i)
    if i == 'C':
        break
#A
#B
#C


# The function repeat repeats an object, either infinitely or a specific number of times.
for i in  repeat(10 , 3):
    print(i)
#
# 10
# 10
# 10