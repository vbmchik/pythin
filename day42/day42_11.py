l = [5, [10, 15, [20, 35, [30,35], 40], 45], 35]

def changer(m):
    for x in range(len(m)):
        if isinstance( m[x], list):
           changer(m[x])
        else:
            if m[x] == 35:
                m[x] = 3500

changer(l)
print(l) 