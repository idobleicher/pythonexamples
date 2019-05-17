i = 1
while i <=5:
    print(i)
    i = i + 1
print("Finished!")

# Infinite loop: while 1==1:

# Break and continue

i = 0
while True:
    i = i + 1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking")
        break
    print(i)

print("Finished")
# 1
#  Skipping 2
# 3
# 4
# Breaking
# Finished

