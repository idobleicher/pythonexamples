# Before Python 3.6, you had two main ways of embedding Python expressions inside string literals for formatting: %-formatting and str.format()
#Option #1: %-formatting
#This is has been in the language since the very beginning.

name = "Eric"
print("Hello, %s." % name)
age = 74

out="Hello, %s. You are %s." % (name, age)
print(out)

# once you start using several parameters and longer strings, your code will quickly become much less easily readable
#Unfortunately, this kind of formatting isn’t great because it is verbose and leads to errors,