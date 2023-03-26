class InfiniteSquaring:
    
    def __init__(self, initial_number):
        self.number = initial_number

    def __next__(self):
        self.number = self.number**2
        """ if self.number > 3:
            raise StopIteration """
        return self.number
    
    def __iter__(self) -> None:
        return self
    
s = InfiniteSquaring(6)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))


s = iter({1,2,3})
print(next(s))
print(next(s))
print(next(s))
