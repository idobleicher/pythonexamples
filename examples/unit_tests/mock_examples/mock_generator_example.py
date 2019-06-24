from unittest import mock


class Foo(object):
    def iter(self):
        for i in [1, 2, 3]:
            yield i
...
foo = Foo()
print(list(foo.iter()))

values = [10, 20, 30]
mock_foo = mock.MagicMock()
iterable = mock_foo.iter.return_value
iterator = iter(values)
iterable.__iter__.return_value = iterator
print(list(mock_foo.iter()))

#The above example is done step-by-step. The shorter version is:
mock_foo2 = mock.MagicMock()
mock_foo2.iter.return_value.__iter__.return_value = iter([11, 22, 33])
print(list(mock_foo2.iter()))
