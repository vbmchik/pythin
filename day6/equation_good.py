def roots(a: float, b: float, c: float) -> list:
    # есть два корня [minx, maxx]
    # есть один корень [x]
    # нет корней []
    # бесконечное количество корней [0,0,-1]
    if a == b == c == 0:
        return [0, 0, -1]
    if a == b == 0:
        return []
    if a == 0:
        x1 = round(-b/c,2)
        return[x1]
    d = b**2-4*a*c
    if d < 0:
        return []
    sd = d**0.5
    x1 = round((-b + sd)/(2*a),2)
    x2 = round((-b - sd)/(2*a),2)
    if x1 == x2:
        return [x1]
    if x1 > x2:
        return [x2,x1]
    return [x1,x2]
    
