#n Python3, the map function returns an iterator or map object which gets lazily evaluated,
# similar to how the zip function is evaluated


#Iterating Over a Dictionary Using Map and Lambda

dict_a = [
    {'name': 'python', 'points': 10},
    {'name': 'java', 'points': 8}
]

print(list(map(lambda x: x['name'], dict_a)) ) # Output: ['python', 'java']

print(list(map(lambda x: x['points'] * 10, dict_a)) ) # Output: [100, 80]

print(list(map(lambda x: x['name'] == "python", dict_a) )) # Output: [True, False]


#Multiple Iterables to the Map Function
list_a = [1, 2, 3]
list_b = [10, 20, 30]

print(list(map(lambda x, y: x + y, list_a, list_b) )) # Output: [11, 22, 33]
# Output: [11, 22, 33]