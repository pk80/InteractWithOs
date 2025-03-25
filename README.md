from os import write

# Interaction with Operating System with Python

<!-- TOC -->
* [Interaction with Operating System with Python](#interaction-with-operating-system-with-python)
  * [Interpreted Language vs Compiled Language](#interpreted-language-vs-compiled-language)
  * [Running a Python Script](#running-a-python-script)
  * [Code reusability](#code-reusability)
  * [Code Editors or IDEs](#code-editors-or-ides)
  * [Python Specific Editors](#python-specific-editors)
  * [Create, activate and deactivate virtual environments for Python](#create-activate-and-deactivate-virtual-environments-for-python)
  * [Generate Requirements file list](#generate-requirements-file-list)
  * [Install Requirements file](#install-requirements-file)
  * [MODULE 2](#module-2)
    * [Reading and Writing files](#reading-and-writing-files)
      * [Programming with files](#programming-with-files)
      * [Reading files](#reading-files)
      * [Iterating through files](#iterating-through-files)
      * [Writing files](#writing-files)
      * [Reading and Writing files](#reading-and-writing-files-1)
    * [File paths](#file-paths)
    * [Managing files and directories](#managing-files-and-directories)
    * [Reading and writing csv files](#reading-and-writing-csv-files)
      * [Reading and writing CSV files with dictionaries](#reading-and-writing-csv-files-with-dictionaries)
  * [MODULE 3](#module-3)
    * [Regular Expressions](#regular-expressions)
    * [Basic Regular Expressions](#basic-regular-expressions)
      * [Simple matching](#simple-matching)
      * [Wildcards and Character classes](#wildcards-and-character-classes)
    * [Advanced Regular Expressions](#advanced-regular-expressions)
  * [MODULE 4](#module-4)
    * [Data Streams](#data-streams)
    * [Python Subprocesses](#python-subprocesses)
    * [Processing Log Files](#processing-log-files)
    * [Qwiklab Assignment:](#qwiklab-assignment)
  * [MODULE 5](#module-5)
    * [Simple Tests](#simple-tests)
    * [Unit Tests](#unit-tests)
    * [Pytest](#pytest)
      * [Key difference between unittest and pytest](#key-difference-between-unittest-and-pytest)
      * [Edge Case](#edge-case)
      * [Assertions](#assertions)
      * [Test Suites](#test-suites)
    * [Other Test Concepts](#other-test-concepts)
      * [More about tests](#more-about-tests)
    * [Errors and Exceptions](#errors-and-exceptions)
      * [Terms and definitions from course 2, module 5](#terms-and-definitions-from-course-2-module-5)
    * [Qwiklab Assignment](#qwiklab-assignment-1)
  * [MODULE 6](#module-6)
    * [Interacting with command-line shell](#interacting-with-command-line-shell)
    * [Bash scripting](#bash-scripting)
    * [Advanced Bash concepts](#advanced-bash-concepts)
    * [Glossary](#glossary)
    * [Qwiklab Assignment](#qwiklab-assignment-2)
    * [IT skills in action reading](#it-skills-in-action-reading)
  * [MODULE 7](#module-7)
    * [Getting ready for the final project](#getting-ready-for-the-final-project)
    * [Job searching and Professional Networking](#job-searching-and-professional-networking)
    * [Course warp-up](#course-warp-up)
<!-- TOC -->

## Interpreted Language vs Compiled Language

Examples of Compiled programming languages : C, C++, Go, Rust

- They relay on compilers
  Examples of Interpreted programming languages : Python, Ruby, JavaScript, Bash, PowerShell
- They relay on interpreters
  Examples of mixed approach (both compiler and interpreter) programming languages : Java, C#

## Running a Python Script

- Command prompt to run a python file : python3 <file_name> on linux & macOS, <file_name> on windows
- file extension : .py
- commands:
    - exit() or Ctl+D on linux & macOs, Ctl+Z on windows
    - cat (shows contents of files on linux / macOS)
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

```text
python3 -m venv myenv
# activate on mac/linux
myenv/bin/activate 
# activate on windows
myenv/Scripts/activate
# deactivate
deactivate
```

## Generate Requirements file list

```text
% pip freeze > requirements.txt
```

## Install Requirements file

```text
% pip install -r requirements.txt
```

## MODULE 2

### Reading and Writing files

#### Programming with files

- Python interacting with files directly
- Data is usually stored on a disk and saved in files
- Absolute path is the full/real path to the resource in the file system
- Relative path is portion of path to show where it is located in relation to current working directory
-

#### Reading files

- open() function returns a file object
- readline() method reads one line from the file and returns as string
- read() method reads the entire file and returns as string
- close() method closes the file
- with (key word) statement to open a file will open file and executed the code within the with block and closes the
  file
  automatically at the end
- File descriptor: a token, generated by OS, that allows programs to do more operations with file
- File open and close method of working with files is a typical way, the best way is to use with statement
-

#### Iterating through files

- If the file is small, reading complete file by `read` or `readlines` methods are okay
- If the file is large, reading line by line is the best method to follow else it'll lead poor performance

#### Writing files

- File objects can be opened in several modes which is the second argument like :
    - 'r' (read only, default)
    - 'w' (write only, truncating the file first)
    - 'a' (appending content)
    - 'x' (creation mode, fails if the file already exists)
    - '+' (open for updating in reading and writing)
    - 'b' (binary mode)
    - 'r+' (read-write)
    - 'rt' (read only in text mode, default)
- If you open an already existing file for writing, it will automatically delete the content the moment the file is
  opened
- Write method returns the number of characters written to the file
- Third argument is encoding,
    - the default is the platform-dependent
    - locale.getencoding() gets the current encoding
    - if you need to open the text in a specific encoding, you must specify it
    - binary mode data is read and written as bytes objects
    - you cannot specify encoding when opening a file in binary mode
    - you have to have permission to write to the directory where you’re placing the file

#### Reading and Writing files

```text
# Lab work
guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]
# writing to file
with open('assets/guests.txt', 'w') as file:
    for i in guests:
        file.write(i + '\n')
# reading from file
rw_files.read_file('assets/guests.txt')
# updating file
new_guests = ['John', 'Rachel', 'Robert']
with open('assets/guests.txt', 'a') as file:
    for i in new_guests:
        file.write(i + '\n')
rw_files.read_file('assets/guests.txt')
# checked out
checked_out = ["Andrea", "Manuel", "Khalid"]
temp_list = []
with open("assets/guests.txt", 'r') as file:
    for g in file:
        temp_list.append(g.strip())
with open("assets/guests.txt", 'w') as file:
    for name in temp_list:
        if name not in checked_out:
            file.write(name + "\n")
rw_files.read_file('assets/guests.txt')
# check guest
check_guests = ['Bob', 'Andrea']
checked_in = []
with open('assets/guests.txt', 'r') as file:
    for g in file:
        if g.strip() in check_guests:
            checked_in.append(g.strip())
print(checked_in)
```

### File paths

- The specific location of a file on a computer or web server is called file path
- You can also use file paths to call environment variables such as libraries, applications, and even other languages
  like C+ or JavaScripts.
- Two types of file paths:
    - Relative file path (r/w file by name alone)
    - Absolute file path (r/w file by exact location/drive/dir/file_name)
- Programmers tend to avoid absolute file paths because the drive names can change from computer to computer
- Python programmers wrap directories using the command OS path to work around the platform differences
- File paths are most often used to save and load information
- You can use the forward slash for writing the file path in Python
- If you use backslash in a file path, you have to use it again to escape every instance
- Uses :
    - Save Information
    - Load Information (applications, env variables)

```text
import os

outputs = dict()
outputs['files_and_directories'] = os.listdir()
outputs['current_directory'] = os.getcwd()
```

### Managing files and directories

- os.remove(<file_name>) : remove the file
- os.rename(<old_name, new_name>) : rename / move the file
- os.path.exists(<file_name>) : check if file exists
- os.path.getsize(<file_name>) : get size of the file in bytes
- os.path.getmtime(<file_name>) : get last modified unix timestamp for the file
- datetime.datetime.fromtimestamp(timestamp) : convert timestamp to readable time
- os.path.abspath(<file_name>) : get the absolute path of the file
- os.getcwd() : get current working directory
- os.mkdir(<dir_name>) : created new directory
- os.chdir(<new_dir>) : changes the directory
- os.rmdir(<dir_name>) : removes the directory
- os.listdir(<dir_name>): lists all files and subdirectories
- os.path.isfile(<file_name>) : checks if file_name is file or not
- os.path.isdir(<dir_name>) : checks if dir_name is dir or not
- os.path.join(<path>,<paths...>) : joins the path depending on the OS / underlying platform
- os.chmod()
- os module uses:
    - file operations (open,close,read,write,append)
    - directories (create,read,update,delete) and
    - permissions (create,read,update)

### Reading and writing csv files

- csv file: comma separated values, a common data format used to store data as segments of text separated by commas
- formats give data structure and computer loves structure
- parsing a file: analysing file's content to correctly structure the data

#### Reading and writing CSV files with dictionaries

- csv.DictReader()
- csv.DictWriter()

## MODULE 3

### Regular Expressions

- Also known as `regex` or `regexp`
- It is a search query for text that's expressed in string pattern
- It allows us to search for a text for string matching a specific pattern
- `grep` is case-sensitive
- `grep` is a command line regex tool
- Search is executed on the line basis but not on individual word

```text
% grep thon <filename>
% grep -i thon <filename> # use -i to avoid case-sensitivity
```

- Reserved Characters : give extra meaning to the patterns that we create
    - Exs:
        - . sign : dot matches any character, it is said to ba a wildcard
        - ^ sign : caret/circumflex indicates the beginning, it is said to be an anchor character
        - $ sign : dollar indicates the end of the line, it is said to be an anchor character

```text
% grep l.rts <filename>
% grep ^fruit <filename>
% grep cat$ <filename>
```

### Basic Regular Expressions

#### Simple matching

- Module used in `re`
- re.search(pattern, string) returns a match object
- `r` in pattern indicates raw-string (meaning no special chars)
- raw-string and normal string are exactly the same
- it's a good practise to use raw-strings in regular expressions in python
- `None` is a special value that python uses to show that there's not actual value there
- re.IGNORECASE option in search parameters ignores the case sensitivity

#### Wildcards and Character classes

```text
# Wildcards and Character classes
% print(re.search(r"[Pp]ython", "Python"))
% print(re.search(r"[a-z]way", "The end of the highway"))
% print(re.search(r"[a-z]way", "What a way to go"))
% print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
% print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

% print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
% print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

% print(re.search(r"cat|dog", "I like cats."))
% print(re.search(r"cat|dog", "I love dogs!"))
% print(re.search(r"cat|dog", "I like both dogs and cats."))

% print(re.search(r"cat|dog", "I like cats."))
% print(re.search(r"cat|dog", "I love dogs!"))
% print(re.search(r"cat|dog", "I like both dogs and cats."))
% print(re.findall(r"cat|dog", "I like both dogs and cats."))

# Repetition Qualifiers
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))
```

- Character classes : written insided square brackets
- To match any characters that aren't in a group use caret sign inside square brackets like this [^a-z]
- To match either we use a pipe symbol like this `cat|dog`
- `.*` means it matches any character repeated as many times as possible including zero. This behavior in programming
  terms is called as greedy.
- `+` matches one or more occurrences of the character that comes before it
- `?` either zero or one occurrence of the character before it
- Escape character :
- `\.` matches dot in the string
- When we see a pattern that includes a backslash, it could be escaping a special regex character or a special string
  character
- `\w` matches any alphanumeric character including numbers, letters, and underscores
- `\d` for matching digits
- `\s` for matching white space characters like space, tab or new line
- `\b` for word boundaries and few others
- Regular Expressions in Action, Examples:
    - `r”\d{3}-\d{3}-\d{4}”` :matches U.S. phone numbers in the format 111-222-3333
    - `r”^-?\d*(\.\d+)?$”`  :matches any positive or negative number, with or without decimal places
    - `r”^/(.+)/([^/]+)/$”` :is often used to extract specific parts of URLs or file paths, such as the directory names
      or filenames

### Advanced Regular Expressions

- Capturing Groups : are portions of the pattern that are enclosed in parentheses
- result.group() method returns a tuple, can access elements by indexing
- first(0) index being the whole string followed by each element in the group
- More on Repetition qualifiers
- Extracting a PID using regexes in Python
- Splitting and Replacing

## MODULE 4

### Data Streams

- Standard streams : IO streams (input-output)
    - STDIN :
        - input('...') for python3 and raw_input('...') for python 2
        - raw_input will just get a string from a user,
        - on the other hand input will actually perform basic maths on calling eval()
        - eval() is used to evaluate string expressions
    - STDOUT
    - STDERR
- Environment variables :
    - variables set in environment(shell command-line environment)
    - source of information saved in environment to use in the scripts
- Shell : a command-line interface used to interact with your operating system
    - bash (commonly used shell)
    - zsh
    - fish
- Check environmental variables from command-line prompt
    - env : returns all the environmental variables in the system
    - echo $PATH : returns all the paths stored
        - echo is a command to print text in linux
        - $ is prefixed to name of the variable to access its value
- Command-line arguments:
    - parameters passed to a program when it's started
    - these are useful for system administration tasks
    - cmd-line arguments are stored in sys module
    - each parameter is saved as separate element in a list
- Exit status / Return code:
    - value returned by a program to the shell in unix like OS
    - 0 : when process succeeds
    - echo $? : return the exit status
    - wc <filename> : returns lines, word & characters in the file

### Python Subprocesses

- Subprocesses are a way to call and run other applications from within Python, including other Python scripts
- Running system commands in Python
    - subprocess : run a system program from python script using functions provided
        - runt() : receives list of commands followed by other parameters
- Obtaining the output of a system command
- Advanced subprocess management
    - os.environ.copy() : copy env vars in dictionary to store and prepare for new environment
    - os.pathsep.join() : joins two elements of the path with respect to underlying OS
    - cwd : current working directory
    - evn : environment variable
- If we're automating a one-off, well-defined task, we're developing a solution quickly is the biggest requirement,
  then using system commands and subprocesses can help a lot. But if we're doing something more complex or long-running,
  it's usually a good idea to use the baked-in or external modules that Python provides
- So before deciding to use a sub-process, it's a good idea to check the standard library or pypi repository to see if
  we can do the task with native Python and to check if someone has already created the automation that we wanted to
  write
- Subprocess is best used when you need to
    - interface with external processes,
    - run complex shell commands, or
    - need precise control over input and output.
- Subprocess also spawns fewer processes per task than OS, so subprocess can use less compute power
- Subprocess can run any shell command, providing greater flexibility
- Subprocess can capture stdout and stderr easily

vs OS

- On the other hand, OS is useful for basic file and directory operations, environment variable management, and when you
  don't need the object-oriented approach provided by Pathlib.
- OS provides a simple way to interface with the operating system for basic operations
- OS is part of the standard library, so it's widely available.

vs Pathlib

- Pathlib is most helpful for working extensively with file paths, when you want an object-oriented and intuitive way to
  handle file system tasks, or when you're working on code where readability and maintainability are crucial.
- Pathlib provides an object-oriented approach to handle file system paths.
- Compared to OS, Pathlib is more intuitive for file and directory operations.
- Pathlib is more readable for path manipulations

- run() :
    - simplest way to run a command
    - recommended approach to invoking subprocesses
    - It runs the command, waits for it to complete, then returns a CompletedProcess instance that contains information
      about the process
- Popen() : most fully featured way to call external commands
    - lot more powerful when spawning parallel processes or communicating between subprocesses,
    - all 4 others are wrappers around this class
    - very useful when you need asynchronous behavior and the ability to pipe information between a subprocess and the
      Python program that ran that subprocess.
- call()
- check_call() :
    - similar to call()
    - receive just the status of a command
    - raises a CalledProcessError exception if the command returns a non-zero exit code
- check_output() : receive the status of a command and also obtain output

### Processing Log Files

- Log files :
    - kind of data you can find in Syslog file or a web request log
    - Log files contain a lot of useful information, particularly when you're trying to debug a tricky problem that's
      happening on a computer
    - Using regex's in our scripts gives us a great deal of flexibility when processing log files and other text data
      sources too
- Filtering log files with regex :
    - regex expressions
- Making sense out of the data :
    - dictionaries are great structures to store data

### Qwiklab Assignment:

Imagine one of your colleagues is struggling with a program that **keeps throwing an error**. Unfortunately, the
program's source code is too complicated to easily find the error there. The good news is that the program outputs a 
**log file** you can read! Let's write a script to **search the log file for the exact error**, then **output that error
into a separate file** so you can work out what's wrong.

**What you'll do**

1. Write a script to search the log file using regex to find for the exact error.
2. Report the error into a separate file so you know what's wrong for further analysis.

## MODULE 5

### Simple Tests

- Software Testing : a process of evaluating computer code to determine whether it does what you expect it to do
- Scripts and programs can fail in all sorts of strange ways, especially as it becomes more complicated
- Writing tests can help you eliminate a bunch of bugs, helping to improve the reliability and the quality of automation
- Tests can help make good code great
- Fundamentals:
    - Manual testing
        - The most basic way of testing a script is to run it with different parameters and see if it returns the
          expected values
        - Using the interpreter to try our code before putting it in a script is another form of manual testing.
        - Ex: Executing a script with different command-line arguments to see how its behavior changed
    - Automated testing
        - Codifying tests into its own software and code that can be run to verify that our programs do what we expect
          them to do. This is called automatic testing
        - The goal of automatic testing is to automate the process of checking if the returned value matches the
          expectations
        - Test cases :
            - You ought to verify that test code behaves the way you expect it to have as many possible values known as
              test cases
        - The more test cases that you include in your test, the better tested your code is and the more you can
          guarantee that your code does what you expect it to do
        - Advantages :
            - we can run them as many times as necessary and will always get the same results
        - Types of automatic test:
            - Unit testing
    - Unit Tests
        - These tests can be run on individual components or by isolating units of code to ensure their correctness
        - Can help in identifying and fix any bugs that appear, creating a more reliable code
        - Concepts relied on :
            - Test fixture :
                - preparation to perform one or more tests
                - involve creating temporary or proxy databases, directories, or starting a server process
            - Test case :
                - individual unit of testing that looks for a specific response to a set of inputs
                - TestCase is a base class provided by unittest and can be used to create new test cases
            - Test suite :
                - a collection of test cases, test suites, or a combination of both
                - used to compile tests that should be executed together
            - Test runner :
                - runs the test and provides developers with the outcome’s data
                - use different interfaces, like graphical or textual, to provide the developer with the test results
                - provide a special value to developers to communicate the test results
        - Unit test is a class based
    - Integration Test
    - Test-driven development
- Having good tests for our software can help us catch mistakes, errors, and bugs before we deploy our scripts to
  perform real-world automation tasks

### Unit Tests

- Used to verify that small, isolated parts of a program are correct
- An unittest provides developers with a set of tools to construct and run tests
- These tests can be run on individual components or by isolating units of code to ensure their correctness

### Pytest

- Pytest is a powerful Python testing tool that assists programmers in writing more effective and stable programs
- It helps to simplify the process of writing, organizing and executing tests
- It can be used to write a variety of tests including:
    - integration,
    - end-to-end, and
    - functional tests
- It supports automatic test discovery and generates informative test reports
- Pytests are written with functions that use the operation, assert()
- An assert is a commonly used debugging tool in Python that allows programmers to include sanity checks in their code
- If the condition provided to assert() turns out to be false, it indicates a bug in the code, an exception is raised,
  and halts the program’s execution

```text
def divide(a, b):
    assert b != 0, 'cannot divide by zero'
    return a / b


divide(2, 0)
```

- An AssertionError message is raised informing the programmer that it is not possible to divide a value by zero

**Pytest fixtures**

- Fixtures are used to separate parts of code that only run for tests

#### Key difference between unittest and pytest

- Both unittest and pytest provide developers with tools to create robust and reliable code through different forms of
  tests
- Unittest is a tool that is built directly into Python, while pytest must be imported from outside your script.
- Unittest has the functionality to automatically detect test cases within an application, but it must be called from
  the command line. Pytests are performed automatically using the prefix test_
- Unittests use an object-oriented approach to write tests, while Pytests use a functional approach
- Pytests use built-in assert statements, making tests easier to read and write. On the other hand, unittests provide
  special assert methods like assertEqual() or assertTrue()

#### Edge Case

- Edge cases are inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges of
  input we imagine our programs will typically work with
- Edge cases usually need special handling in scripts in order for the code to continue to behave correctly
- We can handle this edge case by performing a simple check of the result variable before operating with it

#### Assertions

* assertEqual(a, b) : method checks that a == b
* assertNotEqual(a, b) : method checks that a != b
* assertTrue(x) : method checks that bool(x) is True
* assertFalse(x) : method checks that bool(x) is False
* assertIs(a, b) : method checks that `a` is `b`
* assertIsNot(a, b) : method checks that `a` is not `b`
* assertIsNone(x) : method checks that x is None
* assertIsNotNone(x) : method checks that x is not None
* assertIn(a, b) : method checks that `a` in `b`
* assertNotIn(a, b) : method checks that `a` not in `b`
* assertIsInstance(a, b) : method checks that isinstance(a, b)
* assertNotIsInstance(a, b) : method checks that not isinstance(a, b)
* assertRaises : test whether exceptions are raised

#### Test Suites

- Test suites are collections of tests that should be executed together
- Optimization the testing process
    - setUp() :
        - called automatically with every test that’s run to set up code
        - if raises an exception during the test, the unittest framework considers this to be an error and the test
          method is not executed
        - if successful, tearDown() runs even if the test method fails
    - tearDown() :
        - helps clean up after the test has been run
- Taking together a group of tests of one or many kinds is commonly referred to as a test suite.

### Other Test Concepts

- White-box test (clear-box or transparent testing)
    - relies on the test creator's knowledge of the software being tested to construct the test cases
    - helpful because a test writer can use their knowledge of the source code to create tests that cover most of the
      ways that the program behaves
    - If unit tests are run alongside or after the code has been developed, the test cases are made with a knowledge of
      how software works. They are white-box tests
- Black-box test
    - written with an awareness of what the program is supposed to do, its requirements or specifications, but not how
      it does it
    - the software being tested is treated like an opaque box, meaning tester doesn't know the internals of how the
      software works
    - useful because they don't rely on the knowledge of how the system works
    - If the unit tests are created before any code is written based on specifications of what the code is supposed to
      do, they can be considered black-box unit test
- Other test types
    - Integration test
        - verify that the interactions between the different pieces of code in integrated environments are working the
          way we expect them to
        - goal of an integration test is to verify these kinds(boundaries) of interactions and make sure the whole
          system works how you expect it to
        - usually take the individual modules of code that unit tests verify then combine them into a group to test
    - Regression test
        - a variant of unit test
        - usually written as part of a debugging and troubleshooting process to verify that an issue or error has been
          fixed once it's been identified
        - useful part of a test suite because they ensure that the same mistake doesn't happen twice
    - Smoke test (build verification tests)
        - a concept that comes from testing hardware equipment.
        - serve as a kind of sanity check to find major bugs in a program
        - usually run before more refined testing takes place
        - For a web service the smoke test would be to check if there's a service running on the corresponding port
        - For an automation script, the smoke test would be to run it manually with some basic input and check that the
          script finishes successfully
        - Running a piece of software code as-is to see if it runs describes what type of testing
    - Load test
        - verify that the system behaves well when it's under significant load
        - To actually perform these tests will need to generate traffic to our application simulating typical usage of
          the service
        - can be super-helpful when deploying new versions of our applications to verify that performance does not
          degrade
    - Test Driven Development
        - TDD calls for creating the test before writing the code.
        - TDD cycle typically involves first writing a test then running it to make sure it fails

#### More about tests

Check out the following links for more information:

* https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/
* https://landing.google.com/sre/sre-book/chapters/testing-reliability/
* https://testing.googleblog.com/2007/10/performance-testing.html
* https://www.guru99.com/smoke-testing.html
* https://www.guru99.com/exploratory-testing.html
* https://testing.googleblog.com/2008/09/test-first-is-fun_08.html

### Errors and Exceptions

- Types of errors
    - TypeError
    - ValueError
    - IndexError
    - OSError
    - etc...
- An exception is not meant to produce an error, but to bypass it
- The Try-Except concept
    - Code in the except block is only executed if one of the instructions in the try block raises an error of the
      matching
      type
- Raising Errors
- Testing for expected errors
- Handling errors
    - There are several potential issues here:
        - The file might not exist, causing a **FileNotFoundError**.
        - The file might not have enough lines of data, leading to an **IndexError**.
        - The data in the file might not be convertible to integers, raising a **ValueError**.
        - The second number might be zero, which would raise a **ZeroDivisionError**.
    - The errors should read
        - file level issues
        - value error like not enough data in the file
        - error like the file was not found
        - data level issues
        - value error like invalid literal for int() with base 10:'apple'
        - division error like the denominator is zero

#### Terms and definitions from course 2, module 5

- **Automatic testing**: A process where software checks itself for errors and confirms that it works correctly
- **Black-box tests**: A test where there is an awareness of what the program is supposed to do but not how it does it
- **Edge case**s: Inputs to code that produce unexpected results, found at the extreme ends of the ranges of input
- **Pytest**: A powerful Python testing tool that assists programmers in writing more effective and stable programs
- **Software testing**: A process of evaluating computer code to determine whether it does what is expected
- **Test case**: This is the individual unit of testing that looks for a specific response to a set of inputs
- **Test fixture**: This prepared to perform one or more tests
- **Test suite**: This is used to compile tests that should be executed together
- **Test runner**: This runs the test and provides developers with the outcome’s data
- **unittest**: A set of Python tools to construct and run unit tests
- **Unit tests**: A test to verify that small isolated parts of a program work correctly
- **White-box test**: A test where test creator knows how the code works and can write test cases that use the
  understanding to make sure it performs as expected

### Qwiklab Assignment

Imagine one of your IT coworkers just retired and left a folder of scripts for you to use. One of the scripts, called
emails.py, matches users to an email address and lets us easily look them up! For the most part, the script works
great — you enter an employee's name and their email is printed to the screen. But, for some employees, the output
doesn't look quite right. Your job is to add a test to reproduce the bug, make the necessary corrections, and verify
that all the tests pass to make sure the script works! Best of luck!

What you'll do

- Write a simple test to check for basic functionality
- Write a test to check for edge cases
- Correct code with a try/except statement

## MODULE 6

- Input/Output streams to files or even to other programs
- Bash is a programming language
- Bash commands are more readable and a lot easier to maintain

### Interacting with command-line shell

- Basic Linux Commands

```text
echo 'Hello World!'
mkdir my_new_dir
cd my_new_dir/
/my_new_dir$ pwd
/my_new_dir$ cp ../spider.txt .
/my_new_dir$ touch my_file.txt
/my_new_dir$ ls -l
/my_new_dir$ ls -la
/my_new_dir$ mv my_file.txt emptyfile.txt
/my_new_dir$ cp spider.txt yet_another_file.txt
/my_new_dir$ ls -l
/my_new_dir$ rm *
/my_new_dir$ ls -l
/my_new_dir$ cd ..
rmdir my_new_dir/
ls my_new_dir

# Managing files and directories:
mv file1.txt file2.txt file3.txt dir1/ # This command moves multiple files
cp file1.txt file2.txt file3.txt dir1/ # This command copies multiple files
# chmod/chown/chgrp is used to make a file readable to everyone on the system before moving it to a public director
chmod +r file.html && mv file.html /var/www/html/index.html 
# cut is a command that extracts fields from a data file
cut -f1 -d”,” addressbook.csv # This command extracts the first field from a .csv file
cut -c1-3,5-7,9-12 phones.txt # This command extracts only the digits from a list of phone numbers
# sort is a command that sorts the contents of a file. Some examples include:
sort names.txt # This command sorts inputs alphabetically
sort -r names.txt # This command sorts inputs in reverse alphabetical order, starting with the letter z 
sort -n numbers.txt # This command treats the inputs as numbers and then sorts them numerically
ls -l | cut -w -f5,9 | sort -rn | head -10 # This command displays the 10 largest files in the current directory
cut -f1-2 -d”,” addressbook.csv | sort # This command extracts the first and last names from a .csv file and sorts them

# Additional commands:
id # command that prints information about the current user
free # is a command that prints information about memory on the current system
#free -h: Display memory sizes in human-readable format.
#free -s [delay]: Repeat the command with a specified delay between updates.
#free -b: Display memory sizes in bytes.
#free -k: Display memory sizes in kilobytes.
#free -m: Display memory sizes in megabytes.
#free -g: Display memory sizes in gigabytes.
```

- Redirecting streams
    - redirection is a process sending a stream to a different destination
    - each time we perform of redirection of STD out, the destination is overwritten
    - If we want to append the redirected standard out to a file we can use the double greater than sign instead of
      single greater than
    - redirect standard input sending data into a program by using the less than symbol to read the contents of a file

```text
cat stdout_example.py
./stdout_example.py 
./stdout_example.py > new_file.txt
cat new_file.txt 
./stdout_example.py >> new_file.txt
cat new_file.txt
cat streams_err.py 
./streams_err.py < new_file.txt
./streams_err.py < new_file.txt 2> error_file.txt
cat error_file.txt
echo "These are the contents of the file" > my_amazing_file.txt
cat my_amazing_file.txt
#command > file: redirects standard output, overwrites file
#command >> file: redirects standard output, appends to file
#command < file: redirects standard input from file
#command 2> file: redirects standard error to file
```

- Pipes and pipelines
    - Another powerful way of performing IO stream redirection called Piping
    - Using pipes, you can connect multiple scripts, commands, or other programs together into a data processing
      pipeline
    - Pipes connect the output of one program to the input of another in order to pass the data between programs
    - Pipes are represented by the pipe character
    - Allows us to create new commands by combining the functionality of one command, with the functionality of another
      without having to store the contents in an intermediate file
    - You can use your Python scripts and pipelines too

```text
ls -l | less
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head 
# tr - translate/transform ' ' to '\n'
# sort - sorts the then results alphabetically, -nr flag, sorts numerically and in reverse order
# uniq - which displays each match once and by using a -c flag, it prefixes each unique line with a number of times it occurred
# head - prints first 10 lines to stdl
cat capitalize.py
cat haiku.txt
cat haiku.txt | ./capitalize.py
./capitalize.py < haiku.txt
#command1 | command2: connects the output of command1 to the input of command2
```

- Signaling processes
    - Signals are tokens delivered to running processes to indicate a desired action
    - Using signals, we can
        - tell a program that we want it to pause or terminate,
        - to reload its configuration, or
        - to close all open files.
    - Since Kill is a separate program, we need to run it on a separate terminal, and we also need to know the process
      identifier or PID of the process
    - Depending on what options that we pass, `ps` command will show different subsets of processes with different
      amounts of detail
        - with `ax` : lists all the running process in the current computer

```text
ping www.google.com
Ctrl-c # sends SIGINT signal # process does whatever it needs to finish cleanly
Ctrl-Z # sends SIGSTOP signal # causes the program to stop running without actually terminating
fg # process stopped by SIGSTOP can be run again by this command
kill # sends SIGTERM signal # terminates the program
ps # list the currently running processes
```

```text
# run ping on one terminal
ping www.google.com
PING www.google.com (142.251.42.100): 56 data bytes
64 bytes from 142.251.42.100: icmp_seq=0 ttl=53 time=33.239 ms
64 bytes from 142.251.42.100: icmp_seq=1 ttl=53 time=34.095 ms
64 bytes from 142.251.42.100: icmp_seq=2 ttl=53 time=33.931 ms
64 bytes from 142.251.42.100: icmp_seq=3 ttl=53 time=34.123 ms
...
zsh: terminated  ping www.google.com
```

```text
# find its PID and kill it in another terminal
ps ax | grep ping
44655 s001  S+     0:00.01 ping www.google.com
44659 s002  R+     0:00.00 grep ping
kill 44655
```

```text
$ ps  # : lists the processes executing in the current terminal for the current user
$ ps ax # : lists all processes currently executing for all users  
$ ps e  # : shows the environment for the processes listed  
$ kill PID  # : sends the SIGTERM signal to the process identified by PID
$ fg  # : causes a job that was stopped or in the background to return to the foreground
$ bg  # : causes a job that was stopped to go to the background
$ jobs  # : lists the jobs currently running or stopped
$ top # : shows the processes currently using the most CPU time (press "q" to quit)  
```

### Bash scripting

- Creating Bash scripts
- Using Variables and Globs
    - variables
        - variable initialization should be like `example=hello world` without space around `=`
        - to access a variable prefix $ before variable name
    - globs
        - globs are characters that allow us to create lists of files
        - `*` and `?` are the most common globs
        - globs lets us create sequences of filenames that we can use as parameters to the commands we call in our
          script

```text
echo *.py # all files with  filenames ending .py
echo c* # all files starting with letter `c`
echo * # all files 
echo ????.py # .py files with 4 characters resembling `?`
```

- Conditional execution in Bash
    - In bash scripting, the condition used is based on the exit status of commands
    - In bash scripting, the exit value of 0 means success
    - `test` is a command that evaluates the conditions received and exits with zero when they're true and with one when
      they're false
    - alias to `test` command is `[ <condition> ]` with spaces at start and end of condition
- Bash scripting resources

### Advanced Bash concepts

- While loops in Bash scripts
- For loops in Bash scripts
- Advanced command interaction
    - `tail` and `cat` are almost similarly command printing the content of the file
    - `tail` prints last lines

```text
tail sample.txt
tail sample.txt | cut -d' ' -f5-
cut -d' ' -f5- sample.txt | sort | uniq -c | sort -nr | head
# -d' ' : delimiter as space 
```

- Choosing between Bash and Python
    - Sometimes bash script is unreadable, that is better done in python script
    - Good idea to use bash for system commands and file operations than python
    - Bash is platform dependent

### Glossary

**Terms and definitions from Course 2, Module 6**

* Bash script: A script that contains multiple commands
* Cut: A command that can split and take only bits of each line using spaces
* Globs: Characters that create list of files, like the star and question mark
* Pipes: A process of connecting the output of one program to the input of another
* Piping: A process of connecting multiple scripts, commands, or other programs together into a data processing pipeline
* Redirection: A process of sending a stream to a different destination
* Signals: Tokens delivered to running processes to indicate a desired action

### Qwiklab Assignment

In this lab, you'll change the username of your coworker Jane Doe from "jane" to "jdoe" in compliance with company's
naming policy. The username change has already been done. However, some files that were named with Jane's previous
username "jane" haven't been updated yet. To help with this, you'll write a bash script and a Python script that will
take care of the necessary rename operations.

**What you'll do**

1. Practice using the cat, grep, and cut commands for file operations
2. Use > and >> commands to redirect I/O stream
3. Replace a substring using Python
4. Run bash commands in Python

**Prerequisites**

- cat
- grep : grep [pattern] (file-directory/file-location)
- cut : cut [options] (file) ; cut -d [delimiter] -f [field number]

**Linux I/O Redirection**

- Redirection into a file using >
- Append using >>

**Redirection into a file**

- cat > [file]
- cat >> [file]

### IT skills in action reading

In this reading, you will review an example of how regular expressions are used in the real world.

**Disclaimer**: The following scenario is based on a fictitious company called LogicLink Innovations.

**Time is ticking**
Dakota is a fairly new programmer with his company. He just earned a spot on the project for LogicLink Innovations. This
is one of the biggest and most credible companies in the industry, so Dakota knows he has to excel on this project to
help make a name for himself. LogicLink Innovations manages customer data and has hundreds of customer phone numbers in
its database. The phone numbers are in inconsistent formats. Some are written with dashes, some in parentheses with
spaces, and some are just digits. Dakota sees this:

123-456-7890
(123) 456-7890
1234567890

Dakota is assigned to take the dataset containing phone numbers and organize the formatting so they are all consistent.
His manager tells him they need it by the end of the week! There is no way Dakota can work through and edit hundreds of
phone numbers. There has to be another way.

**Search and replace**
Dakota remembers reading about how other programmers use regular expressions to make their coding life easier. He knows
there has to be one that can help him with his dilemma. This can’t be the first time a programmer needs to standardize
numbers! He decides to craft a regular expression that captures three groups of digits, each of which might be
surrounded by non-digit characters.

Using a regex tool and the sample data from above, he eventually comes up with a regex that matches all three samples:
**^\D*(\d{3})\D*(\d{3})\D*(\d{4})$**

Let’s break down this line of code, piece by piece:

* ^\D*    : This part of the code matches zero or more non-digit characters at the beginning of the string.
* (\d{3}) : This part of the code captures exactly three digits, which represent the area code.
* \D* : This part of the code matches zero or more non-digit characters between the area code and exchange.
* (\d{3} )    : This part of the code captures the three-digit exchange.
* \D* : This part of the code matches zero or more non-digit characters between the exchange and line.
* (\d{4})$    : This part of the code captures exactly four digits at the end of the string.

Now he has three capture groups: area code, exchange, and number. He then substitutes those groups into a new string
using backreferences:
**(\1) \2-\3**

This puts all the phone numbers into a uniform format.

This regular expression helps Dakota by searching for phone numbers in different formats and replacing them to match the
format that Dakota’s manager needs: (123) 456-7890. Dakota begins to code.

He writes up a simple Python script to read the dataset from a file and output the corrected phone numbers using his
regular expressions:

```text
import re

with open("data/phones.csv", "r") as phones:
    for phone in phones:
        new_phone = re.sub(r"^\D*(\d{3})\D*(\d{3})\D*(\d{4})$", r"(\1) \2-\3", phone)
        print(new_phone)
```

```text
    (123) 456-7890
    (123) 456-7890
    (123) 456-7890
```

Success! Dakota gets the project done in a single day and is now the office hero.

## MODULE 7

### Getting ready for the final project

- Introduction
- Writing script from ground up
    - Steps for coding projects
        1. Understand the problem statement
            - what needs to be done
            - identifying the given inputs and desired outputs
        2. Research
            - how to tackle the problem
            - tools provided by python library
            - documentation of modules, classes and functions and understanding how to apply
        3. Planning
            - what data types are useful
            - order of operations
            - how all pieces come together to give our solution
            - Synergy : If the problem is complex, it might help to write down the plan for quick reference, either on a
              piece of paper or in a digital document
        4. Writing script
            - writing and checking the code
            - manual testing, automatic testing
- Project problem statement
    - Write some automation scripts that will process the system log and generate a bunch of reports based on the
      information extracted from log files. The log lines follow a pattern similar to the ones we've seen before.
    - When the service runs correctly, it logs an info message to syslog, stating what it's done, the username, and the
      ticket number related to the event
    - If the service encounters a problem, it logs an error message to the syslog, indicating what was wrong and the
      username that triggered the action that caused the problem
    - The developers of the service want two different reports out of this data.
        - The first one is a ranking of errors generated by the system. This means a list of all error messages logged,
          and how many times each of them was found, not taking into account the users involved. They should be sorted
          by the most common error to the least common error.
        - The second one is a usage statistics for the service. This means, a list of all users that have used the
          system
          including how many info messages and how many error messages they've generated.
    - This report should be sorted by username.
    - To visualize the data in these reports, you want to generate a couple of webpages that'll be served by a web
      server running on the machine. To do this, you can make use of a script that's already in the system called csv_
      to_html.py. This script converts the data in a CSV file into an HTML file containing a table with the data
    - Then, put the files in the directory that's used by the webserver to display the web pages. The goal is to have
      one script that can get all the necessary work done automatically, every day without any user interaction.
    - This script doesn't need to do all the work itself. It can call on other scripts to do individual tasks and then
      put the results together. In fact, we recommend splitting the task so that each piece can be written and tested
      separately. I imagine that your mind is racing, your pulse might have spread up a little bit, and your palms are
      sweating all over the keyboard. Don't worry. This might sound like a lot of work. But once you've understood the
      problem and done some research and planning, everything will start to fall into place
- Help with Research and Planning
    - for specific log lines use regex (www.regex101.com) and create a pattern
    - count how many errors of same type of errors, use dictionaries for this
    - then sort different criteria
    - output is the couple of csv files
    - then call csv_to_html.py file pass parameters to it either by python / bash, recommended bash
- Qwiklab assessment

  Imagine your company uses a server that runs a service called `ticky`, an internal ticketing system. The service logs
  events to syslog, both when it runs successfully and when it encounters errors.

  The service's developers need your help getting some information from those logs so that they can better understand
  how
  their software is used and how to improve it. So, for this lab, you'll write some automation scripts that will process
  the system log and generate reports based on the information extracted from the log files.

  **What you'll do**
    - Use regex to parse a log file
    - Append and modify values in a dictionary
    - Write to a file in CSV format
    - Move files to the appropriate directory for use with the CSV->HTML converter

- Log analysis using regular expressions
- Graded Assessment

### Job searching and Professional Networking

- Build a job search plan
- What is your career identity?
- Personal Branding
- Get started with LinkedIn
- Recruiters, Headhunters and Staffing Agencies

### Course warp-up

- Reflect and connect using peers