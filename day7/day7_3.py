def takesecond(x):
    return x[1]

from itertools import groupby
input = [
    ('11013331', 'KAT'),
    ('9085267',  'NOT'),
    ('5238761',  'ETH'),
    ('5349618',  'ETH'),
    ('11788544', 'NOT'),
    ('962142',   'ETH'),
    ('7795297',  'ETH'),
    ('7341464',  'ETH'),
    ('9843236',  'KAT'),
    ('5594916',  'ETH'),
    ('1550003',  'ETH')
]
for x in range(0, len(input)):
    print(input[x])
print('Now! Focus pokus!')
input.sort(key = lambda x: x[1])
#input.sort(key=takesecond)

for x in range(0, len(input)):
    print(input[x])

l = [ x for x in range(0,11)]

print(l)  

result = []

for key, group in groupby(input, key=lambda x: x[1]):
    result.append((key, [ v[0] for v in group ] ))

d = {key: [v[0] for v in group] for key, group in groupby(input, key=lambda x: x[1])}

for key, value in d.items():
    print( f'key = {key}, value = {value}' )

# Filter Sorted Map Reduce Sum Groupby    