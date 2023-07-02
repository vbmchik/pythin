class MyMeta(type):
    def __new__(mcs, name, bases, dictionary):
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attr = "Added in meta"
        return obj
    
class MyObject(metaclass=MyMeta):
    pass

print(MyObject.__dict__)