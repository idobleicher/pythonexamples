from contextlib import contextmanager

@contextmanager
def conm1(param1):
    print("econm1 enter:param %s" % param1)
    yield "X-{}".format(param1)
    print("econm1 exit:param %s" % param1)


@contextmanager
def conm2(param1):
    print("econm2 enter:param %s" % param1)
    yield "Y-{}".format(param1)
    print("econm2 exit:param %s" % param1)




with conm1("a") as cm1,\
     conm2("b") as cm2:
    print("start")
    print(cm1)
    print("----------")
    print(cm2)
    print("end")