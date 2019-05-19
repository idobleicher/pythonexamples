# To write to files you use the write method, which writes a string to the file
# The "w" mode will create a file, if it does not already exist.

filename="newfile.txt"
file = open(filename, "w")
file.write("This has been written to a file")
file.close()

file = open(filename, "r")
print("--- File content:")
print(file.read())
file.close()