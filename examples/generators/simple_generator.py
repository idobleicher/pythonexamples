def simple_generator_function():
    yield 1
    yield 2
    yield 3



for value in simple_generator_function():
    print(value)
# 1
# 2
# 3

for value in simple_generator_function():
    print("again" , value)

# again 1
# again 2
# again 3

print ("-----------")
our_generator = simple_generator_function()
print(next(our_generator))
#  1

print(next(our_generator))
#  2

print(next(our_generator))
#  3


print ("-----------")
for value in our_generator:
    print(value)
#WILL NOT PRINT


#next(our_generator)
#will cause StopIteration
