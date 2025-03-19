#!/usr/bin/env python3
import unittest

# Unit test design pattern

class Library:
    def __init__(self):
        self.collection = []

    def add_book(self, book_title):
        self.collection.append(book_title)

    def has_book(self, book_title):
        return book_title in self.collection


# Unit test for the Library system
class TestLibrary(unittest.TestCase):
    def test_adding_book(self):
        library = Library()
        testcase = 'Python Design Patterns'
        library.add_book(testcase)
        self.assertTrue(library.has_book(testcase))


library_test_output = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestLibrary))
print(library_test_output)
