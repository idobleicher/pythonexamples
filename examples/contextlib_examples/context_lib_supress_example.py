import contextlib


class Exception_A(Exception):
    pass

class Exception_B(Exception):
    pass


def a() :
    print("a")
    raise Exception_A



def b() :
    print("b")
    raise Exception_B

try:
    a()
    try:
        b()
    except Exception_B:
        pass
except Exception_A:
    pass


#Alternative:
with contextlib.suppress(Exception_A):
    a()
    with contextlib.suppress(Exception_B):
        b()