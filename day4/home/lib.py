
from datetime import datetime
import sys;
from itertools import groupby;

def mapfunc(w):
    # Let us remove all puncuation and spaces.  
    cleanword = ''.join([i for i in w if i.isalpha()])
    return [cleanword,1];

def reducefunc(key, values):
    counts = [x[1] for x in values];
    return [key,sum(counts)];

print('start',datetime.now())
with open("advs.txt",encoding="utf-8") as f:
    fulltext = f.read()
    fulltext = fulltext.replace(",","").replace(".","").replace(":","").replace("?","").replace("!","").replace("-","").replace(";","").replace("\n","").replace('"',"").replace("'","")
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
print('done first',datetime.now())
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
print('reduced',datetime.now())
print(len(reduce_result))  