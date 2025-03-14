# CSV module
import csv
import os


# rw_files.read_file('../assets/submissions.csv')

def read_csv(filename):
    """Reading csv file using csv module"""
    with open(filename, 'r') as file:
        # content is the instance of reader class
        content = csv.reader(file)
        # rules of csv file
        print(content.dialect.delimiter)
        print(content.dialect.quotechar)
        print(content.dialect.strict)
        # -----------------------------
        for row in content:
            # every row is a list of data in columns
            print(row)
            # # unpacking row
            # submission, hacker, challenge, score = row
            # print(f'{hacker} submitted {challenge} challenge with submission id {submission} and scored {score}.')


def write_csv(filename, data):
    """Generating csv file using csv module"""
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        # rules of csv file
        print(writer.dialect.delimiter)
        print(writer.dialect.quotechar)
        print(writer.dialect.strict)
        # -----------------------------
        writer.writerows(data)
    print('Writing to file is complete.')


def delete_csv(filename):
    """Delete a file"""
    if os.path.isfile(filename):
        os.remove(filename)
    print(f'{filename} has been removed')


# Reading and writing CSV files with dictionaries
def read_dict_csv(filename):
    with open(filename, 'r') as file:
        content = csv.DictReader(file)
        for row in content:
            print('Name :{}, Status :{}, Users :{}'.format(row['name'],row['status'],row['users']))


def write_dict_csv(filename, data, keys):
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f'Finished writing dict to file at {filename}')
