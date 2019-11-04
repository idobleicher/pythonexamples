import itertools

# repeat(val, num) :- This iterator repeatedly prints the passed value infinite number of times.
# If num. is mentioned, them till that number.


# using repeat() to repeatedly print number
print("Printing the numbers repeatedly : ")
print(list(itertools.repeat(25, 4)))
# [25, 25, 25, 25]
