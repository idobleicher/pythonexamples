#https://docs.python.org/3/library/unittest.html

# The unittest module provides a rich set of tools for constructing and running tests.
# This section demonstrates that a small subset of the tools suffice to meet the needs of most users.
#
# Here is a short script to test three string methods:



#The three individual tests are defined with methods whose names start with the letters test.
# This naming convention informs the test runner about which methods represent tests.

#The setUp() and tearDown() methods allow you to define instructions that will be executed before and after each test method.

#The final block shows a simple way to run the tests. unittest.main() provides a command-line interface to the test script. When run from the command line, the above script produces an output that looks like this:

import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print("this is setup")

    def tearDown(self):
        print("this is tearDown")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string

        #assert raise- verify that a specific exception gets raised.
        with self.assertRaises(TypeError):
            s.split(2)


#The final block shows a simple way to run the tests. unittest.main() provides a command-line interface to the test script.
if __name__ == '__main__':
    unittest.main()



