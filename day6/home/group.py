

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

input.sort(key=lambda x: x[1])

result = []
for k,g in groupby(input,key=lambda x: x[1]):
    result.append((k, list(v[0] for v in list(g))))
test = {k: list(v[0] for v in list(g)) for k, g in groupby(input, key=lambda x: x[1])}
print(result)
print(test)
