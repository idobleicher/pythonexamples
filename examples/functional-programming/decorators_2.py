
#Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.
#If we are defining a function we can "decorate" it with the @ symbol like:

#A single function can have multiple decorators.

def my_decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@my_decor
def print_text():
    print("Hello world!")

print_text()

# ============
# Hello world!
# ============


