from itertools import groupby


def listprint(l):
    for x in l:
        print(x)


def printdict(d):
    for x, y in d.items():
        print(f'key = {x}, value = {y}')


input = [
    ('11013331', 'JUN', '2002'),
    ('9085267',  'MAY', '2002'),
    ('5238761',  'JLY', '2005'),
    ('5349618',  'JLY', '2003'),
    ('11788544', 'JUN', '2005'),
    ('962142',   'JLY', '2002'),
    ('7795297',  'MAY', '2003'),
    ('7341464',  'JLY', '2004'),
    ('9843236',  'MAY', '1998'),
    ('5594916',  'MAY', '1999'),
    ('1550003',  'MAY', '2001')
]
# s = [2, 4, 5, 3]
# s.sort()
# listprint(s)

listprint(input)

input.sort(key=lambda x: x[2])
print('---------------')
listprint(input)
print('---------------')


# key = 2002
# y =
# ('11013331', 'JUN', '2002') -t
# ('9085267', 'MAY', '2002') -t
# ('962142', 'JLY', '2002') -t
#
#
result = {}
for x, y in groupby(input, key=lambda x: x[2]):
    #result[x] = [(t[1], t[0]) for t in y]
    l = list(y)
    print(l)
    
    result[x] = {t[1]: t[0] for t in y}

for x in groupby(input, key=lambda t: t[2]):
    print(x[0], list(x[1]))

resulttest = dict(
    map(
        lambda y: (y[0], {t[1]: t[0] for t in y[1]}), # преобразование в кортеж 
        #(год, словарь (месяц, показатель)) кажого элемента группировки
        groupby(input, key=lambda t: t[2])  # сортировка по году
        )
    )



print('---------------')
printdict(resulttest)
print('---------------')

# for a, b in result.items():
#    result[a] = {t[0]: t[1] for t in b}

# printdict(result)

# print(result['2002']['MAY'])
