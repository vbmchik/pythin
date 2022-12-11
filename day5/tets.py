def move(valera, diana, n):
    for x in range(0, n):
        valera.append(diana[x])
    t = []
    # for i in range(n, len(l2)):
    #    t.append(l2[i])
    # l2=t
    print(valera)
    #diana = [diana[x] for x in range(n, len(diana))]
    for x in range(0, n):
        diana.pop(0)
    print(diana)


tanya = [1, 2, 3, 4, 5]
david = [6, 7, 8, 9, 10]

move(tanya, david, 2)
print(tanya)
print(david)
