
class Test(object):
    i = 3


t = Test()
print(t.i )    # "static" variable accessed via instance
#3

t.i = 5 # but if we assign to the instance ...
print(Test.i)  # we have not changed the "static" variable
#3

print(t.i)     # we have overwritten Test.i on t by creating a new attribute t.i
#5

Test.i = 6 # to change the "static" variable we do it by assigning to the class
print(t.i)
#5


print(Test.i)
#6
u = Test()
print(u.i)
#6           # changes to t do not affect new instances of Test

# Namespaces are one honking great idea -- let's do more of those!
print(Test.__dict__)
#{'i': 6, ...}

print(t.__dict__)
#{'i': 5}

print(u.__dict__)
#{}