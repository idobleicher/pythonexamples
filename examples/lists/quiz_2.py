list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])
# list [5]
# 8

for i in range(10):
    if not i % 2 == 0:
        # i is odd
        print(i+1)
# 2
# 4
# 6
# 8
# 10

while False:
    print("Looping...")
    #Will not run

list = [1,2,3,4]
if len(list) % 2 == 0 :
    print(list[0])
# 1

letters = ['x', 'y', 'z']
letters.insert(1, 'w')
print(letters)
#['x', 'w', 'y', 'z']
print(letters[2])
# y

list = [1, 2, 3]
for var in list:
    print(var)
    # 1
    # 2
    # 3

