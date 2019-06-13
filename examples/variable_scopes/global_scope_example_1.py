
# This function uses global variable s
#Global variables are the one that are defined and declared outside a function and we need to use them inside a function
def f():
	print (s)

# Global scope
s = "I love Geeksforgeeks"
f()
