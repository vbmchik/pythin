alphabet = {
    'a': 65,
    'b': 66,
    'c': 67,
    'd': 68,
    'e': 69,
    'f': 70
}

f = ['a','c','f']

r = dict(filter(lambda x: x[0] in f , alphabet.items()))
print(r)
d = dict( (x,y) for (x,y) in alphabet.items() if x in f )
print(d)
k = [ x for x in alphabet.keys()]
for x in k:
    if x not in f:
        del alphabet[x]
        
print(alphabet)