import unittest
from examples.unit_tests.test_suite_example.Widget import *

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        print("This is setup")
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        print ("This is test_default_widget_size")
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        print("This is test_widget_resize")
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

    def tearDown(self):
        print("This is tear down")
        self.widget.dispose()
