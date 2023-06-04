def mountain_scape(tops: list[tuple[int, int]]) -> int:
    # your code here
    overlap = 0
    l = []
    for x, y in tops:
        l.append((x-y,x+y))
    l.sort(key=lambda x: x[0])  
    print(l) 
    n = len(l)
    area = 0
    overlap = 0
    for x in range(n):
        area += ((l[x][1]-l[x][0])/2)**2
        if l[x][0] < 0:
            area -= (l[x][0]**2)/2
        if x < n-1:
            for y in range(x+1,n):
                if l[x][1] > l[y][0]:
                    o = l[x][1] - l[y][0]
                    overlap += (o/2)**2
    return area-overlap


print(mountain_scape([(1, 1), (4, 2), (7, 3)]))

# __1_____2__
# _1___2_____
# ____1____2_
# __1________2
