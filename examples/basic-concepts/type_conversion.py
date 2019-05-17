

# In Python, it's impossible to complete certain operations due
# to the types involved.
#
# For instance, you can't add two strings containing the numbers 2 and 3 together
#  to produce the integer 5, as the operation will be performed
# on strings, making the result '23'.

# The solution to this is type conversion.
# In that example, you would use the int function.

print("2" + "3")
# '23'

print (int("2") + int("3"))
# 5

# Another example of type conversion is turning user input (which is a string) to
# numbers (integers or floats), to allow for the performance of calculations.

result = float(input("Enter a number: ")) + float(input("Enter another number: "))
# Enter a number: 40
# Enter another number: 2

print(result)
#42.00
# Passing non-integer or float values ("x") will cause an error
# ValueError: could not convert string to float: 's'
