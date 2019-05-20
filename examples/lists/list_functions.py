nums = [1, 2, 3]
# append- adds an item to the end of an existing list.
nums.append(4)
print(nums)
# [1, 2, 3, 4]

# o get the number of items in a
#  list, you can use the len function.

nums = [1, 3, 5, 2, 4]
print(len(nums))
#5

letters = ["a", "b", "c"]
letters.append("d")
print(len(letters))
# 4

#The insert method is similar to append, except that it allows you to insert
#  a new item at any position in the list, as opposed to just at the end.
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)
# ['Python', 'is', 'fun']

#The index method finds the first occurrence of a list item and returns its index.
#If the item isn't in the list, it raises a ValueError.

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
#2
print(letters.index('p'))
#0
#print(letters.index('z'))
#ValueError: 'z' is not in list
