# Regular Expressions
import csv
import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(index)
print(log[index + 1:index + 6])

regex = r"\[(\d+)\]"
result = re.search(pattern=regex, string=log)
print(result, ':', type(result))
print(result[1])

mystring = 'plaza, bazaar, maze, xenon, penguin, clapping, sponge, Pangaea'
result = re.search(r"aza", mystring)
print('aza :', result)
result = re.search(r"^p", mystring)
print('^p :', result)
result = re.search(r"ea$", mystring)
print('ea$ :', result)
result = re.search(r"p.ng", mystring, re.IGNORECASE)
print('p.ng :', result)
result = re.search(r"l.ng", mystring, re.IGNORECASE)
print('l.ng :', result)

# Wildcards and Character classes
print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

# Repetition Qualifiers / repeated matches
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

# Escaping Characters
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

# Regular Expressions in Action
print('Regular Expressions in Action')
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

"""
Fill in the code to check if the text passed looks like a standard sentence, 
meaning that it starts with an uppercase letter, followed by at least 
some lowercase letters or a space, and ends with a period, question mark, 
or exclamation point. 
"""


def check_sentence(text):
    result = re.search(r"^[A-Z][a-z|0-9| ]*[.|?|!]$", text)
    return result is not None


print(check_sentence("Is this is a sentence?"))  # True
print(check_sentence("is this is a sentence?"))  # False
print(check_sentence("Hello"))  # False
print(check_sentence("1-2-3-GO!"))  # False
print(check_sentence("A star is born."))  # True

# Complex expressions
pattern1 = r"\d{3}-\d{3}-\d{4}"
print(re.search(pattern1, '112-222-3333'))
pattern2 = r"^-?\d*(\.\d+)?$"
print(re.search(pattern2, "5111111.111112"))
pattern3 = r"^/(.+)/([^/]+)/$"
print(re.search(pattern3, "/my.regex/__init__.py"))

"""
Question 1
The check_web_address() function checks if the text passed qualifies 
as a top-level web address, meaning that it contains alphanumeric 
characters (which includes letters, numbers, and underscores), 
as well as periods, dashes, and a plus sign, followed by a period and 
a character-only top-level domain such as ".com", ".info", ".edu", etc. 
Fill in the regular expression to do that, using escape characters, 
wildcards, repetition qualifiers, beginning and end-of-line characters, 
and character classes.
"""


def check_web_address(text):
    pattern = r"[a-zA-Z0-9_\.\-\+]*\.[a-zA-Z]*$"
    result = re.search(pattern, text)
    return result != None


print('Question 1 :')
print(check_web_address("gmail.com"))  # True
print(check_web_address("www@google"))  # False
print(check_web_address("www.Coursera.org"))  # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True

"""
Question 2
The check_time() function checks for the time format of a 12-hour clock, as follows: 
the hour is between 1 and 12, with no leading zero, followed by a colon, 
then minutes between 00 and 59, then an optional space, and then AM or PM, 
in upper or lower case. Fill in the regular expression to do that. 
How many of the concepts that you just learned can you use here?
"""


def check_time(text):
    pattern = r"^(1[0-2]|0?[1-9]):[0-5][0-9]\s?[a|A|p|P][m|M]$"
    result = re.search(pattern, text)
    return result != None


print('Question 2 :')
print(check_time("12:45pm"))  # True
print(check_time("9:59 AM"))  # True
print(check_time("6:60am"))  # False
print(check_time("five o'clock"))  # False
print(check_time("6:02 am"))  # True
print(check_time("6:02km"))  # False

"""
Question 3
The contains_acronym() function checks the text for the presence of 2 or more 
characters or digits surrounded by parentheses, with at least the first character 
in uppercase (if it's a letter), returning True if the condition is met, 
or False otherwise. 
For example, "Instant messaging (IM) is a set of communication technologies 
used for text-based communication" should return True since (IM) satisfies 
the match conditions." Fill in the regular expression in this function: 
"""


def contains_acronym(text):
    pattern = r"\([A-Z0-9][a-zA-Z]*\)"
    result = re.search(pattern, text)
    return result != None


print('Question 3 :')
print(contains_acronym(
    "Instant messaging (IM) is a set of communication technologies used for text-based communication"))  # True
print(contains_acronym(
    "American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication"))  # True
print(contains_acronym("Please do NOT enter without permission!"))  # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)"))  # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!"))  # True

"""
Question 6
An intern implemented a zip code checker, but it works only with five-digit zip codes. 
Your task is to update the checker so that it includes all nine digits of the zip code; 
the leading five digits and the optional four after the hyphen. The zip code needs to 
be preceded by at least one space, and cannot be at the start of the text. 
Update the regular expression.
Note: Are you checking for exactly 5 digits, and which
characters can precede and follow the zip code?
"""


def check_zip_code(text):
    result = re.search(r" ?\b\d{5,5}\b(-?\b\d{4,4}\b)?", text)
    return result != None


print('Question 6 :')
print(check_zip_code("The zip codes for New York are 1000100 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # True
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-000100."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False

# Capturing Groups
print('*********** Advanced Regular Expression ***********')
print('Capturing groups :')
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
print("{} {}".format(result[2], result[1]))


def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


def rearrange_name_2(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])


print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name_2("Hopper, Grace M."))

# More on Repetition qualifiers
print('************** More on Repetition Qualifiers **************')
print(re.search(r'[a-zA-Z]{5}', "a ghost"))
print(re.search(r'[a-zA-Z]{5}', "a scary ghost appeared"))
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
print(re.findall(r"\w{5,10}", "I really like strawberries"))
print(re.findall(r"\w{5,}", "I really like strawberries"))
print(re.findall(r"s\w{,20}", "I really like strawberries"))

# Extracting a PID using regexes in Python
print('************** Extracting a PID using regexes in Python **************')
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

# regex = r"\[(\b\d{5}\b)\]"
result = re.findall(regex, "A completely different string [12378] that also has numbers [34567]")
print(result)
print(result[0])
print(result[1])

result = re.search(regex, "99 elephants in a [cage]")
print(result)


def extract_pid(text):
    ep_pattern = r"\[(\d+)\]"
    ep_result = re.search(ep_pattern, text)
    if ep_result is None:
        return text
    return ep_result[1]


print(extract_pid(log))

"""
Add to the regular expression used in the extract_pid function, 
to return the uppercase message in parenthesis, after the process id.
"""


def extract_pid_q(log_line):
    regex = r"\b\[(\d+)\]+[:\s]+([A-Z]*)\b"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])


print(
    extract_pid_q("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))  # 12345 (ERROR)
print(extract_pid_q("99 elephants in a [cage]"))  # None
print(extract_pid_q("A string that also has numbers [34567] but no uppercase message"))  # None
print(extract_pid_q("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))  # 67890 (RUNNING)

# Splitting and Replacing
print('************** Splitting and Replacing **************')
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))
print(re.split(r"the|a", "One sentence. Another one? And the last one!"))

# Practice Advanced Regular Expressions
print('************** Practice Advanced Regular Expressions **************')
print(re.search(r'(Test\d)-(?=Passed)', 'Test1-Passed, Test2-Passed, Test3-Failed, Test4-Passed, Test5-Failed'))
print(re.findall(r'(Test\d)-(?=Passed)', 'Test1-Passed, Test2-Passed, Test3-Failed, Test4-Passed, Test5-Failed'))


# Question 1
# You’re working with a CSV file that contains employee information.
# Each record has a name field, followed by a phone number field,
# and a role field. The phone number field contains U.S. phone numbers
# and needs to be modified to the international format, with +1-
# in front of the phone number. The rest of the phone number should
# not change. Fill in the regular expression, using groups, to use
# the transform_record() function to do that.
def transform_record(record):
    # new_record = re.sub(___)
    new_record = re.sub(r"(\w*)+(\d{3}-.*)+(\w*)", r"\1+1-\2\3", record)
    return new_record


print('Question 1:')
print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator
print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist
print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer
print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))  # Charlie Rivera,+1-698-746-3357,Web Developer


# Question 2
# The multi_vowel_words() function returns all words
# with 3 or more consecutive vowels (a, e, i, o, u).
# Fill in the regular expression to do that.
def multi_vowel_words(text):
    pattern = r"\w*[aeiou]{3,}\w*"
    result = re.findall(pattern, text)
    return result


print('Question 2:')
print(multi_vowel_words("Life is beautiful"))  # ['beautiful']
print(multi_vowel_words(
    "Obviously, the queen is courageous and gracious."))  # ['Obviously', 'queen', 'courageous', 'gracious']
print(multi_vowel_words(
    "The rambunctious children had to sit quietly and await their delicious dinner."))  # ['rambunctious', 'quietly', 'delicious']
print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))  # ['queue']
print(multi_vowel_words("Hello world!"))  # []


# Question 4
# The transform_comments() function converts comments in a Python script
# into those usable by a C compiler. This means looking for text that
# begins with a hash mark (#) and replacing it with double slashes (//),
# which is the C single-line comment indicator. For the purpose of
# this exercise, we'll ignore the possibility of a hash mark embedded
# inside of a Python command, and assume that it's only used to indicate
# a comment.
# We also want to treat repetitive hash marks (##), (###), etc.,
# as a single comment indicator, to be replaced with just (//)
# and not (#//) or (//#). Fill in the parameters of the substitution
# method to complete this function:
def transform_comments(line_of_code):
    result = re.sub(r'#+', r'//', line_of_code)
    return result


print('Question 4:')
print(transform_comments("### Start of program"))
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable"))
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable"))
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)"))  # Should be "  return(number)"


# Question 5
# The convert_phone_number() function checks for a U.S. phone number
# format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits
# followed by a dash, and 4 digits), and converts it to a more formal
# format that looks like this: (XXX) XXX-XXXX. Fill in the regular
# expression to complete this function.
def convert_phone_number(phone):
    result = re.sub(r'\s(\d{3})-', r' (\1) ', phone)
    return result


print('Question 5:')
print(convert_phone_number("My number is 212-345-9999."))  # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234"))  # Please call (888) 555-1234
print(convert_phone_number("123-123-12345"))  # 123-123-12345
print(convert_phone_number(
    "Phone number of Buckingham Palace is +44 303 123 7300"))  # Phone number of Buckingham Palace is +44 303 123 7300

"""
# LAB WORK :
# What you'll do
#     - Replacing the old domain name (abc.edu) with a new domain name (xyz.edu).
#     - Storing all domain names, including the updated ones, in a new file.
/data/user_emails.csv
/scripts/script.py
AIM: 
The aim of the script is to use regex to find all instances of the old domain ("abc.edu") 
in the user_emails.csv file and then replace them with the new domain ("xyz.edu").

Update file permissions : sudo chmod 777 script.py
"""


def contains_domain(address, domain):
    """This function uses regex to identify the domain of the user email addresses in the user_emails.csv file.
    Its primary objective is to check whether an email address belongs to the old domain(abc.edu)"""
    domain_regex = r'[\w\.-]+@' + domain + '$'
    if re.match(domain_regex, address):
        return True
    return False


def replace_domain(address, old_domain, new_domain):
    """The replace_domain function takes in one email address at a time, as well as the email's old domain name and its new domain name.
    This function's primary objective is to replace the email addresses containing the old domain name with new domain name"""
    old_domain_regex = r'' + old_domain + '$'
    address = re.sub(old_domain_regex, new_domain, address)
    return address


def update_csv(csv_file, report_file, old_domain, new_domain):
    old_domain_email_list, new_domain_email_list = [], []
    with open(csv_file, 'r') as file:
        records = list(csv.reader(file))
        user_email_list = [data[1].strip() for data in records[1:]]
        for each in user_email_list:
            if contains_domain(each, old_domain):
                old_domain_email_list.append(each)
                replaced = replace_domain(each, old_domain, new_domain)
                new_domain_email_list.append(replaced)

        email_key = ' ' + 'Email Address'
        email_index = records[0].index(email_key)
        for user in records[1:]:
            for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
                if user[email_index] == ' ' + old_domain:
                    user[email_index] = ' ' + new_domain

        file.close()
    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(records)
        output_file.close()
    print('csv file update is complete')
