# Operator precedence is a very important concept in programming.
#  It is an extension of the mathematical idea of order of operations
# (multiplication being performed before addition, etc.)
#  to include other operators, such as those in Boolean logic.

# The below code shows that == has a higher precedence than or:

print(False == False or True)
# True! FALSE == FALSE (true) and then or

print(False == (False or True))
# False - False or True (true)  and then the ==

print((False == False) or True)
# True - FALSE==FALSE (true) and then or

print (1 + 1 * 3 == 6)
# False

y = 2
x = 4
print(not 1 + 1 == y or x == 4 and 7 == 8)
# False









