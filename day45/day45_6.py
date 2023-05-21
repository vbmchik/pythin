class B:
    pass

class SingletonBase:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance
    
class A(SingletonBase):
    pass


a = A()
b = A()
c = A()
print(a)
print(b)
print(c)
a = B()
b = B()
c = B()
print(a)
print(b)
print(c)
