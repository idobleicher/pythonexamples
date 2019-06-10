#https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-new-yield-from-syntax-in-python-3

def reader():
    """A generator that fakes a read from a file, socket, etc."""
    for i in range(4):
        print ("in reader")
        yield '<< %s' % i

def reader_wrapper(g):
    # Manually iterate over data produced by reader
    for v in g:
        yield v

wrap = reader_wrapper(reader())
for i in wrap:
    print(i)


#alternative:
def reader_wrapper_2(g):
    print("reader wrapper 2")
    yield from g

wrap = reader_wrapper_2(reader())
for i in wrap:
    print(i)