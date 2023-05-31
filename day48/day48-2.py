import re


word = "piiipiiiipipiiiipiiiipiip1iipiiipipig"
# match = re.search(r'iii', "32iiip")
match = re.search(r'(pi+)+', word)
if match:
    a, b = match.span()
    print(a, b)
    print(word[a:b])
