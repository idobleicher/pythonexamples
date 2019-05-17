x = 365
y = 7
# this is a comment

#Docstrings (documentation strings) serve a similar purpose to comments,
#   as they are designed to explain code.
#  However, they are more specific and have a different syntax.
#  They are created by putting a multiline string containing an
# explanation of the function below the function's first line


# Unlike conventional comments, docstrings are retained
# throughout the runtime of the program.
# This allows the programmer to inspect these comments at run time.

def shout(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")


shout("spam")