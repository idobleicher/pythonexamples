# Named parameters to a function can be made optional by giving them a default value.
# These must come after named parameters without a default value.
#
# In case the argument is passed in, the default value is ignored.
# If the argument is not passed in, the default value is used.

def function(x, y, food="spam"):
   print(food)

function(1, 2)
function(3, 4, "egg")

# out:
# spam
# egg
