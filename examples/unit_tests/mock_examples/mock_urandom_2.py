import unittest
from os import urandom
from unittest import mock

#if we imported the urandom function using a from statement (from os import urandom) is a special case where you can use __main__ to mock the function:


def simple_urandom(length):
    return 'f' * length


class TestRandom(unittest.TestCase):
    @mock.patch('__main__.urandom', side_effect=simple_urandom)
    def test_urandom(self, urandom_function):
        assert urandom(5) == 'fffff'