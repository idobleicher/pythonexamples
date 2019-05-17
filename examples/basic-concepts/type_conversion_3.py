# 3. ord() : This function is used to convert a character to integer.
#
# 4. hex() : This function is to convert integer to hexadecimal string.
#
# 5. oct() : This function is to convert integer to octal string

# Python code to demonstrate Type conversion
# using  ord(), hex(), oct()

# initializing integer
s = '4'

# printing character converting to integer
c = ord(s)
print("After converting character to integer : ", end="")
print(c)

# printing integer converting to hexadecimal string
c = hex(56)
print("After converting 56 to hexadecimal string : ", end="")
print(c)

# printing integer converting to octal string
c = oct(56)
print("After converting 56 to octal string : ", end="")
print(c)

# Out:
# After converting character to integer : 52
# After converting 56 to hexadecimal string : 0x38
# After converting 56 to octal string : 0o70
#
