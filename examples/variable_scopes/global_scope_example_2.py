#f a variable with same name is defined inside the scope of function as well then it will print the value given inside
# the function only and not the global value.

# This function has a variable with
# name same as s.
def f():
	s = "Me too."
	print (s)

# Global scope
s = "I love Geeksforgeeks"
f()
print (s)

#Me too.
#I love Geeksforgeeks
