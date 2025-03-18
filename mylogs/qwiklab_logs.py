#!/usr/bin/env python3

"""
# Qwiklab work
You dealt with a program that kept throwing an error because the source code was too complicated to quickly find the
error. The good news is that the program outputs a log file you could read! Let's review how to write a script to
search the log file for the exact error, then output that error into a separate file so you can work out what's wrong.

logfile = /Users/praveen/PycharmProjects/InteractWithOS/mylogs/fishy_log.log

Month Day hour:minute:second mycomputername "process_name"["random 5 digit number"] "ERROR/INFO/WARN" "Error description"
July 31 00:26:45 mycomputername CRON[83063]: INFO I'm sorry Dave. I'm afraid I can't do that
July 31 00:44:50 mycomputername kernel[63793]: ERROR Failed process [13966]
...

search for the CRON error that failed to start
"""
import os.path
import re
import sys


def error_search(log_file):
    error = input('What is the error? ')  # CRON ERROR Failed to start
    returned_errors = []

    with open(file=log_file, mode='r', encoding='UTF-8') as file:
        for log_line in file.readlines():
            error_patterns = ['error']  # list to store all the patterns (user input) that will be searched
            for i in range(len(error.split(' '))):
                error_patterns.append(r'{}'.format(error.split(' ')[i].lower()))
                if all(re.search(error_pattern, log_line.lower()) for error_pattern in error_patterns):
                    returned_errors.append(log_line.strip())
        file.close()

    return returned_errors


def file_output(errors_output):
    # os.path.expanduser('~') : returns the home directory of the user
    output_file = '/Users/praveen/PycharmProjects/InteractWithOS/mylogs/errors_found.log'
    # output_file = os.path.expanduser('~') + '/data/errors_found.log'
    with open(output_file, 'w') as file:
        for error in errors_output:
            file.write(error + '\n')

        file.close()
    print('writing to file is complete')


if __name__ == '__main__':
    logfile = sys.argv[1]
    if not os.path.isfile(logfile):
        print('Please provide correct file...')
        sys.exit(1)

    output = error_search(logfile)
    file_output(output)
    sys.exit(0)


"""
import sys
import os
import re


def error_search(log_file):
    error = input('Provide the error? ')
    returned_errors = []

    with open(log_file, 'r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ['error']
            for i in range(len(error.split(' '))):
                error_patterns.append(r'{}'.format(error.split(' ')[i].lower()))
                if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                    returned_errors.append(log)
        file.close()

    return returned_errors


def file_output(returned_errors):
    output_file = os.path.expanduser('~') + '/data/errors_found.log'
    with open(output_file, 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()


if __name__ == '__main__':
    log_file = sys.argv[1]
    if not os.path.isfile(log_file):
        print('Provide correct file path')
        sys.exit(1)
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)
"""