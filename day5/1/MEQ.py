def roots(a: float, b: float, c:float ):
    if c == 0 and a == 0 and b == 0:
        return [0,0,-1]
    if c != 0 and a == 0 and b == 0:
        return []
    if a == 0 and b != 0 and c != 0:
        return [round(- c / b, 2)]
    dt = b**2 - 4 * a * c
    if dt < 0:
        return []
    d = dt**0.5
    x1 = (- b - d) / (2 * a)
    x2 = (- b + d) / (2 * a)
    if x1 < x2:
       return([round(x1, 2),round(x2, 2)])
    elif x1 == x2:
        return ([round(x2, 2)])
    else:
        return([round(x2, 2), round(x1, 2)])

