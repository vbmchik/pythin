word = 'mhgf678234jhasDI76KJHGdfkjadhf;oa'

newword = ''.join( filter( lambda x: x.isalpha() ,word) )
print(newword)

w = ''
word1 = ''.join( x for x in word if x.isalpha())
print(word1)

spisok = [(1,2),(3,4),(6,6),(8,12),(3,4)]

newspisok = list( x for x in spisok if x[0]%2 == 0 or x[1]%2 == 0)
print(newspisok)

fspisok = list(filter(lambda x: x[0]%2==0 or x[1]%2 ==0, spisok))
print(fspisok)
