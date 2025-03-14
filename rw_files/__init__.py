# Reading and Writing files
import datetime
import dis
import os.path


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def iterate_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())
            # print(line.strip().upper())
            # print(line,end="")


def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)


def read_line(file_path):
    file = open(file_path, 'r')
    line = file.readline()
    file.close()
    print(line)


def read_lines(file_path):
    file = open(file_path)
    lines = file.readlines()
    file.close()
    print(lines)


# # Lab work
#     guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]
#     # writing to file
#     with open('assets/guests.txt', 'w') as file:
#         for i in guests:
#             file.write(i + '\n')
#     # reading from file
#     rw_files.read_file('assets/guests.txt')
#     # updating file
#     new_guests = ['John', 'Rachel', 'Robert']
#     with open('assets/guests.txt', 'a') as file:
#         for i in new_guests:
#             file.write(i + '\n')
#     rw_files.read_file('assets/guests.txt')
#     # checked out
#     checked_out = ["Andrea", "Manuel", "Khalid"]
#     temp_list = []
#     with open("assets/guests.txt", 'r') as file:
#         for g in file:
#             temp_list.append(g.strip())
#     with open("assets/guests.txt", 'w') as file:
#         for name in temp_list:
#             if name not in checked_out:
#                 file.write(name + "\n")
#     rw_files.read_file('assets/guests.txt')
#     # check guest
#     check_guests = ['Bob', 'Andrea']
#     checked_in = []
#     with open('assets/guests.txt', 'r') as file:
#         for g in file:
#             if g.strip() in check_guests:
#                 checked_in.append(g.strip())
#     print(checked_in)


# # File Paths:
#     cwd = os.getcwd()
#     outputs = {'files_dirs': os.listdir(),
#                'current_dir': os.getcwd(),
#                'path_vars': os.environ.get('PATH')}
#     print(cwd)
#     print(outputs['files_dirs'])
#     print(outputs['current_dir'])
#     print(outputs['path_vars'])


# # Managing files and directories
#     result = os.path.exists('main.py')
#     result = os.path.getsize('main.py')
#     result = os.path.getmtime('main.py')
#     result = datetime.datetime.fromtimestamp(result)
#     result = os.path.abspath('main.py')
#     result = os.path.isfile('main.py')
#     print(result

# create directory and an empty file
def new_dir(directory, filename):
    if not os.path.isdir(directory):
        os.mkdir(directory)

    os.chdir(directory)
    with open(filename, 'w') as file:
        pass

    dt = os.path.getmtime(filename)
    d = datetime.datetime.fromtimestamp(dt)
    print(os.listdir(directory))
    # return os.listdir(directory)


# Question 5
# The parent_directory function returns the name of the directory that's
# located just above the current working directory.
# Remember that '..' is a relative path alias that means
# "go up to the parent directory". Fill in the gaps to complete this function.
def parent_directory():
    # Create a relative path to the parent
    # of the current working directory
    os.chdir('..')
    relative_parent = os.path.join('..', os.getcwd())
    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)
"""
Incorrect
Not quite. We're looking for the name of the parent
directory, not the current working directory.

by including chdir method it is correct
"""
