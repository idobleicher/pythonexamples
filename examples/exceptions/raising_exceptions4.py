# In except blocks, the raise statement can be used without arguments
#  to re-raise whatever exception occurred.

try:
    num = 5 / 0
except:
    print("An error occurred!")
    raise

# An error occurred!

# Traceback (most recent call last):
#   File "C:/work/devenv/git-views/javaexamples/pythonexamples/examples/exceptions/raising_exceptions4.py", line 4, in <module>
#     num = 5 / 0
# ZeroDivisionError: division by zero



