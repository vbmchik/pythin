from board import Board


class Turtle:
    __vectors = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    def __init__(self, board: Board, point: tuple, value) -> None:
        self.board = board 
        self.__point = point 
        self.__vector = 0 
        self.board.board = point[0], point[1], value
        self.camove=True
        self.__value = value
        
    def pointsum(self, point1: tuple, point2:tuple):
        return (point1[0]+point2[0], point1[1]+point2[1])

    def leftvec(self):
        return (-1*self.__vectors[self.__vector][1],
                self.__vectors[self.__vector][0])
    
    def leftcell(self, x, y):
        ppoint = self.pointsum((x, y), self.leftvec())
        return self.board.freecell(ppoint[0], ppoint[1])
    
    def turnvector(self):
        if self.__vector == 3:
            self.__vector = 0
        else:
            self.__vector = self.__vector + 1
            
    def insideboard(self, x, y):
            return x <= self.board.n and y <= self.board.n and x >= 1 and y >= 1
        
    def validate(self, x, y):
        if self.insideboard(x,y):
            if self.board.freecell(x, y):
                self.board.board = x, y, self.__value
                self.__point = (x, y)
                if self.leftcell(x, y):
                    self.turnvector()
                return True
        return False

    def onborderline(self, x, y):
        return x == 1 or y == 1 or x == self.board.n or y == self.board.n
    
    def move(self):
        if not self.camove:
            return False
        for i in range(4):
            if self.__vector + i > 3:
                k = self.__vector + i-4
            else:
                k = self.__vector + i
            x, y = self.pointsum(self.__vectors[k], self.__point)
            if self.validate(x, y):
                if self.onborderline(x,y):
                    if not self.leftcell(x,y):
                        a, b = self.pointsum(
                            self.__vectors[self.__vector], (x, y))
                        if not self.insideboard(a,b):
                            self.camove = False
                            return False
                return True
        self.camove = False
        return False
