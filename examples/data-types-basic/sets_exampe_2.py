#Sets can be combined using mathematical operations.

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

# The union operator | combines two sets to form a new one containing items in either.
print(first | second)
#{1, 2, 3, 4, 5, 6, 7, 8, 9}

# The intersection operator & gets items only in both.
print(first & second)
#{4, 5, 6}

# The difference operator - gets items in the first set but not in the second.
print(first - second)
# {1, 2, 3}
print(second - first)
# {8, 9, 7}

# The symmetric difference operator ^ gets items in either set, but not both.
print(first ^ second)
#{1, 2, 3, 7, 8, 9}
