from asyncio import sleep
import os
from pprint import pprint
from random import randint, random
import time



class Board:
    __vectors = [(0,1),(-1,0),(0,-1),(1,0)]
    def __init__(self, n) -> None:
        self.__board = []
        self.__n = n
        self.__vector=0
        for i in range (n):
            self.__board.append([ 0 for _ in range (n)])
    
    def startpoint(self, x, y):
        self.__point = x,y
        self.board = x,y
        
    @property
    def point(self):
        return self.__point
    
    def pointsum(self,point1, point2):
        return (point1[0]+point2[0], point1[1]+point2[1])
    
    def validate(self, x, y):
        if x<=self.n and y <=self.n and x >=0 and y >=0:
            if self.bvalue(x,y) :
                self.board = x, y
                self.__point = (x,y)
                pvector = (-1*self.__vectors[self.__vector][1],
                           self.__vectors[self.__vector][0])
                ppoint = self.pointsum((x,y), pvector)
                if not self.bvalue(ppoint[0], ppoint[1]):
                    return True
                if self.__vector == 3:
                    self.__vector = 0
                else:
                    self.__vector = self.__vector + 1
                return True
        return False
                
    def move(self):
        for i in range(4):
            if self.__vector + i > 3:
                k = self.__vector +i-4
            else:
                k = self.__vector + i
            x, y = self.pointsum(self.__vectors[k], self.__point)
            if self.validate(x,y):   
                if x == 1 or y == 1 or x == self.__n or y == self.__n:
                    pvector = (-1*self.__vectors[self.__vector][1],
                            self.__vectors[self.__vector][0])
                    ppoint = self.pointsum((x, y), pvector)
                    if not self.bvalue(ppoint[0], ppoint[1]):
                        a, b = self.pointsum(self.__vectors[self.__vector], (x,y))
                        if a ==0 or a > self.n or b ==0 or b > self.n:
                            return False
                return True
        return False
                
        
    
    @property
    def n(self):
        return self.__n
    
    def bvalue(self, x, y):
        y = self.n-y
        x = x-1
        return self.__board[y][x] == 0
    
    @property
    def board(self):
        return self.__board   
    
    @board.setter
    def board(self, tuplexy: tuple ):
        y = self.n-tuplexy[1]
        x = tuplexy[0]-1
        self.__board[y][x] = 1            
  
n = int(input())  
b = Board(n)

b.startpoint(randint(2,n), randint(2,n))
os.system('clear')
while(b.move()):
    pprint(b.board)
    time.sleep(0.5)
    os.system('clear')
