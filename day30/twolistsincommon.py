import random
import datetime
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [2, 8, 9, 0, 1, 11, 12]

# общие элементы обоих списков?
print(set(l1) & set(l2))

rer = []
for x in l1:
    if x in l2:
        rer.append(x)

print(rer)

rer = []
for x in l1:
    for b in l2:
        if x == b:
            rer.append(x)
            break
print(rer)
print(l2)

l1 = [random.randint(1, 40000) for x in range(1, 100000)]
l2 = [random.randint(1, 40000) for x in range(1, 100000)]

print(datetime.datetime.now())
rer = []
l1 = set(l1)
l2 = set(l2)
rer = l1 & l2

# print(rer)
print(len(rer))
print(datetime.datetime.now())
