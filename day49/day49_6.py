def NthUglyNumber2(n ) :
    if n == 0:
        return 0
    ugly = [ 0 for _ in range(n)]
    ugly[0] = 1
    i2, i3, i5 = 0, 0, 0
    m2, m3, m5 = 2, 3, 5
    nextUgly = ugly[0]
    for i in range(1,n):
        nextUgly = min(m2, m3, m5)
        ugly[i] = nextUgly
        if nextUgly == m2:
            i2+=1
            m2 = ugly[i2] * 2     
        if nextUgly == m3 :
            i3+=1
            m3 = ugly[i3] * 3
        if nextUgly == m5 :
            i5+=1
            m5 = ugly[i5] * 5
    return nextUgly



# Driver code
p = 900
no = NthUglyNumber2(p)
print(f"{p}th ugly no. is ", no)
