def changing_direction(elements: list[int]) -> int:
    p = elements[0]
    directions = 0
    delta = 0 #(-1 0 1)
    for x in elements:
        t = x - p
        if t != 0 :
            t = t//abs(t)
        if t != delta and t != 0 and delta !=0 :
            directions +=1
            delta = t      
        if delta == 0:
            delta = t
        p = x
    return directions


print("Example:")
print(changing_direction([1, 2, 3, 2, 1]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
