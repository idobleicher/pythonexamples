# Code in a finally statement even runs if an uncaught exception occurs
# in one of the preceding blocks.
try:
    print(1)
    print(10 / 0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("This is executed last")

# 1
# This is executed last
#
# ZeroDivisionError: division by zero
#
# During handling of the above exception, another exception occurred:
# NameError: name 'unknown_var' is not defined
