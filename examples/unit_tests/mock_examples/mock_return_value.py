import unittest
from unittest import mock

import os



def simple_urandom(length):
    return 'f' * length


class TestRandom(unittest.TestCase):

    #replacing os.urandom with simple_urandom

    @mock.patch('os.urandom', return_value='fffff')
    def test_urandom(self, urandom_function):
        assert os.urandom(5) == 'fffff'