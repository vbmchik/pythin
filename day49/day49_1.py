# Вам предоставляется набор координат, в которых расставлены белые пешки. 
# Вы должны подсчитать количество защищенных пешек.
# Входные данные: Координаты расставленных пешек в виде набора строк.
# Выходные данные: Количество защищенных пешек в виде целого числа.
# Пример:
# assert safe_pawns({"d2", "f4", "d4", "b4", "e3", "g5", "c3"}) == 6
# assert safe_pawns({"f4", "g4", "d4", "b4", "e4", "e5", "c4"}) == 1
# Как это используется: Для игрового искусственного интеллекта оценка текущего состояния 
# в игре является одной из важных задач. Эта методика покажет вам как можно реализовать
# это для расстановок шахматных фигур.


from pprint import pprint

def checker(x, y):
    if y == 0:
        return False
    t = y-1
    r = False
    if x > 0:
        r = board[t][x-1]
    if x < 7:
        r = r or board[t][x+1]
    return r
        
    
hor = 'abcdefgh'
ver = '12345678'

board = []
for _ in range(8):
    board.append([ False for i in range(8) ])
#input = {"d2", "f4", "d4", "b4", "e3", "g5", "c3"}
input = {'h2', 'a1', 'h3', 'a2', 'a3', 'h1', 'a4', 'h4'}
for pawn in input:
    x, y = tuple(pawn)
    board[ver.index(y)][hor.index(x)] = True
pprint(board)
protected = 0
for y in range(8):
    for x in range(8):
        if board[y][x] and checker(x,y):
            protected += 1
print(protected)