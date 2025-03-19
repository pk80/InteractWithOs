#!/usr/bin/env python3
import unittest
import os
import shutil


# Function to test
def addition(a, b):
    return a + b


# Paths to file operations
ORG_FILE = '/Users/praveen/PycharmProjects/InteractWithOS/mytests/org_file.txt'
COP_FILE = '/Users/praveen/PycharmProjects/InteractWithOS/mytests/cop_file.txt'

# Global counter
COUNTER = 0


# This method runs once before any tests or test classes
def setUpModule():
    global COUNTER
    COUNTER = 0
    # Create an org file
    with open(ORG_FILE, 'w') as file:
        file.write('Test Results:\n')


# This method runs after each individual test
def tearDowmModule():
    # copy org_file to cop_file
    shutil.copy2(ORG_FILE, COP_FILE)
    # remove org_file
    os.remove(ORG_FILE)


# Class
class TestAddition(unittest.TestCase):
    # This method will run before each individual test
    def setUp(self):
        global COUNTER
        COUNTER += 1

    # This method will run after each individual test
    def tearDown(self):
        # Append the test result to the file
        with open(ORG_FILE, 'a') as file:
            result = 'Passed' if self._outcome.success else 'Failed'
            file.write(f'Test {COUNTER}: {result}\n')

    def test_add_positive(self):
        self.assertEqual(addition(3, 4), 7)

    def test_add_negative(self):
        self.assertEqual(addition(-3, -4), -7)


# Running the test suite
suite = unittest.TestLoader().loadTestsFromTestCase(TestAddition)
runner = unittest.TextTestRunner()
runner.run(suite)

# Read the copied file to show the results
with open(COP_FILE, 'r') as file:
    test_results = file.read()

print(test_results)

#  In the example, a global counter is initialized in setUpModule.
#  The counter is incremented in the setUp method before each test starts.
#  After each test is completed, the tearDown method checks the test result and appends it to the temporary file.
#  During module teardown in tearDownModule,
#  the temporary file is copied to another directory and the original file is deleted
