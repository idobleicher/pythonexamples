
#The None object is used to represent the absence of a value.
#It is similar to null in other programming languages.
#Like other "empty" values, such as 0, [] and the empty string, it is False when converted to a Boolean variable.
#When entered at the Python console, it is displayed as the empty string.

print (None == None)
#True

print(None)
# None


# The None object is returned by any function that doesn't explicitly return anything else.
def some_func():
  print("Hi!")

var = some_func()
print(var)
#None