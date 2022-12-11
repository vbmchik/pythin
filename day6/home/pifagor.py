def pifagor( a, b, c):
    #         False           True            True
    if not (ifnumber(a) and ifnumber(b) and ifnumber(c)):
        #print(ifnumber(a))
        #print(ifnumber(b))
        #print(ifnumber(c))
        return False
    if a<=0 or b <=0 or c<=0:
        return False 
    # c наиболььшая сторона
    # с**2 == a**2 + b**2
    # result = c**2 == a**2 + b**2
    return c**2 == a**2 + b**2 or b**2 == a**2 + c**2 or a**2 == b**2 + c**2
    
# isinstance('eee',str)

def ifnumber(a):
    return isinstance(a,float) or isinstance(a,int)


pifagor('maria',4,5)

