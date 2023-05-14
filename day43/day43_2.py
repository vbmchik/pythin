#Строки в Питоне сравниваются на основании значений символов.
#Т.е. если мы захотим выяснить, что больше: «Apple» или «Яблоко», – то «Яблоко» окажется бОльшим.
#А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки),
# а русская буква «Я» – 1071 (с помощью функции ord() это можно выяснить).
#Такое положение дел не устроило Анну.
#Она считает, что строки нужно сравнивать по количеству входящих в них символов.
#Для этого девушка создала класс RealString и реализовала озвученный инструментарий. 
# Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
#К слову, Анне понадобилось только 3 метода внутри класса(включая __init__()) для воплощения 
# задуманного.

from collections import UserString

class LString(UserString):
        
    def __init__(self, string) -> None:
        self.data = string
        
    def __eq__(self, __value: object) -> bool:
        return self.data.lower() == __value.lower()

    def __gt__(self, __value: object) -> bool:
        return self.data.lower() > __value.lower()

    def __lt__(self, __value: object) -> bool:
        return self.data.lower() < __value.lower()
    
    def __str__(self) -> str:
        return self.data
    
a = LString("AaAaAa")
b = LString("aaaaaa")

print(a=="aaaaaa")
print("AaAaAa" == "aaaaaa")
