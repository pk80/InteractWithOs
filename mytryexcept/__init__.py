# Try and Except
import random


# basic structure of exception handling
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return 'file not found'
    finally:
        print('finished reading file')


def faulty_read_and_divide(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
        num1 = int(data[0])
        num2 = int(data[1])
        return num1 / num2


def enhanced_read_and_divide(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readlines()

            if len(data) < 2:
                raise ValueError('Not enough data in the file')

            num1 = int(data[0])
            num2 = int(data[1])

            if num2 == 0:
                raise ZeroDivisionError('The denominator is zero')

            return num1 / num2
    except FileNotFoundError:
        return 'Error: file not found'
    except ValueError as ve:
        return f'Value Error: {ve}'
    except ZeroDivisionError as zde:
        return f'Division Error: {zde}'


print(read_file('/Users/praveen/PycharmProjects/InteractWithOS/mytests/org_fileq.txt'))


def guess(participants):
    try:
        my_participant_dict = {}
        for participant in participants:
            my_participant_dict[participant] = random.randint(1, 9)
        if my_participant_dict['Larry'] == 9:
            return True
        else:
            return False
    except KeyError:
        return None


participants = ['Cathy', 'Fred', 'Jack', 'Larry']
# participants = ['Cathy', 'Fred', 'Jack', 'Tom']
print(guess(participants))

# The code seems to be working fine. However, there are some things that could go wrong, so find the part that might
# throw an exception and wrap it in a try-except block to ensure that you get sensible behavior. Do this in the cell
# below. Code your function to return None if an exception occurs.
