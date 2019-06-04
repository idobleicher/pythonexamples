#Caching
#https://pymotw.com/3/functools/

#The lru_cache() decorator wraps a function in a least-recently-used cache.
# Arguments to the function are used to build a hash key, which is then mapped to the result.
# Subsequent calls with the same arguments will fetch the value from the cache instead of calling the function.
# The decorator also adds methods to the function to examine the state of the cache (cache_info()) and empty the cache (cache_clear()
import functools


@functools.lru_cache()
def expensive(a, b):
    print('expensive({}, {})'.format(a, b))
    return a * b


MAX = 2

print('First set of calls:')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)


#First set of calls:
# expensive(0, 0)
# expensive(0, 1)
# expensive(1, 0)
# expensive(1, 1)

print(expensive.cache_info())

# CacheInfo(hits=0, misses=4, maxsize=128, currsize=4)



print('\nSecond set of calls:')
for i in range(MAX + 1):
    for j in range(MAX + 1):
        expensive(i, j)

#Second set of calls:
# expensive(0, 2)
# expensive(1, 2)
# expensive(2, 0)
# expensive(2, 1)
# expensive(2, 2)

print(expensive.cache_info())
#CacheInfo(hits=4, misses=9, maxsize=128, currsize=9)



print('\nClearing cache:')
expensive.cache_clear()
print(expensive.cache_info())

#Clearing cache:
#CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)

print('\nThird set of calls:')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
 #Third set of calls:
# expensive(0, 0)
# expensive(0, 1)
# expensive(1, 0)
# expensive(1, 1)


print(expensive.cache_info())
#CacheInfo(hits=0, misses=4, maxsize=128, currsize=4)
