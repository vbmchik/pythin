# a*x^2+b*x+c = 0
# D = sqrt( b^2 - 4*a*c )
# x1 = (-b + D)/(2*a)
# x2 = (-b - D)/(2*a)

def MEQn(a: float, b: float, c: float) -> list:
    d = (b**2-4*a*c)**0.5
    x1 = (-b + d)/(2*a)
    x2 = (-b - d)/(2*a)
    if x2<x1:
        return [x2,x1]
    return [x1,x2]

