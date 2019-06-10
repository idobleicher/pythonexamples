#Example 2: How iter() works for custom objects?

class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

printNum = PrintNumber(3)

printNumIter = iter(printNum)

# prints '1'
print(next(printNumIter))

# prints '2'
print(next(printNumIter))

# prints '3'
print(next(printNumIter))

# raises StopIteration
##print(next(printNumIter))

#1
# 2
# 3
# StopIteration