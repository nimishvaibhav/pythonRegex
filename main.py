import re

#   To search the starting character of a string
def regex_string_match(string):
    pattern = re.compile(r'N[a-z]+')
    matches = pattern.match(string)
    print(matches)


def regex_string_search(string):
    pattern = re.compile(r'N[a-z]+')
    matches = pattern.search(string)
    print(matches)


def regex_string_findall(string):
    pattern = re.compile(r'N[a-z]+')
    matches = pattern.findall(string)
    print(matches)


def regex_string_finditer(string):
    pattern = re.compile(r'N[a-z]+')
    matches = pattern.finditer(string)
    #print(matches)

    for match in matches:
        print(match)


def regex_find_phone_number(string):
    # 222-333-4444 -- Phone Number
    # pattern = re.compile(r'[0-9]{3}\-[0-9]{3}\-[0-9]{4}')
    pattern = re.compile(r'([0-9]{3}\-){2}([0-9]{4})')
    matches = pattern.match(string)
    print(matches)


def regex_find_phone_number2(string):
    # 7033217654, (703)3217654, (703) 321 7654, 703.321.7654.  (703)-321-7654, 703-321-7654
    pattern = re.compile(r'(\d{3}|\(\d{3}\))(:?\s+|-|\.)?(\d{3})(:?\s+|-|\.)?(\d{4})')
    matches = pattern.finditer(string)

    for match in matches:
        print(match)



def regex_find_emailid(string):
    # nimishvaibhav.p@gmail.com, nimishvaibhav_p@outlook.com, nimishvaibhav1992@yahoo.coom, 1992nimishvaibhav@hotmail.com
    pattern = re.compile(r'\b[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]+\b')
    matches = pattern.finditer(string)
    #print(matches)

    for match in matches:
        print(match)


def regex_find_ipaddr(string):
    # 255.255.255.255, 1.2.3.4, 11.33.55.77, 149.156.186.192, 249.34.86.100
    # pattern = re.compile(r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])')
    pattern = re.compile(r'((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])')
    matches = pattern.search(string)
    print(matches)


if __name__ == '__main__':
    regex_string_match('Nimish Vaibhav')
    regex_string_match('How are you Nimish Vaibhav ?')

    regex_string_search('How are you Nimish Vaibhav ?')
    regex_string_search('Padamata Nimish')

    regex_string_findall('How are you Nimish Vaibhav ?')
    regex_string_findall('Nimish Vaibhav')
    regex_string_findall('Padamata Nimish')

    regex_string_finditer('How are you Nimish Vaibhav ?')
    regex_string_finditer('Nimish Vaibhav')
    regex_string_finditer('Padamata Nimish')
    regex_string_finditer('Nimish Nimish')


    regex_find_phone_number('333-666-9999')
    regex_find_phone_number2('7033217654')
    regex_find_phone_number2('(703) 3217654')
    regex_find_phone_number2('(703) 321 7654')
    regex_find_phone_number2('703.321.7654')
    regex_find_phone_number2('(703)-321-7654')
    regex_find_phone_number2('703-321-7654')

    regex_find_emailid('nimishvaibhav.p@gmail.com')
    regex_find_emailid('nimishvaibhav_p@outlook.com')
    regex_find_emailid('nimishvaibhav1992@yahoo.coom')
    regex_find_emailid('1992nimishvaibhav@hotmail.com')

    regex_find_ipaddr('255.255.255.255')
    regex_find_ipaddr('11.33.55.77')
    regex_find_ipaddr('1.2.3.4')
    regex_find_ipaddr('149.156.186.192')
    regex_find_ipaddr('249.34.86.100')

