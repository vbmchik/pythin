import os
from pprint import pprint
from random import randint
import time
from turtle import Turtle
from board import Board

#n = int(input())
n = 20
b = Board(n)
#turtle = Turtle(b, (randint(2, n), randint(2, n)), 2)
turtle = Turtle(b, (5,9),1 )
turtle1 = Turtle(b, (14,16), 2)
turtle2 = Turtle(b, (4, 16), 3)
turtle3 = Turtle(b, (14, 8), 4)
turtle4 = Turtle(b, (8, 17), 5)
os.system('clear')
while (any([turtle.move(), turtle1.move(), turtle2.move(), turtle3.move(), turtle4.move()])):
    pprint(b.board)
    time.sleep(0.5)
    os.system('clear')
