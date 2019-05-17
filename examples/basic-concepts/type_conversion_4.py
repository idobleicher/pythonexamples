# 6. tuple() : This function is used to convert to a tuple.
#
# 7. set() : This function returns the type after converting to set.
#
# 8. list() : This function is used to convert any data type to a list type.
# Python code to demonstrate Type conversion
# using tuple(), set(), list()

# initializing string
s = 'geeks'

# printing string converting to tuple
c = tuple(s)
print ("After converting string to tuple : ",end="")
print (c)

# printing string converting to set
c = set(s)
print ("After converting string to set : ",end="")
print (c)

# printing string converting to list
c = list(s)
print ("After converting string to list : ",end="")
print (c)

# After converting string to tuple : ('g', 'e', 'e', 'k', 's')
# After converting string to set : {'e', 'k', 'g', 's'} - no repeating
# After converting string to list : ['g', 'e', 'e', 'k', 's']

