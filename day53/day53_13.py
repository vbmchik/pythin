import abc

class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

class Something(BluePrint):
    def hello(self):
        print('Hello!')

gf = Something()
gf.hello()