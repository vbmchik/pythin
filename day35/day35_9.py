def fact(n):
    factor_list = []
    for val in range(1,n+1):
        if not n%val:
            factor_list.append(val)
    return factor_list

print(fact(20))