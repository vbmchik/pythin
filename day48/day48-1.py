# patterns types for regular expressions
# a, X, 2 
# . () but not исключая \n
# \w [a-zA-Z0-9_]
# \W 
# \s
# \t \n \r
# \d цифра от 1 до 9
# ^ старт 
# \\ - слеш
# + - значит повторение
# * - 0 и более

import re
word = "lil1lrlil0lrypomegranad"
#match = re.search(r'iii', "32iiip")
match = re.search(r'l\wl\dl.', word)
if match :
    a, b = match.span()
    print(a,b)
    print(word[a:b])
match = re.search(r'l\wl\dl.', word[6:])
if match:
    a, b = match.span()
    print(a, b)
    print(word[a+6:b+6])
