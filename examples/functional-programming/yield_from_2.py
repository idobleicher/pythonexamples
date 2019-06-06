# Sending data to a generator (coroutine) using yield from - Part 1

# Now let's do something more interesting. Let's create a coroutine called writer that accepts data sent to it and writes to a socket, fd, etc.

def writer():
    """A coroutine that writes data *sent* to it to fd, socket, etc."""
    while True:
        w = (yield)
        print('>> ', w)

#Now the question is, how should the wrapper function handle sending data to the writer,
# so that any data that is sent to the wrapper is transparently sent to the writer()?

#The wrapper needs to accept the data that is sent to it (obviously) and should also handle the StopIteration w
# hen the for loop is exhausted.
# Evidently just doing for x in wrapped_coroutine : yield x won't do. Here is a version that works.

def writer_wrapper(wrapped_coroutine):
    wrapped_coroutine.send(None)  # prime the wrapped_coroutine
    while True:
        try:
            x = (yield)  # Capture the value that's sent
            wrapped_coroutine.send(x)  # and pass it to the writer
        except StopIteration:
            pass


#elegant alternative using from:
def writer_wrapper_2(wrapped_coroutine):
   yield from wrapped_coroutine



def func_use_wrapper(wrapper):
    wrapper.send(None)  # "prime" the coroutine

    for i in range(4):
        wrapper.send(i)


my_writer = writer()
wraped_writer_1 = writer_wrapper(my_writer)

wraped_writer_2 = writer_wrapper_2(my_writer)


func_use_wrapper(wraped_writer_1)

func_use_wrapper(wraped_writer_2)