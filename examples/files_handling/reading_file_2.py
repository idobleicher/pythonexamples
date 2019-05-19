# To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file.

text_filename = "testfile.txt"
file = open(text_filename, "r")
content = file.readlines()
print(len(content))
print(content)
file.close()



# You can also use a for loop to iterate through the lines in the file:
file = open(text_filename, "r")

for line in file:
    print(line)

file.close()


# In the output, the lines are separated by blank lines, as
# the print function automatically adds a new line at the end of its output.