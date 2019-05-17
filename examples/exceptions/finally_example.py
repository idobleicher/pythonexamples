
# To ensure some code runs no matter what errors occur, you can use a finally statement.
# The finally statement is placed at the bottom of a try/except statement.
#  Code within a finally statement ALWAYS runs after execution of the code in the try,
#  and possibly in the except, blocks.
try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")

# Hello
# Divided by zero
# This code will run no matter what\


