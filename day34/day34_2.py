def spoof(st):
    print(st)
    
def trt( st, sp):
    print(st)
    sp(st)
    
def findf(list, i ):
    return list[i]
trt("c", spoof)
c = trt 
l = [spoof, trt]
l.append(c)
print(findf, 1)