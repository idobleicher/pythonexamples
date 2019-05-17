# The contents of a file that has been opened in text
# mode can be read using the read method.

file = open("testfile.txt", "r")
cont = file.read()
print(cont)
file.close()
