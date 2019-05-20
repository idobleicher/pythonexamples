# Tuples are very similar to lists, except that they are immutable (they cannot be changed).
# Also, they are created using parentheses, rather than square brackets.

words = ("spam", "eggs", "sausages",)

print(words[0])
# spam

#Trying to reassign a value in a tuple causes a TypeError.
## words[1] = "cheese"
#TypeError: 'tuple' object does not support item assignment

# Like lists and dictionaries, tuples can be nested within each other.


#Tuples can be created without the parentheses, by just separating the values with commas.
my_tuple = "one", "two", "three"
print(my_tuple[0])
#one

# An empty tuple is created using an empty parenthesis pair
tpl = ()

#Tuples are faster than lists, but they cannot be changed.