

#The write method returns the number of bytes written to a file, if successful
filename="newfile3.txt"
msg = "Hello world!"
file = open(filename, "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

