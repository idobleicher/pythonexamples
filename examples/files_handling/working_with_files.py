#It is good practice to avoid wasting resources by making sure that files are always closed after they
# have been used. One way of doing this is to use try and finally.

#This ensures that the file is always closed, even if an error occurs.

text_filename = "testfile.txt"
try:
    f = open(text_filename)
    print(f.read())
finally:
    f.close()

#An alternative way of doing this is using with statements.
# This creates a temporary variable (often called f), which is only accessible
# in the indented block of the with statement.

with open(text_filename) as f:
    print(f.read())


    ##Try /except/with
    try:
        with open("test.txt") as f:
            print(f.read())
    except:
        print("Error")