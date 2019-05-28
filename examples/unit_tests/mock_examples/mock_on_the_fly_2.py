import unittest
from unittest import mock
from  unit_tests.mock_examples import fots
import os


class TestRandom(unittest.TestCase):
    @mock.patch('os.urandom')
    @mock.patch('unit_tests.mock_examples.fots.some_method')
    def test_abc_urandom(self, mocked_urandom , mocked_some_method):

       mocked_urandom.return_value = 'pumpkins'
       assert os.urandom(5) == 'pumpkins'


      # mocked_some_method.return_value = 'xxx'
      # assert fots.some_method() == 'xxx'
