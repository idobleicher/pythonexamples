
def func_yield_with_break():
    for num in range(1, 20):
        if num < 10:
            yield num
        else:
            print('highr', num)
        break


def fun_get_all():
    objects = func_yield_with_break()
    for obj in objects:
        yield obj


nums = list(fun_get_all())
print(nums)

