# Четвёртая задача

#У вас есть массив чисел, составьте из них максимальное число. Например:

# [61, 228, 9] -> 961228

def firstnumber( n ):
    if n/10 < 1:
        return n
    else:
        return firstnumber(int(n/10))

start = [161, 2028, 90]

#start.sort(key=firstnumber, reverse=True)


p = [str(x) for x in start]
p.sort(reverse=True)

result = int(''.join(p))

print(result)