import itertools

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [2, 8, 9, 0, 1, 11, 12]


l3 = list(filter(lambda x: x in l2, l1))

print(l3)

s1 = set(l1)
s2 = set(l2)

print(list(s1 & s2))

# *****
l3 = set()
for x in l1:
    for y in l2:
        if x == y:
            l3.add(x)
print(list(l3))

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [2, 8, 9, 0, 1, 11, 12]
l3 = [2, 4, 6, 3, 4, 2, 3, 4]
l4 = [11, 13, 14, 15, 16, 17]
# Ищем есть ли общиме элементы у списоков - элементов большого списка


def combunit(ar):
    p = set(l[0])
    for x in range(1, len(ar)):
        uni = set()
        for y in p & set(ar[x]):
            uni.add(y)
        p = uni.copy()
    if (len(p) > 0):
        print(p, ar)


l = [[2, 8, 9, 3, 1, 11, 12], [2, 4, 6, 3, 4, 1, 3, 4], [
    1, 3, 14, 15, 16, 17], [1, 2, 3, 4], [3, 4, 5], [1, 2, 3, 4, 5, 6, 7]]


for i in range(2, len(l)):
    combinations = itertools.combinations(l, i)
    for ll in list(combinations):
        print("combo: ", ll)
        combunit(list(ll))
combunit(l)
