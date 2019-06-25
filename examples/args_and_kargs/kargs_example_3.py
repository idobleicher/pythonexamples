
def my_func(a=None , b=None, **kwargs):
    print(a)
    print(b)


def my_func2(c=None, d=None , e=None, **kwargs):
    print(c)
    print(d)
    print(e)


func_resolver= {
   1:my_func,
   2:my_func2
}


def call_resolved_func(func_num):
    func = func_resolver.get(func_num)
    func(e=5,c=3,a=1,d=4,b=2)

call_resolved_func(1)
print("----------")
call_resolved_func(2)