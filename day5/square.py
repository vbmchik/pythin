from figure import Figure

class Square(Figure):
    def __init__(self, a):
        super().__init__(2)
        self.a = a
    def len(self):
        return 4*self.a
    def square(self):
        return self.a**2
