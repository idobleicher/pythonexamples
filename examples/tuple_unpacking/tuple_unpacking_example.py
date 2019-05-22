#Tuple unpacking allows you to assign each item in an iterable (often a tuple) to a variable.

numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

# 1
# 2
# 3
print("-------------------")
#This can be also used to swap variables by doing a, b = b, a ,
# since b, a on the right hand side forms the tuple (b, a) which is then unpacked.
x = 1
y =2

x ,y = [y , x]
print(x)
print(y)
#2
#1

print("-------------------")
#A variable that is prefaced with an asterisk (*) takes all values from the iterable that
# are left over from the other variables.
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

# 1
# 2
# [3, 4, 5, 6, 7, 8]
# 9

a, b, c, d, *e, f, g = range(20) #0-19
print(len(e))
#14 =20-6
