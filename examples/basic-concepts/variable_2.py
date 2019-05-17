# Trying to reference a variable you haven't assigned to causes an error.
# You can use the del statement to remove a variable,
#  which means the reference from the name to the value is deleted,
# and trying to use the variable causes an error.
#  Deleted variables can be reassigned to later as normal

foo = "a string"
print(foo)
# 'a string'
# bar
# NameError: name 'bar' is not defined
del foo
# foo
# NameError: name 'foo' is not defined

# You can also take the value of the variable from the user input.
foo = input("Enter a number: ")
# Enter a number: 7
print(foo)
# 7

