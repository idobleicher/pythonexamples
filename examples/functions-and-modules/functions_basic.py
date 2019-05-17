print("Hello world!")
# the comma - separated values inside the parentheses are function arguments.
range(2, 20)

#In addition to using pre-defined functions, you can create your own functions by using the def statement.

def my_func():
   print("spam")
   print("spam")

my_func()

# You must define functions before they are called, in the same way that you must assign variables before using them.
#hello()
#NameError: name 'hello' is not defined

def hello():
    print("Hello world!")