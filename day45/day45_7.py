from typing import Any


class SingletonMeta(type):
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        cls.instance = None
    
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwds)
        return cls.instance

class SingletonBaseMeta(metaclass=SingletonMeta):
    pass

class A(SingletonBaseMeta):
    pass

class B(A):
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
c.t = 5
c.d = 6
print(a)
print(b)
print(c.t+c.d)
