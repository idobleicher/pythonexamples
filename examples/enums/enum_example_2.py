# Python code to demonstrate enumerations

# importing enum for enumerations
import enum

# creating enumerations using class
class Animal(enum.Enum):
	dog = 1
	cat = 2
	lion = 3

# printing enum member as string
print ("The string representation of enum member is : ",end="")
print (Animal.dog)
#The string representation of enum member is : Animal.dog

# printing enum member as repr
print ("The repr representation of enum member is : ",end="")
print (repr(Animal.dog))
#The repr representation of enum member is : <Animal.dog: 1>

# printing the type of enum member using type()
print ("The type of enum member is : ",end ="")
print (type(Animal.dog))
#The type of enum member is : <enum 'Animal'>

# printing name of enum member using "name" keyword
print ("The name of enum member is : ",end ="")
print (Animal.dog.name)
#The name of enum member is : dog

# Enumerations are iterable. They can be iterated using loops

#. Enumerations support hashing. Enums can be used in dictionaries or sets.



print("------------------")
# printing all enum members using loop
print("All the enum values are : ")
for Anim in (Animal):
    print(Anim)

# Hashing enum member as dictionary
di = {}
di[Animal.dog] = 'bark'
di[Animal.lion] = 'roar'

# checking if enum values are hashed successfully
if di == {Animal.dog: 'bark', Animal.lion: 'roar'}:
    print("Enum is hashed")
else:
    print("Enum is not hashed")



 #Accessing Modes : Enum members can be accessed by two ways
#
# 1. By value :- In this method, the value of enum member is passed.
#
# 2. By name :- In this method, the name of enum member is passed.


# Accessing enum member using value
print("The enum member associated with value 2 is : ", end="")
print(Animal(2))
#The enum member associated with value 2 is : Animal.cat

# Accessing enum member using name
print("The enum member associated with name lion is : ", end="")
print(Animal['lion'])
#The enum member associated with name lion is : Animal.lion

# Assigning enum member
mem = Animal.dog

# Displaying value
print("The value associated with dog is : ", end="")
print(mem.value)
#The value associated with dog is : 1

# Displaying name
print("The name associated with dog is : ", end="")
#The name associated with dog is : dog
print(mem.name)


# Comparison : Enumerations supports two types of comparisons
#
# 1. Identity :- These are checked using keywords “is” and “is not“.
#
# 2. Equality :- Equality comparisons of “==” and “!=” types are also supported.

# Comparison using "is"
if Animal.dog is Animal.cat:
    print("Dog and cat are same animals")
else:
    print("Dog and cat are different animals")

#Dog and cat are different animals

# Comparison using "!="
if Animal.lion != Animal.cat:
    print("Lions and cat are different")
else:
    print("Lions and cat are same")


# #Seperate value or name can also be accessed using “name” or “value” keyword.
# Comparison : Enumerations supports two types of comparisons
#
# 1. Identity :- These are checked using keywords “is” and “is not“.
#
# 2. Equality :- Equality comparisons of “==” and “!=” types are also supported.
