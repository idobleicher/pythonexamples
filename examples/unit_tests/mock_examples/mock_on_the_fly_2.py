import unittest
from unittest import mock
from  unit_tests.mock_examples import fots
import os



#NOTE the order!!! (mocked_some_method parameter before  mocked_urandom) - Python calls @patch decorators from the "bottom up".

class TestRandom(unittest.TestCase):
    @mock.patch('os.urandom')
    @mock.patch('unit_tests.mock_examples.fots.some_method')
    def test_abc_urandom(self , mocked_some_method ,mocked_urandom):

       mocked_urandom.return_value = 'pumpkins'
       assert os.urandom(5) == 'pumpkins'
       mocked_some_method.return_value = "xxx"
       result =  fots.some_method()
       assert result == "xxx"

      # mocked_some_method.return_value = 'xxx'
      # assert fots.some_method() == 'xxx'
