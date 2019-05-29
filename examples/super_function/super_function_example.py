class MyParentClass(object):
    def __init__(self):
        print("in MyParentClass")
        pass


class SubClass(MyParentClass):
    def __init__(self):
        #But we still need to initialize the parent class within the subclass.
        # To make this process easier, Python’s core development team created the super function.
        # The goal was to provide a much more abstract and portable solution for initializing classes.
        MyParentClass.__init__(self)

#IN python 2:
class SubClass2(MyParentClass):
    def __init__(self):
        super(SubClass2, self).__init__()

super_class_2 = SubClass2()

#IN python 3:

class SubClass3(MyParentClass):
    def __init__(self):
        super().__init__()


super_class_3 = SubClass3()
