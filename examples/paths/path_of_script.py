import os
import sys

#The __file__ variable contains the path to the file that Python is currently importing.
# You can use this variable inside a module to find the path of the module

print (os.path.dirname(os.path.abspath( __file__ )))


print( os.path.dirname(os.path.realpath(__file__)))

# this will not work if you happen to call your script from another script. I’:
print (os.path.dirname(sys.argv[0]))

#The solution  for the executables  created with py2exe

print (os.path.abspath(os.path.dirname(sys.argv[0])))

