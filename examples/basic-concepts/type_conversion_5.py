# 9. dict() : This function is used to convert a tuple of order (key,value) into a dictionary.
# 10. str() : Used to convert integer into a string.
# 11. complex(real,imag) : : This function converts real numbers to complex(real,imag) number.
#

# Python code to demonstrate Type conversion
# using dict(), complex(), str()

# initializing integers
a = 1
b = 2

# initializing tuple
tup = (('a', 1), ('f', 2), ('g', 3))

# printing tuple converting to expression dictionary
c = dict(tup)
print ("After converting tuple to dictionary : ", end="")
print (c)

# printing integer converting to complex number
c = complex(1,2)
print ("After converting integer to complex number : ", end="")
print (c)

# printing integer converting to string
c = str(a)
print ("After converting integer to string : ", end="")
print (c)

# Out:After converting tuple to dictionary : {'a': 1, 'f': 2, 'g': 3}
# After converting integer to complex number : (1+2j)
# After converting integer to string : 1
