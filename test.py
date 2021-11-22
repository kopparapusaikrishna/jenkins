#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from main import equals

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """

        result1 = summation(12, 12)
        self.assertEqual(result1, 1)

        result2 = summation(13, 31)
        self.assertEqual(result2, 0)

        result3 = summation(1, 1)
        self.assertEqual(result3, 1)

        result4 = summation(12, 12)
        self.assertEqual(result4, 1)


if __name__ == '__main__':
    unittest.main()
