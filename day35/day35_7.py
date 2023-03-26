def myfor(iterable, loop_body_fun):
    iterator = iter(iterable)
    next_element_exist = True
    while next_element_exist:
        try:
            element = next(iterator)
        except StopIteration:
            next_element_exist = False
        else:
            loop_body_fun(element)
            
def test(x):
    print(x**2)
    
l = [1,2,3,4,5,6]

myfor(l, test)    

coords = [1,2,3]
print(coords)
x,y,z=coords
print(x,y,z)