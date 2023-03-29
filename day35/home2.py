#infinite(list, tries)

def infinite(list, tries):   
    for x in list:
        for _ in range(tries):
            yield x

for x in infinite([1, 2, 3], 6):
    print(x)

