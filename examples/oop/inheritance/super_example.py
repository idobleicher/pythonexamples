# The function super is a useful inheritance-related function that refers to the parent class.
# It can be used to find the method with a certain name in an object's superclass.

class A:
    def spam(self):
        print(1)


class B(A):
    def spam(self):
        print(2)
        #super().spam() calls the spam method of the superclass.
        super().spam()


B().spam()
#2
#1