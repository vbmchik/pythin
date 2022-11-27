def test(**args):
    for a in args:
        print(a, args[a])
    print(args['b'])

def test1(*args):
    for a in args:
        print(a)
    print(args)    

d2 = { 
    "Имя1" : "Копатыч",
    "Цвет1" : "Коричневый", 
    "Серии1" : ["Долгая рыбалка", "Кулинария", "Танцор Диско"]
    }

test(a="23", b = "c", c=12)
test1(1,"2", "343", 1)
s = "3"
f = 4
b=4
print("a=", b, "b=", f)