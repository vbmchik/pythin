
#Filter 

nums = [1,2,3,6,8,7,9,12,14,3,6]

#odd_nums = [num for num in nums if num%2 ==0]
odd_nums = [num for num in range(1,34,1) if num%2 == 0]
# [ данные откуда берутся и при каком условии ]
#print(odd_nums)
def odd(x):
    if x%2 !=0:
        return x

t = {
    "cio" : ["John", "Smith"],
    "cto" : ['John', 'Black'],
    'cfo' : ['Sandra', 'Bullock'],
    'ceo' : ['John', 'Pollock']
}

i = filter( lambda item: item[1][0] == 'John', t.items())
q = [key[0] for key in t.items() if key[1][0]=='John']
print(list(q))
m = map(lambda x: x[0], i)
print(list(m))

odd_nums = []
for num in range(1,32,4):
    if num%2 == 0 :
        odd_nums.append(num)

print(list(filter(odd, range(1,34,1))))
m = list( map(odd, range(1,32,1)) )
print(m)
#print(list(filter(lambda x : x%2!=0, range(1,34,1))))
#odd_nums = [lambda x: x/2 for num in range(1,34,1) if num%2 == 0] 
#print(odd_nums)      