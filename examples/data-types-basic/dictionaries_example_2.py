# A useful dictionary method is get.
# It does the same thing as indexing, but if the key is not found in
# the dictionary it returns another specified value instead ('None', by default).

pairs = {1: "apple",
  "orange": [2, 3, 4],
  True: False,
  None: "True",
}

print(pairs.get("orange"))
#[2, 3, 4]

print(pairs.get(7))
#None

print(pairs.get(12345, "not in dictionary"))
#not in dictionary


fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))
# 8 (3+5)

