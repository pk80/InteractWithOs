import datetime
import os

import areas
import data_streams
import mycsv
import myregex
import system_health
import rw_files
from rw_files import new_dir


def main():
    print(f"{'-' * 42}")
    print('Welcome to Interaction with OS with Python')
    print(f"{'-' * 42}")

    # # Areas of shapes from areas package
    # print(f"{'_' * 10} Area 0f Shapes {'_' * 17}")
    # print(f'Area of triangle : {areas.triangle(5, 3)}')
    # print(f'Area of rectangle : {areas.rectangle(5, 3)}')
    # print(f'Area of circle : {areas.circle(5)}')
    # print(f'Area of donut : {areas.donut(5, 3)}')
    #
    # # System Health Check from system_health pacakge
    # print(f"{'_' * 10} System Health Check {'_' * 12}")
    # if not system_health.check_disk_usage('/') or not system_health.check_cpu_usage(1):
    #     print('Error')
    # else:
    #     print('Everything is ok!')

    # # Reading file
    # rw_files.read_file('assets/submissions.csv')
    # # Read line in a file
    # rw_files.read_line('assets/submissions.csv')
    # # Read lines in a file
    # rw_files.read_lines('assets/submissions.csv')
    # Iterate over lines in file
    # rw_files.iterate_file('assets/submissions.csv')
    #
    # Writing file
    # rw_files.write_file('assets/output.csv', 'Hell World!')

    # rw_files.new_dir('assets/test_1','scripts.txt')
    # result = rw_files.new_dir('assets/test_1/','scripts.txt')
    # print(result)

    # rw_files.parent_directory()

    # # Reading and writing using csv module
    # # reading from csv file
    # mycsv.read_csv('assets/software.csv')
    # # writing data to csv
    # emp_list = [['praveen kumar', '8686960907', 'DevOps Eng'], ['praveen', '9502551905', 'DevOps Eng']]
    # mycsv.write_csv('assets/emp.csv', emp_list)
    # # deletes the file
    # mycsv.delete_csv('assets/emp.csv')

    # mycsv.read_dict_csv('assets/software.csv')
    # users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
    #          {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
    #          {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
    # keys = ["name", "username", "department"]
    # mycsv.write_dict_csv('assets/output.csv', users, keys)

    # LAB WORK 2
    # call the functions: contains_domain() and replace_domain from the main()
    # write the updated list to a CSV file in the data directory
    # csv_file_location = '/home/student/data/user_emails.csv'
    # report_file = '/home/student/data/updated_user_emails.csv'
    # old_domain, new_domain = 'abc.edu', 'xyz.edu'
    # if myregex.contains_domain(address, old_domain):
    #     print(myregex.replace_domain(address, old_domain, new_domain))
    # else:
    #     print('Domain does not exit!')
    # csv_file = 'assets/user_emails.csv'
    # report_file = 'assets/updated_user_emails.csv'
    # myregex.update_csv(csv_file, report_file, old_domain, new_domain)

    # Module 3
    data_streams.cmd_line_args()


if __name__ == '__main__':
    main()
