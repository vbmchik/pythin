
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
#Добавление любимых фраз Копатыча и Лосяша
addPhrase(beasts, "Лосяш", "Хрю")
#Поиск серий, в которых участвуют оба персонажа
print(seriesSets(beasts))
#Удаление серии Герой Плутона из списка серий Лосяша
seriesRemove(beasts, 'Лосяш', 'Герой Плутона')
print(getBeast(beasts,'Лосяш'))
#Замена цвета Копатыча на Светло-коричневый
changeColor(beasts,"Копатыч","Светло-коричневый")
print(getBeast(beasts,'Копатыч'))
#Добавление данных о любом другом смешарике пользователем
addBeast(beasts)
print(beasts)
#Подсчет количества записанных смешариков
#???
#Создание второй структуры, идентичной первой, удаление оттуда записи про Копатыча так чтобы оригинальная структура не поменялась
# Создавайте )
deleteBeast(omg,'Копатыч')
print(omg)