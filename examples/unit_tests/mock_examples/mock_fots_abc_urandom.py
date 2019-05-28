import unittest
from unittest import mock
from unit_tests.mock_examples.fots import abc_urandom

def simple_urandom(length):
    return 'f' * length



class TestRandom(unittest.TestCase):
    @mock.patch('unit_tests.mock_examples.fots.urandom', side_effect=simple_urandom)
    def test_abc_urandom(self, abc_urandom_function):
        assert abc_urandom(5) == 'abcfffff'