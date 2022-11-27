
def palindrom(str):
    str = str.lower().replace(' ', '')
    return str == str[::-1]


#напишите метод (функцию) которая будет проверять является ли строка палиндромом (совпадает с собой в перевернутом виде)
s = "Let it itel"
q = lambda x : x.lower().replace(' ','')
t = q(s) == q(s)[::-1]
print(t)
#print(palindrom(s))