class Meta(type):
    def __init__(cls, name, bases, namespace):
        super(Meta, cls).__init__(name, bases, namespace)
        print(f"New class creating! {cls}")
        
    def __call__(cls):
        new_instance = super(Meta, cls).__call__()
        print(f"class {cls} new instanse {new_instance}")
        return new_instance

class A:
    pass
class B(A):
    pass
class C(B, metaclass=Meta):
    def __init__(self, x) -> None:
        super().__init__()
        self.x = x

c = C()
print(c)