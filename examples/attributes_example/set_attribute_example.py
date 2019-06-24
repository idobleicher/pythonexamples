class Person:
    name = 'Adam'


p = Person()
print('Before modification:', p.name)

# setting name to 'John'
setattr(p, 'name', 'John')

print('After modification:', p.name)

# setting attribute name to None
setattr(p, 'name', None)
print('Name is:', p.name)

# setting an attribute not present
# in Person
setattr(p, 'age', 23)
print('Age is:', p.age)