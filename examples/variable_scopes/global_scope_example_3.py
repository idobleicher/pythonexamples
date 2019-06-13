#We only need to use global keyword in a function if we want to do
# assignments / change them. global is not needed for printing and accessing

#Any variable which is changed or created inside of a function is local, if it hasn’t been declared as a global variable.
#To tell Python, that we want to use the global variable, we have to use the keyword “global”, as can be seen in the following example:



# This function modifies global variable 's'
def f():
	global s
	print (s)
	s = "Look for Geeksforgeeks Python Section"
	print(s)

# Global Scope
s = "Python is great!"
f()
print (s)

#Python is great!
#Look for Geeksforgeeks Python Section
#Look for Geeksforgeeks Python Section
