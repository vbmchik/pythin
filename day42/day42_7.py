alphabet = {
    'a':65,
    'b':66,
    'c':67,
    'd':68
}

rev = dict( map( lambda x: (x[1],x[0]) , alphabet.items()) )
print(rev)

t = {}
for x,y in alphabet.items():
    t[y] = x
print(t)

c = dict( [(y,x) for (x,y) in alphabet.items()] )
print(c)