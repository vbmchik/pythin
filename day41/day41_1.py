class A:
    a = 5
    b = 6
    def summa():
        return A.a+A.b
    
    def __init__(self):
        self.a = 4
        self.b = 9

        
a = A()
b = a
a = A()
print(a)
print(b)
print(a.a)
print(a.b)
print(A.summa())
        