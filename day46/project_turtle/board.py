import os
from pprint import pprint
from random import randint, random
import time

class Board:
   
    def __init__(self, n) -> None:
        self.__board = []
        self.__n = n
        for i in range (n):
            self.__board.append([ 0 for _ in range (n)])
    
    @property
    def n(self):
        return self.__n
    
    def freecell(self, x, y):
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
        try:
            v = tuplexy[2]
        except:
            v = 1
        self.__board[y][x] = v            
  

