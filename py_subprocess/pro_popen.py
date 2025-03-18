import subprocess
import time

process = subprocess.Popen(['sleep', '3'])

msg_1 = 'The process is running in the background'
time.sleep(2)

# print(process.poll())
# time.sleep(1)
# print(process.poll())

if process.poll() is None:
    msg_2 = 'The process is still running'
else:
    msg_2 = 'The process has finished'

print(msg_1, ':', msg_2)
