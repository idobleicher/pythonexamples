#
# Most Python code is either a module to be imported, or a script that does something.
# However, sometimes it is useful to make a file that can be both imported as a module and run as a script.
# To do this, place script code inside if __name__ == "__main__".
# This ensures that it won't be run if the file is imported.

def function():
   print("This is a module function")

if __name__=="__main__":
   print("This is a script")

#When the Python interpreter reads a source file, it executes all of the code it finds in the file. Before executing the code, it defines a few special variables.
#For example, if the Python interpreter is running that module (the source file) as the main program,
# it sets the special __name__ variable to have a value "__main__".
# If this file is being imported from another module, __name__ will be set to the module's name.