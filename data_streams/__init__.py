# DATA STREAMS

import os
import sys


def hello():
    """Reading data interactively"""
    name = input('Please enter your name: ')
    print(f'Hello, {name}')


def streams():
    """Standard streams"""
    data = input('This will come from STDIN: ')
    print(f'Now we write it to STDOUT: {data}')
    print(f'Now we generate an error to STDERR: {data + 1}')


def env_variables():
    """Environment Variables"""
    print(f'HOME: {os.environ.get('HOME', '')}')
    print(f'SHELL: {os.environ.get('SHELL', '')}')
    print(f'FRUIT: {os.environ.get('FRUIT', '')}')


def cmd_line_args():
    """Command-line Arguments"""
    print(sys.argv)
    # refer cmd_args.py file for more details

