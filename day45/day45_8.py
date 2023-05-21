# напишите программу которая принимает текст и выводит два слова - самое 
# длинное и самое часто встречающееся

from itertools import groupby

with open('advs.txt', 'r') as f:
    t = f.read()

t = ''.join(filter(lambda x: x.isalpha() or x == ' ', t))
t = t.lower().split()

t.sort(key=len, reverse=True)
print(t[0])
t.sort()
quant = list(map( lambda x: (len(list(x[1])), x[0]), groupby(t) ))
quant.sort(key=lambda x: x[0], reverse=True)
print(quant[0])