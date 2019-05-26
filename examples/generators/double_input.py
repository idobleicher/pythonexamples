#send  used to send values into a generator that just yielded.

def double_inputs():
    while True:
        x = yield
        yield x * 2

gen = double_inputs()
next(gen)      # run up to the first yield
print(gen.send(10) )   # goes into 'x' variable
#20

next(gen)       # run up to the next yield
print(gen.send(6) )    # goes into 'x' again
#12

next(gen)       # run up to the next yield
print(gen.send(94.3))  # goes into 'x' again
#188.5999999999999

