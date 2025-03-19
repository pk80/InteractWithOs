import random


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


participants = ['Cathy', 'Fred', 'Jack', 'Tom']
print(guess(participants))

# The code seems to be working fine. However, there are some things that could go wrong, so find the part that might
# throw an exception and wrap it in a try-except block to ensure that you get sensible behavior. Do this in the cell
# below. Code your function to return None if an exception occurs.
