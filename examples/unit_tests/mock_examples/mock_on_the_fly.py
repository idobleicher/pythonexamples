import unittest
from unittest import mock
import os



class TestRandom(unittest.TestCase):
    @mock.patch('os.urandom')
    def test_abc_urandom(self, urandom_function):
        urandom_function.return_value = 'pumpkins'
        assert os.urandom(5) == 'pumpkins'

        urandom_function.return_value = 'lemons'
        assert os.urandom(5) == 'lemons'

        urandom_function.side_effect = (
            lambda l: 'f' * l
        )
        assert os.urandom(5) == 'fffff'