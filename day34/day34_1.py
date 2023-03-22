l = [1,2,3,4,5]

c = (1,2,3,4,5)

print(hex(id(l)))
print(hex(id(c)))

l.append(6)
c = c + (6,)
print(l)
print(c)
print(hex(id(l)))
print(hex(id(c)))

c = "from django.conf import settings"
c = 5

