import copy

def addPhrase(beasts, name, phrase):
    beast = getBeast(beasts, name)
    beast['Фраза'] = phrase

def addBeast(beasts, name, color, series ):
    beasts.append({
        "Имя" : name,
        "Цвет" : color, 
        "Серии" : series
    })
def findBeast(beasts, name):
    n = -1
    for i in [0,len(beasts)-1, 1]:
        if beasts[i]['Имя'] == name:
           n = i
           return n
    return n       

def delBeast(beasts, name):
    n = findBeast(beasts,name)
    if n == -1 :
        print('No beast')
        return
    beasts.pop(n)

def allSeries(beasts):
    l = []
    for beast in beasts:
        l += beast['Серии']
    f = filter(lambda x: l.count(x)>1, l)
    print(set(f))    

def getBeast(beasts, name):
    l = filter( lambda b: b["Имя"] == name, beasts)
    return (list(l)[0])
# Здесь должен быть ваш код - методы которые требуются в задаче мы не используем if, for, while... 

#
#
beasts = list()

beasts.append({ 
    "Имя" : "Лосяш",
    "Цвет" : "Шафрановый", 
    "Серии" : ["Герой Плутона","Бабочка","Долгая рыбалка"]
    })

beasts.append({ 
    "Имя" : "Копатыч",
    "Цвет" : "Коричневый", 
    "Серии" : ["Долгая рыбалка", "Кулинария", "Танцор Диско"]
    })

# нельзя использовать циклы и условия
#Добавление любимых фраз Копатыча и Лосяша
#addPhrase(beasts, "Лосяш", "Хрю")
#print(beasts)
#Поиск серий, в которых участвуют оба персонажа
#allSeries(beasts)
#print(seriesSets(beasts))
#Удаление серии Герой Плутона из списка серий Лосяша
#l = getBeast(beasts,'Лосяш')
#l['Серии'].remove('Герой Плутона')
#print(l)
#seriesRemove(beasts, 'Лосяш', 'Герой Плутона')
#print(getBeast(beasts,'Лосяш'))
#Замена цвета Копатыча на Светло-коричневый
#l = getBeast(beasts,'Копатыч')
#l['Цвет'] = "Светло-коричневый"
#print(l)
#changeColor(beasts,"Копатыч","Светло-коричневый")
#print(getBeast(beasts,'Копатыч'))
#Добавление данных о любом другом смешарике пользователем
#addBeast(beasts)
#print(beasts)
#Подсчет количества записанных смешариков
#???
#Создание второй структуры, идентичной первой, удаление оттуда записи про Копатыча так чтобы оригинальная структура не поменялась
# Создавайте )
#deleteBeast(omg,'Копатыч')
beasts2 = beasts.copy()
delBeast(beasts2,'Копатыч')
print(beasts)
print(beasts2)