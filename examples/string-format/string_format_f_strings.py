#https://realpython.com/python-f-strings/

#F string  joined the party in Python 3.6. You can read all about it in PEP 498,
# which was written by Eric V. Smith in August of 2015.

# The syntax is similar to the one you used with str.format() but less verbose.

name = "Eric"
age = 74
msg=f"Hello, {name}. You are {age}."
print(msg)

# Arbitrary Expressions
print(f"{2 * 37}")

def to_lowercase(input):
    return input.lower()

name = "Eric Idle"
print(f"{to_lowercase(name)} is funny.")
# eric idle is funny.

# You also have the option of calling a method directly:
print(f"{name.lower()} is funny.")

# You could even use objects created from classes with f-strings. Imagine you had the following class:

class Comedian:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}.1"

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"


new_comedian = Comedian("Eric", "Idle", "74")

print(f"{new_comedian}")
# 'Eric Idle is 74.1'

# The    __str__() and __repr__()    methods    deal
#  with how objects are presented as strings, so you’ll need to make sure you include
#  at least one of those methods in your class definition.
#  If you have to pick one, go with __repr__() because it can be used in place of __str__().

# The string returned by __str__() is the informal string representation of an object and should be readable.
# The string returned by __repr__() is the official representation and should be unambiguous.
# Calling str() and repr() is preferable to using __str__() and __repr__() directly.

# By default, f-strings will use __str__(),
# but you can make sure they use __repr__() if you include the conversion flag !r:
print(f"{new_comedian!r}")
#Eric Idle is 74. Surprise!

# Multiline f-strings
#You can have multiline strings:

profession = "comedian"
affiliation = "Monty Python"
message = (
   f"Hi {name}. "
   f"You are a {profession}. "
   f"You were in {affiliation}."
 )

print(message)
#Hi Eric Idle. You are a comedian. You were in Monty Python.

message2 = f"Hi {name}. " \
             f"You are a {profession}. " \
             f"You were in {affiliation}."
print(message2)
#Hi Eric Idle. You are a comedian. You were in Monty Python.

#Speed
#-strings are faster than both %-formatting and str.format().

#Quotation Marks
#You can use various types of quotation marks inside the expressions.
# Just make sure you are not using the same type of quotation mark on the outside of the f-string as you are using in the expression.

#This will work:
print(f'\"{"Eric Idle"}\"')
# "Eric Idle"

#This code will also work:
print(f"\'{'Eric Idle'}\'")
# 'Eric Idle'





