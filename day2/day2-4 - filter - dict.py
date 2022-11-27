

def getBeast(beasts, name):
    l = filter( lambda b: b["Имя"] == name, beasts)
    return (list(l)[0])

def getBeasts(beasts, name):    
    l = filter( lambda b: b["Имя"] == name, beasts)
    return(list(l))


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

#print( getBeast(beasts, 'Лосяш'))
#print( getBeasts(beasts, 'Лосяш'))

m = map(lambda beast: beast['Серии'], beasts)
print(sum(m,["первый", "2"]))
# sum 
#print(beasts)    

#f = filter( lambda beast: beast["Имя"] == 'Лосяш', beasts)

#for beast in beasts:
#    if beast["Имя"] == "Копатыч":
#        print(beast['Серии'])
#f = filter( lambda key, value: value=='John', d.items())

#print(list(f))