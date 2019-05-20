# Python contains many useful built-in functions and methods to accomplish common tasks.

# join - joins a list of strings with another string as a separator.
print("-".join(["spam", "eggs", "ham"]))
#spam-eggs-ham

# replace - replaces one substring in a string with another.
print("Hello ME".replace("ME", "world"))
#Hello world

# startswith and endswith - determine if there is a substring at the start and end of a string, respectively.
print("This is a sentence.".startswith("This"))
#True
print("This is a sentence.".endswith("sentence."))
# "True"

# To change the case of a string, you can use lower and upper.
print("This is a sentence.".upper())
#"THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#"an all caps sentence"


# The method split is the opposite of join, turning a string with a certain separator into a list.
print("spam, eggs, ham".split(", "))
#"['spam', 'eggs', 'ham']"