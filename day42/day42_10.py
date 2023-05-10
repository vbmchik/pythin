def outer(x,y):
    def inner():
        return x+y
    return inner()+"developer"

print(outer("Masha","Vasya"))