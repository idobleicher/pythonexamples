from functools import reduce

def compose(f, g):
    return lambda x: g(f(x))

def identity(x):
    return x

def pipe(*functions):
    """
    'pipes' the argument through the functions

    Example:
        >>> pipeline = pipe(sum, range, list)
        >>> pipeline([1, 2, 3])
        [0, 1, 2, 3, 4, 5]
        >>> pipeline = pipe(sum, range, len)
        >>> pipeline([1, 2, 3])
        6

    :param functions: functions to thread through
    :return: output of final function
    """

    return reduce(compose, functions, identity)
list1 = [1, 2, 3]

pipeline1 = pipe(sum, range, list)

print(pipeline1(list1))
#[0, 1, 2, 3, 4, 5]
print(list(range(sum(list1))))
#[0, 1, 2, 3, 4, 5]

#--------------------
pipeline2 = pipe(sum, range, len)
print(pipeline2(list1))
#6
print(len(range(sum(list1))))
#6