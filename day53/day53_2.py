class Test:
    def __init__(self, value) -> None:
        self.invar = value

d1 = d3 = Test(100)
d2 = Test(200)
d3.another_var = "Hahahahaha!"
print(d1.invar, d2.invar)
print(Test(7600).invar)
print(d1.another_var)
print(d2.__dict__)
print(d1.__dict__)