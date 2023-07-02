def greetings(self):
    print('Have a nice day!')

class MyMeta(type):

    def __new__(mcs, name, bases, dictionary):
        if 'greetings' not in dictionary:
            dictionary['greetings'] = greetings
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj
    
class Class1(metaclass=MyMeta):
    pass

class Class2(metaclass=MyMeta):
    def greetings(self):
        print("Happpy to see you!")

Class1().greetings()
Class2().greetings()