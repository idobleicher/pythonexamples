
#Sets are data structures, similar to lists or dictionaries.
# They are created using curly braces, or the set function.
# They share some functionality with lists, such as the use of in to check whether they contain a particular item.

num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
#TRUE
print("spam" not in word_set)
#FALSE # - spam is in word_set

# Sets differ from lists in several ways, but share several list operations such as len.

# They are unordered, which means that they can NOT be indexed.

#They cannot contain duplicate elements.

# Due to the way they're stored, it's faster to check whether an item is part of a set, rather than part of a list.


nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
# Instead of using append to add to a set, use add.
nums.add(-7)
# The method remove removes a specific element from a set;
nums.remove(3)
print(nums)
#{1, 2, 4, 5, 6, -7}

# pop removes an arbitrary element.
nums.pop();
print(nums)
#{2, 4, 5, 6, -7}






