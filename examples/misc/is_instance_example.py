#The isinstance() function checks if the object (first argument) is an instance or
# subclass of classinfo class (second argument).
#isinstance(object, classinfo)
#
# object - object to be checked
# classinfo - class, type, or tuple of classes and types

class Foo:
    a = 5


fooInstance = Foo()

print(isinstance(fooInstance, Foo))
#True

print(isinstance(fooInstance, (list, tuple)))
#False

print(isinstance(fooInstance, (list, tuple, Foo)))
#True

# Working of isinstance() with Native Types

numbers = [1, 2, 3]

result = isinstance(numbers, list)
print(numbers,'instance of list?', result)
#[1, 2, 3] instance of list? True

result = isinstance(numbers, dict)
print(numbers,'instance of dict?', result)
#[1, 2, 3] instance of dict? False

result = isinstance(numbers, (dict, list))
print(numbers,'instance of dict or list?', result)
#[1, 2, 3] instance of dict or list? True

number = 5

result = isinstance(number, list)
print(number,'instance of list?', result)
#5 instance of list? False

result = isinstance(number, int)
print(number,'instance of int?', result)
#5 instance of int? True