#!/usr/bin/env python3
import csv
import sys


# Qwiklab Assignment:
# Imagine one of your IT coworkers just retired and left a folder of scripts for you to use. One of the scripts, called
# emails.py, matches users to an email address and lets us easily look them up! For the most part, the script works
# great — you enter an employee's name and their email is printed to the screen. But, for some employees, the output
# doesn't look quite right. Your job is to add a test to reproduce the bug, make the necessary corrections, and verify
# that all the tests pass to make sure the script works! Best of luck!
#
# What you'll do
#
# - Write a simple test to check for basic functionality
# - Write a test to check for edge cases
# - Correct code with a try/except statement
#
# cat ~/data/user_emails.csv
# cat ~/scripts/emails.py

def populate_dictionary(filename):
    """reads the user_emails.csv file and populates a dictionary with name/value pairs"""
    email_dicts = {}
    with open(filename, 'r') as file:
        content = csv.DictReader(file)
        for row in content:
            name = row['Full_Name'].lower()
            email_dicts[name] = row['Email']
        file.close()
    return email_dicts


def find_email(argv):
    """searches the dictionary created in the previous function for the username passed to the function as a parameter
    and then returns the associated email address. It accepts employee's first name and last name as command-line arguments"""
    try:
        name = argv[1] + ' ' + argv[2]
        dict_emails = populate_dictionary('/Users/praveen/PycharmProjects/InteractWithOS/mytryexcept/user_emails.csv')
        return dict_emails[name.lower()]
        # for person, mail in dict_emails.items():
        #     if person == name.lower():
        #         return mail
    except IndexError:
        return 'Missing parameters'
    except KeyError:
        return 'No email address found'


def main():
    print(find_email(sys.argv))
    # no parameters given : IndexError
    # only one parameter : IndexError


if __name__ == '__main__':
    main()
