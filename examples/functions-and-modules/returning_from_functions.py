def max(x, y):
    if x >= y:
        return x
    else:
        return y


print(max(4, 7))
# 7

z = max(8, 5)
print(z)
# 8


def shortest_string(x, y):
    if len(x) <= len(y):
        return x
    else:
        return y


print(shortest_string("a","bc"))
# a

# Once you return a value from a function, it immediately stops being executed.
#  Any code after the return statement will never happen
def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed") # Unreachable code


print(add_numbers(4, 5))
# 9




