from pprint import pprint


n = 9
# 1 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3
# 4 4 4
# 5 5
# 6

for x in range(1, n+1):
    pprint(' '.join([str(x) for _ in range(n-x+1)]))

for x in range(1,n+1):
    for y in range(n-x+1):
        print( f'{x} ', end="")
    print("")