#!/usr/bin/env python3
import unittest

from assignment import find_email


class TestEmails(unittest.TestCase):
    def test_basic(self):
        testcase = [None, 'Blossom', 'Gill']
        expected = 'blossom@abc.edu'
        self.assertEqual(find_email(testcase), expected)

    def test_one(self):
        testcase = [None, 'John']
        expected = 'Missing parameters'
        self.assertEqual(find_email(testcase), expected)

    def test_none(self):
        testcase = [None]
        expected = 'Missing parameters'
        self.assertEqual(find_email(testcase), expected)

    def test_two(self):
        testcase = [None, 'Roy', 'George']
        expected = 'No email address found'
        self.assertEqual(find_email(testcase), expected)


if __name__ == '__main__':
    unittest.main()
