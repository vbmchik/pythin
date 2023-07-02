#        A 
#      /   \
#     B     C
#      \   /
#        D

class A:
    def info(self):
        print("A")
    def info1(self):
        print("2")
        
class B(A):
    def info(self):
        print("B")
    
        
class C(A):
    def info(self):
        print("C")
  
        
class D(B,C):
    pass

D().info()
D().info1()