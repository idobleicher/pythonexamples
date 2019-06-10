#he Sentinel Object pattern is a standard Pythonic approach that’s used both in the Standard Library and beyond.
# The pattern most often uses Python’s built-in None object, but in situations where None might be a useful value,
# a unique sentinel object() can be used instead to indicate missing or unspecified data.

a="abc"
b="xx"
def find_index(instr ,inindex ):
    try:
        i = instr.index(inindex)
        return i
    except:
        return

    # versus
def find_index_2(instr ,inindex ):
     i = instr.find(inindex)
     if i == -1:
        return

print(find_index (a , b))
print(find_index_2 (a , b))


#sentinel = object()  # unique object used to signal cache misses
# result = cache_get(key, sentinel)
# if result is not sentinel: