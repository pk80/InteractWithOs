# Python Subprocesses

import subprocess
import os

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
my_env = os.environ.copy()
my_env['PATH'] = os.pathsep.join(['opt/myapp/', my_env['PATH']])
result = subprocess.run(['myapp'], env=my_env)
