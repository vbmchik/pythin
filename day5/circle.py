from figure import Figure
import math
class Circle(Figure):
    def __init__(self, r):
        super().__init__(0)
        self.r = r
    def print(self):
        super().print()
        print(f"circle with radius {self.r}")
    def len(self):
        return 2*math.pi*self.r

c = Circle(3)
c.print()
print(c.len())