# The filter() method constructs an iterator from elements of an iterable for which a function returns true.
#
#
# simple words, the filter() method filters the given iterable with the help of a function that tests each element in the iterable to be true or not.
#The syntax of filter() method is:

# filter(function, iterable)
# filter() Parameters
# The filter() method takes two parameters:
#
# function - function that tests if elements of an iterable returns true or false
# If None, the function defaults to Identity function - which returns false if any elements are false

# iterable - iterable which is to be filtered, could be sets, lists, tuples, or containers of any iterators

# Return value from filter()
# The filter() method returns an !! iterator  !!that passed the function check for each element in the iterable.
#
# The filter() method is equivalent to:
#
# # when function is defined
# (element for element in iterable if function(element))
#
# # when function is None
# (element for element in iterable if element)

# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)

#Since, iterator doesn't store the values itself, we loop through it and print out vowels one by one.
#
# a
# e
# i
# o


# How filter() method works without the filter function?
# random list
#list of number, string and boolean in randomList.
randomList = [1, 'a', 0, False, True, '0']

#ith filter function as None, the function defaults to Identity function,
# and each element in randomList is checked if it's true or not.

filteredList = filter(None, randomList)

# When we loop through the final filteredList, we get the elements which are true: 1, a, True and '0' ('0' as a string is also true).
print('The filtered elements are:')
for element in filteredList:
    print(element)

    # The filtered elements are:
    # 1
    # a
    # True
    # 0
