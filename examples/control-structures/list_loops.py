# Sometimes, you need to perform code on each item in a list.
# This is called iteration, and it can be accomplished with a while loop and a counter variable

words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
    word = words[counter]
    print(word + "!")
    counter = counter + 1

# hello!
# world!
# spam!
# eggs!

# Iterating through a list using a while loop requires quite a lot of code,
#  so Python provides the for loop as a shortcut that accomplishes the same thing.
# The for loop in Python is like the foreach loop in other languages.

for word in words:
    print(word + "!")

# hello!
# world!
# spam!
# eggs!

# The for loop is commonly used to repeat some code a certain number of times.
#  This is done by combining for loops with range objects.

# You do NOT  need to call list on the range object when it is used in a for loop,
#  because it isn't being indexed, so a list isn't required.
for i in range(5):
    print("hello!")
# hello!
# hello!
# hello!
# hello!
# hello!


for i in range(0, 10, 2):
    print(i)

# 0
# 2
# 4
# 6
# 8
