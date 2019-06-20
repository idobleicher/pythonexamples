#Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of frozen set remains the same after creation.

#Due to this, frozen sets can be used as key in Dictionary or as element of another set.
# But like sets, it is not ordered (the elements can be set at any index).

#The syntax of frozenset() method is:

#frozenset([iterable])

#frozenset() Parameters
#The frozenset() method optionally takes a single parameter:
#iterable (Optional) - the iterable which contains elements to initialize the frozenset with.
#Iterable can be set, dictionary, tuple, etc.

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)

fSet |= set('xxx')
print('The frozen set is:', fSet)

print("-----------------")
print('The empty frozen set is:', frozenset())

print("-----------------")
#Error - fSet.pop()

# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)




