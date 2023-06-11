# 0-5    0-7 
# 10110010 11111111  (110010)
x = int(input('x= '))
y = int(input('y= '))
print(bin(x))
print(bin(y))
x &= 0b11111
y &= 0b1111111
print(bin(x))
print(bin(y))
print(x)
print(y)
print(x*y)
