# Let's create a dictionary, the functional way

# Create your dictionary class
class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value

    # Main Function


dict_obj = my_dictionary()

dict_obj.add(1, 'Geeks')
dict_obj.add(2, 'forGeeks')

print(dict_obj)
#{1: 'Geeks', 2: 'forGeeks'}



#Method #1: Using Subscript notation

# This method will create a new key\value pair on a dictionary by assigning a value to that key.
# If the key doesn’t exist, it will be added and will point to that value.
# If the key exists, the current value it points to will be overwritten.
dict = {'key1': 'geeks', 'key2': 'fill_me'}
print("Current Dict is: ", dict)

# using the subscript notation
# Dictionary_Name[New_Key_Name] = New_Key_Value
dict['key2'] = 'for'
dict['key3'] = 'geeks'
print("Updated Dict is: ", dict)
# Current Dict is:  {'key1': 'geeks', 'key2': 'fill_me'}
# Updated Dict is:  {'key3': 'geeks', 'key1': 'geeks', 'key2': 'for'}


# Method #2: Using update() method
#
# When we have to update/add a lots of key/value to dictionary, update() method is suitable.
dict = {'key1':'geeks', 'key2':'for'}
print("Current Dict is: ", dict)

# adding key3
dict.update({'key3':'geeks'})
print("Updated Dict is: ", dict)

# adding dict1 (key4 and key5) to dict
dict1 = {'key4':'is', 'key5':'fabulous'}
dict.update(dict1)
print(dict)

# by assigning
dict.update(newkey1 ='portal')
print(dict)
# Current Dict is:  {'key2': 'for', 'key1': 'geeks'}
# Updated Dict is:  {'key2': 'for', 'key3': 'geeks', 'key1': 'geeks'}
#
# {'key4': 'is', 'key2': 'for', 'key5': 'fabulous', 'key3': 'geeks', 'key1': 'geeks'}
#
# {'key3': 'geeks', 'newkey1': 'portal', 'key1': 'geeks',
#         'key4': 'is', 'key2': 'for', 'key5': 'fabulous'}




#Method #3: __setitem__ method to add a key-value pair to a dict

#Using __setitem__ method should be avoided because of its poor performance(computationally inefficient).
dict = {'key1': 'geeks', 'key2': 'for'}

# using __setitem__ method
dict.__setitem__('newkey2', 'GEEK')
print(dict)


# Method #4: Using * operator
#
# Using this method we can merge old dictionary and new key/value pair in another dictionary.
dict = {'a': 1, 'b': 2}

# will create a new dictionary
new_dict = {**dict, **{'c': 3}}

print(dict)
print(new_dict)
# {'b': 2, 'a': 1}
# {'b': 2, 'c': 3, 'a': 1}







