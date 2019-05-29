#The getattr() method returns the value of the named attribute of an object.
# If not found, it returns the default value provided to the function.

# The syntax of getattr() method is:
#
# getattr(object, name[, default])
# The above syntax is equivalent to:
#
# object.name

# #getattr() Parameters
# The getattr() method takes multiple parameters:
#
# object - object whose named attribute's value is to be returned

# name - string that contains the attribute's name

# default (Optional) - value that is returned when the named attribute is not found


# Return value from getattr()
# The getattr() method returns:
#
# value of the named attribute of the given object
# default, if no named attribute is found

# AttributeError exception, if named attribute is not found AND default is not defined

#Example 1: How getattr() works in Python?
class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)
#The age is: 23
#The age is: 23

#Example 2: getattr() when named attribute is not found
class Person:
    age = 23
    name = "Adam"

person = Person()

# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))
#The sex is: Male

# when no default value is provided
#print('The sex is:', getattr(person, 'sex'))
#AttributeError
