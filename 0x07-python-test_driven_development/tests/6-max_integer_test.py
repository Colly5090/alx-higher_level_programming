#!/usr/bin/python3
"Import all neccassary modules"
import unittest
max_integer = __import__("6-max_integer").max_integer

"Create a custom class to inherit all unittest testcases"


class TestMaxInteger(unittest.TestCase):
    "Test functions for each test case"
    def test_empty_list(self):
        self.assertIsNone(max_integer([]),)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_multiplepos_elements(self):
        self.assertEqual(max_integer([1, 2, 4, 6]), 6)

    def test_negative_elements(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mix_elements(self):
        self.assertEqual(max_integer([-1, -2, 3, 4]), 4)

    def test_float_elements(self):
        self.assertEqual(max_integer([0]), 0)

    def test_float_elements(self):
        self.assertEqual(max_integer([1, 2.2, 0]), 2.2)

    def test_float_elements(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)


if __name__ == "__main__":
    unittest.main()
