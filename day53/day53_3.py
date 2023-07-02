class Test:
    
    classvar = "shared!"
    
c1 = Test()
c2 = Test()

Test.classvar = "Else!"
print(Test.classvar)
print(c1.classvar)
print(c2.classvar)

print(c1.__dict__)
print(c2.__dict__)