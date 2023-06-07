numbers = {1}

while len(numbers)<50:
    p = list(numbers)
    for i in range(len(p)):
        numbers.add(p[i]*2)
        numbers.add(p[i]*3)
        numbers.add(p[i]*5)

print(sorted(numbers))   
    
