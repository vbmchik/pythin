pat = "asbcklfdmegnot"
str = "eksge"

l = list(pat)

s = list(str)
s.sort(key=lambda x: l.index(x), reverse=True)
print(''.join(s))



pat = "mgewqnasibkldjxruohypzcftv" 
str = 'niocgd'
l = list(pat)
d = {l[i]: i for i in range(len(l))}
print(d)
s = list(str)
s.sort(key=lambda x: d[x], reverse=True)
print(''.join(s))
