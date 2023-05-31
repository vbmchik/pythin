mapp = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
rmappp ={
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}


def makeromandigit(number: int, dec: int):
    if number < 4:
        return rmappp[1*dec]*number
    if number == 4:
        return rmappp[1*dec]+rmappp[5*dec]
    if number == 5:
        return rmappp[5*dec]
    if number > 5 and number < 9:
        return rmappp[5*dec]+rmappp[1*dec]*(number-5)
    return rmappp[1*dec]+rmappp[10*dec]

def write_roman(number: int):
    t = number
    n = 1
    result = ""
    while number > 0:
        d = number - 10*(number//10)
        result = makeromandigit(d, n) + result
        number = number //10
        n = n*10
    return result, str(t)
        

def calculate_roman(rnumber:str):
    a = sum = p = i = 0
    for x in rnumber.upper():
        m = mapp[x]
        if i > 0 and m > p:
            sum += m-a
            a = 0
        else:
           if m == p or p == 0:
               a+=m
           else:
               sum+=a
               a=m  
        p = m
        i += 1
    sum += a
    return sum


print(write_roman(3888))
print(calculate_roman('MMMDCCCLXXXVIII'))
