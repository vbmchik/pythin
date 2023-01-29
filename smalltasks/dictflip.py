d = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
p = dict(map(lambda x: (d[x],x), d))
print(d)
print(p)