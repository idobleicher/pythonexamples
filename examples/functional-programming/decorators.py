# Decorators provide a way to modify functions using other functions.
# This is ideal when you need to extend the functionality of functions that you don't want to modify.

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)

decorated()
# ============
# Hello world!
# ============


#We defined a function named decor that has a single parameter func.
# Inside decor, we defined a nested function named wrap.
# The wrap function will print a string, then call func(), and print another string.
# The decor function returns the wrap function as its result.

#We could say that the variable decorated is a decorated version of print_text - it's print_text plus something.

#In fact, if we wrote a useful decorator we might want to replace print_text with the decorated version altogether so we always got
# our "plus something" version of print_text.
#This is done by re-assigning the variable that contains our function:

print_text = decor(print_text)
print_text()


