def ugly_number(n: int) -> int:
    def num235(x):
        nums = [2, 3, 5]
        if x == 1:
            return 1
        for y in nums:
            if not x%y:
                return num235(x//y)
        return 0
    def number():   
        a = 1
        while(True):
            if a == 1:
                yield 1
                a = 2                
            while(num235(a)!=1):
                a += 1
            yield a 
            a = a+1
        
    w = number()
    r = 0
    for x in range(n):
       r = next(w) 
    return r


print(ugly_number(900))
