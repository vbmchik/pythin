import itertools


def inputlist():
    s = input().split()
    l = list(map(lambda x: int(x), s))
    return l


s = input().split()
k, m = (map(lambda x: int(x), s))
a = []
for _ in range(k):
    a.append(inputlist())

comb = list(set(list(itertools.product(*a))))
comb.sort(key=lambda x: sum([k*k for k in x]) % m, reverse=True)
p = list(map(lambda x: (x,sum([k*k for k in x]) % m), comb))
print((sum([k*k for k in comb[0]])%m))
