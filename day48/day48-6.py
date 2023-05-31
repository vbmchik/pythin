import re


word = "the address is alice-123@gmail.com and mickey_mouse@disney.com and joe.biden@usa.gov"
# match = re.search(r'iii', "32iiip")
match = re.search(r'([\w\.-]+)@([\w\.-]+)', word)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
