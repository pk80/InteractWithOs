# Python Subprocesses

import subprocess
import os
from pathlib import Path

# Running system commands in python
subprocess.run(['date'])
subprocess.run(["sleep", "2"])

result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)  # return code=1 ; No such file or directory

# Obtaining the output of a system command
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
# result = subprocess.run(["host", "192.168.0.2"], capture_output=True)
# result = subprocess.run(["host", "10.0.0.1"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stdout.decode().split())
print(result.stderr)

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)

# Advanced subprocess management
my_env = os.environ.copy()  # creates a dictionary
# print(my_env)
for k, v in my_env.items():
    # print(k, ":", v)
    if k == 'PATH':
        paths = v.split(':')
        for path in paths:
            print(path)
# my_env['PATH'] = os.pathsep.join(['opt/myapp/', my_env['PATH']])
# result = subprocess.run(['myapp'], env=my_env)

# Python subprocesses
print('______________________ Python Subprocesses')
# using os
cwd = os.getcwd()
print(cwd)
# using pathlib
path_cwd = Path.cwd()
print(path_cwd)
# using subprocess
cwd_subprocess = subprocess.check_output(['pwd'], text=True).strip()
print(cwd_subprocess)

# run()
result_run = subprocess.run(['echo', 'Hello, World!'], capture_output=True, text=True)
print(result_run.stdout.strip())  # Extracting the stdout and stripping any extra whitespace

# call()
return_code_call = subprocess.call(['echo', 'Hello from call!'])
print(return_code_call)

# Check_call and check_output
return_code_check_call = subprocess.check_call(['echo', 'Hello from check_call!'])
print(return_code_check_call)
output_check_output = subprocess.check_output(['echo', 'Hello from check_output!'], text=True)
print(output_check_output.strip())  # Extracting the stdout and stripping any extra whitespace

# Popen()
process_popen = subprocess.Popen(['echo', 'Hello from popen!'], stdout=subprocess.PIPE, text=True)
output_popen, _ = process_popen.communicate()
print(output_popen.strip())  # Extracting the stdout and stripping any extra whitespace
