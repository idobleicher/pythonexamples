#Sending data to a generator yield from - Part 2 - Exception handling

class SpamException(Exception):
    pass

def writer():
    while True:
        try:
            w = (yield)
        except SpamException:
            print('***')
        else:
            print('>> ', w)


def writer_wrapper_1_not_handling_exception(wrapped_coroutine):
    wrapped_coroutine.send(None)  # prime the wrapped_coroutine
    while True:
        try:
            x = (yield)  # Capture the value that's sent
            wrapped_coroutine.send(x)  # and pass it to the writer
        except StopIteration:
            pass


def writer_wrapper_2(wrapped_coroutine):
    """Works. Manually catches exceptions and throws them"""
    wrapped_coroutine.send(None)  # prime the coro
    while True:
        try:
            try:
                x = (yield)
            except Exception as e:   # This catches the SpamException
                wrapped_coroutine.throw(e)
            else:
                wrapped_coroutine.send(x)
        except StopIteration:
            pass


#Using yield from - elegant
def writer_wrapper_3(coro):
    yield from coro




def check_wrapped_writer_with_exception(wrap):
    wrap.send(None)  # "prime" the coroutine

    for i in [0, 1, 2, 'spam', 4]:
        if i == 'spam':
            wrap.throw(SpamException)
        else:
            wrap.send(i)



my_writer = writer()
wraped_writer_1 = writer_wrapper_1_not_handling_exception(my_writer)

###  will not work: check_wrapped_writer_with_exception(wraped_writer_1)

#  Expected Result
# >>  0
# >>  1
# >>  2
# ***
# >>  4
#
# # Actual Result
# >>  0
# >>  1
# >>  2
# Traceback (most recent call last):
#   ... redacted ...
#   File ... in writer_wrapper
#     x = (yield)
# __main__.SpamException

wraped_writer_2 = writer_wrapper_2(my_writer)
check_wrapped_writer_with_exception(wraped_writer_2)



wraped_writer_3 = writer_wrapper_3(my_writer)
check_wrapped_writer_with_exception(wraped_writer_3)