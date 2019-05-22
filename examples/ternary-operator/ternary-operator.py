# Conditional expressions provide the functionality of if statements while  using less code.

# They shouldn't be overused, as they can easily reduce readability, but they' \
#             ' are often useful when assigning variables.

# Conditional expressions are also known as applications of the ternary operator.
#
# The ternary operator is so called because, unlike most operators, it takes three arguments.

a = 7
b = 1 if a >= 5 else 42
print(b)
#1

status  = 1
msg = "Logout" if status == 1 else "Login"
print(msg)
#Logout

