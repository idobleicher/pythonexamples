
nums = [1, 2, 3, 4]
res_dict = { 1: "a" , 2: "b" ,3: "b" , 4: "c"}
expected = [ "a" , "b" , "c"]

assert ( 1 in nums)
assert (not  5 in nums)
assert (5  not in nums)


assert all( res_dict[num] in expected for num in nums)