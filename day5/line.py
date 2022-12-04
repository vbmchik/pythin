from figure import Figure
class Line(Figure):
    def __init__(self, n, length):
        super().__init__(n)
        self.length = length
    def len(self):
        return self.length
    def print(self):
        super().print()
        print(f'Line with length {self.length}')

l = Line(2,4)
l.print()