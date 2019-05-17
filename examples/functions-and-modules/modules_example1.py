# Modules are pieces of code that other people have written to fulfill common tasks.
# The basic way to use a module is to add import module_name at the top of your code,
#  and then using module_name.var to access functions and values with the name var in the module.

import random

for i in range(5):
    value = random.randint(1, 6)
    print(value)

# Trying to import a module that isn't available causes an ImportError.











