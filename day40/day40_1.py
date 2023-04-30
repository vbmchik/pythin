from pprint import pprint


lists = [
    [1,2,3],
    ['a','b','c'],
    [1,1,1]
]

# создать из исходного списка новый такой что все элементы долюны быть числами и суммма всех чисел списка больше 4

res = [ x for x in lists if all([isinstance(item, int) for item in x ]) and sum(x)>4 ]

res1 = list(filter(lambda x: all(
    [isinstance(item, int) for item in x]) and sum(x) > 4, lists))

res2 = []
for x in lists:
    p = list(map(lambda l: str(l), x))
    if (''.join(p)).isnumeric() and sum(x) > 4:
        res2.append(x)

pprint(res)
pprint(res1)
pprint(res2)