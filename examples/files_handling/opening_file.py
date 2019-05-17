# You can use Python to read and write the contents of  files.
# Text files.
# files are the easiest to manipulate.
#  Before a file can be edited, it must be opened, using the open function.

# The argument of the open function is the path to the file.
# If the file is in the current working directory of the program, you can specify only its name.
text_filename = "testfile.txt"
binary_filename = "binaryfile.png"

myfile = open(text_filename)

# You can specify the mode used to open a file by applying a second argument to the open function.
# Sending "r" means open in read mode, which is the default.
# Sending "w" means write mode, for rewriting the contents of a file.
# Sending "a" means append mode, for adding new content to the end of the file.
#
# Adding "b" to a mode opens it in binary mode,
# which is used for non-text files (such as image and sound sound files).
# write mode
open(text_filename, "w")

# read mode
open(text_filename, "r")
open(text_filename)

# binary write mode
open(binary_filename, "wb")
