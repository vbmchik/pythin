# Сохранить в файл список из 100000 чисел
# закрыть файл
# теперь к числам этого файла постараться применить reduce
# x+y
import json
from functools import reduce
def redo(x,y):
    return x+y

#l = list(range(1,10001,1))
#with open("list.txt", "w+") as f:
#    f.write(json.dumps(l))

with open("list.txt", "r+") as f:
    s = f.read();
    l = list(json.loads(s))

r = reduce(redo, l)
print(r)