# Hash Values of Custom Classes

# We have seen before that there are differences between mutable and immutable types in Python.
# Built-in immutable types have always a hash method, while mutable types don't.
# However, this leaves outside custom defined classes.
# By default, all instances of custom classes will have a hash value defined at creation and it will not change over time.
# Two instances of the same class will have two different hash values. For example:


class MyClass:
    def __init__(self, value):
        self.value = value

my_obj = MyClass(1)
print(my_obj.__hash__())
my_new_obj = MyClass(1)
print(my_new_obj.__hash__())


print("---------------------")
# If you run the code above, you will see that the hash value that you get from your objects changes every time.
# This is because the hash is derived from the object's id.

# Python, as expected, allows you to define your own hash value.
# For example, you can alter MyClass like this:

class MyClass2:
    def __init__(self, var):
        self.var = var

    def __hash__(self):
        return int(self.var)

my_obj = MyClass2(1)
my_obj_2 = MyClass2(1)
print(my_obj.__hash__())
print(my_obj_2.__hash__())
var = {my_obj: 'my_obj'}
var[my_obj_2] = 'my_obj_2'
print(var)
#{My Class: 'my_obj', My Class: 'my_obj_2'}
