from random import randint
# open('filename', mode, encoding (named parameter))
f = open('json.py', 'r' )
t = f.read()
f.close()

l = [ randint(1,10000) for x in range(1,10)]
f = open('text.txt', 'w')
f.write(str(l))
f.close()
