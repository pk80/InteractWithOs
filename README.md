# Interaction with Operating System with Python

## Interpreted Language vs Compiled Language
Examples of Compiled programming languages : C, C++, Go, Rust
- They relay on compilers
Examples of Interpreted programming languages : Python, Ruby, JavaScript, Bash, PowerShell
- They relay on interpreters 
Examples of mixed approach (both compiler and interpreter) programming languages : Java, C#

## Running a Python Script
- Command prompt to run a python file : python3 <file_name> on linux & macOs, <file_name> on windows
- file extension : .py
- commands:
  - exit() or Ctl+D on linux & macOs, Ctl+Z on windows  
  - cat (shows contents of files on linux / macOs)
  - 

## Code reusability
- Modules : file names

## Code Editors or IDEs
- Editors : Vim, Notepad(Widows), TextEdit(MacOs), Nano(Linux,MacOs)
- Advanced Editors : Atom, Notepad++, Sublime Text, VisualStudio
- Featured Editors : Eclipse, PyCharm

- Common editor for all platforms : Eclipse, PyCharm, Sublime Text, VisualStudio

## Python Specific Editors
- PyCharm, Spyder, Thonny

## Create, activate and deactivate virtual environments for Python
```txt
python3 -m venv myenv
# activate on mac/linux
myenv/bin/activiate 
# activate on windows
myenv/Scripts/activiate
# deactivate
deactivate
```

## Generate Requirements file list
```txt
pip freeze > requirements.txt
```
## Install Requirements file
```txt
pip install -r requirements.txt
```