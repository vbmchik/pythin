
from datetime import datetime
from itertools import groupby

def mapfunc(w):
    # Let us remove all puncuation and spaces.  
    cleanword = ''.join([i for i in w if i.isalpha()])
    return [cleanword.lower(),1]
# . 'the' .  ['the',1],['the',1],['the',1],['the',1],['the',1],['the',1]
# . counts = [1,1,1,1,1,1]
#
def reducefunc(key, values):
    #counts = [x[1] for x in values]
    # return [key,sum(counts)]
    return [key, len(values)]

print('start ',datetime.now())
with open("advs.txt",encoding="utf-8") as f:
    fulltext = f.read()
#   fulltext =  ''.join (x for word in fulltext for x in word if x.isalpha() or x == ' ')
    fulltext =  ''.join ([x for  x in fulltext if x.isalpha() or x == ' '])
    fulltext = fulltext.lower()
    ls = fulltext.split()
    print('get words',datetime.now())
    unique = set(ls)
    print('get unique',datetime.now())
    d = dict()
    for word in unique:
        d[word] = ls.count(word)
    print('created dict',datetime.now())    
    print(len(ls))
    print(len(unique))  
d = dict(sorted(d.items(), key= lambda x : x[1], reverse=True))      
print('done first',datetime.now())



# Google algorythm inplementation
with open("advs.txt") as f:
    words=[word for line in f for word in line.split()]
print('get words',datetime.now())
map_result = map (mapfunc, words)  
print('map to clear text',datetime.now())
map_result_sorted = sorted (map_result, key = lambda x: x[0])
print('sorted',datetime.now())
reduce_result = []
for k, g in groupby(map_result_sorted, key = lambda x: x[0]):
    reduce_result.append(reducefunc(k, list(g)))
d = dict(sorted(reduce_result, key= lambda x : x[1], reverse=True))    
print('reduced',datetime.now())
print(len(reduce_result))  