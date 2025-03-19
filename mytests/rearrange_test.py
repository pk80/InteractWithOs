#!/usr/bin/env python3

import unittest
from rearrange import rearrange_name


class TestRearrangeName(unittest.TestCase):
    def test_basic(self):
        testcase = 'Praveen Kumar, K'
        expected = 'K Praveen Kumar'
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = 'Hopper, Grace M.'
        expected = 'Grace M. Hopper'
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = 'Praveen'
        expected = 'Praveen'
        self.assertEqual(rearrange_name(testcase), expected)


# Run the test
unittest.main()
