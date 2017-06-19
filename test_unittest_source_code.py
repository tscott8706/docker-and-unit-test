# test_unittest_source_code
from unittest_source_code import *
from unittest import TestCase

class test_unittest_source_code(TestCase):

    def test_is_string_within_string_true(self):
        self.assertTrue(is_string_within_string("Hello World", "ello"))
