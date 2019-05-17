# An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
# An expression is tested, and if the result comes up false, an exception is raised.
# Assertions are carried out through use of the assert statement.

# Programmers often place assertions at the start of a function
#  to check for valid input, and after a function call to check for valid output.

print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)

# >>>
# 1
# 2
# AssertionError
# >>>