
class A:
    def info(self):
        print("A")

        
class B(A):
    def info(self):
        print("B")
    
        
class C(A):
    def info(self):
        print("C")
  
        
class D(B,C):
    pass

class E(C,B):
    pass

D().info()
E().info()