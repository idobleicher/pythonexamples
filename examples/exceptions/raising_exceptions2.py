try:
    print(1 / 0)
except ZeroDivisionError:
    raise ValueError

# Traceback (most recent call last):
# File "C:/work/devenv/git-views/javaexamples/pythonexamples/examples/exceptions/raising_exceptions2.py",
#  line 2, in <module>
#     print(1 / 0)
# ZeroDivisionError: division by zero
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "C:/work/devenv/git-views/javaexamples/pythonexamples/examples/exceptions/raising_exceptions2.py", line 4, in <module>
#     raise ValueError
# ValueError
