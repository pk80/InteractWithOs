import re


def secure_website_domain(website):
    pattern = r'^(https://www.)(.*?)(.com|.co)'  # enter the regex pattern here
    result = re.search(pattern, website)  # enter the re method here
    if result is None:
        return ""

    return result.groups()  # enter the correct capturing group


# print(secure_website_domain("http://www.text.com"))  # Should return nothing
# print(secure_website_domain("https://www.text.com"))  # Should return text
# print(secure_website_domain("http://www.text.co"))  # Should return nothing
# print(secure_website_domain("https://www.text.co"))  # Should return text


def parse_city_country(text):
    pattern = r'[,|\.]'  # enter the regex pattern here
    result = re.split(pattern, text)  # enter the re method  here
    if len(result) != 2:
        return ""
    return result[0]  # return the correct capturing group


# print(parse_city_country("Paris, France"))  # should return Paris
# print(parse_city_country("Mumbai, India"))  # should return Mumbai
# print(parse_city_country("Rio de Janeiro. Brazil"))  # should return Rio de Janeiro
# print(parse_city_country("Tokyo! Japan"))  # result should be blank

def find_isbn(list):
    # pattern = r'(\b\d{6}+\b)'  # enter the regex pattern here
    pattern = r'^(\b\d{3,3}+\b)-(\b\d{1,1}+\b)-(\b\d{2,2}+\b)-(\b\d{6,6}+\b)-(\b\d{1,1}+\b)$'  # enter the regex pattern here
    result = re.search(pattern, list)  # enter the re method  here
    if result is None:
        return ""
    return result[4]  # return the correct capturing group
# Incorrect
# Not quite! Review the videos More on repetition qualifiers
# and Extracting a PID using regexes in Python.
print('*'*20)
print(find_isbn("123-4-12-098754-0"))  # Should return 098754
print(find_isbn("223094-AB-30-2"))  # result should be blank
print(find_isbn("1123-4-12-098754-0"))  # result should be blank
