import re


word = "the address is alice-123@gmail.com and it is subscribed"
# match = re.search(r'iii', "32iiip")
match = re.search(r'([\w\.-]+)@([\w\.-]+)', word)
if match:
    a, b = match.span()
    print(a, b)
    print(word[a:b])
