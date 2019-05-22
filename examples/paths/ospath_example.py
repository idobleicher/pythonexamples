
import os

path = "/baz/foo"
print(os.path.basename(path))
#foo

print(os.path.dirname(path))
#/baz

#isabs- It specifies whether the path is absolute or not.
# In Unix system absolute path means path begins with the slash(‘/’)
print(os.path.isabs(path) )
#True


#4. os.path.isdir(path) : This function specifies whether the path is existing directory or not
print(os.path.isdir(path) )
#false

# os.path.normcase(path) : This function normalizes the case of the pathname specified.n Unix and Mac OS X system it returns the pathname as it is

# os.path.normpath(path) : This function normalizes the path names by collapsing redundant separators and up-level references so that A//B, A/B/, A/./B and A/foo/../B all become A/B

print(os.path.normpath("foo/./bar") )
#/foo/bar


print (os.path.join('home', 'foo', 'work'))
# home/foo/work

#The method getcwd() returns current working directory of a process.
print (os.getcwd())
#/home/danny/projects/personal/pythonexamples/examples/paths


# os.path.abspath(path)-Return a normalized absolutized version of the pathname path
#On most platforms, this is equivalent to calling the function normpath() as follows: normpath(join(os.getcwd(), path)).
print (os.path.abspath('x'))
#/home/danny/projects/personal/pythonexamples/examples/paths/x

print (os.path.abspath('y'))
#urn the canonical path of the specified filename, eliminating any symbolic links encountered in the path (
#/home/danny/projects/personal/pythonexamples/examples/paths/y