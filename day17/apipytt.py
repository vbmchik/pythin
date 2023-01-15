import requests
from itertools import groupby
url = 'http://universities.hipolabs.com/search'
#?country=United+States'

# Базовая строка адреса http://universities.hipolabs.com/
# Метод search - имя метода - search 
# ? отделяет параметры метода
# country=United+States сами переметры и значения
# python - def Name(parameter1, parameter2)
# web service - ?parameter1=string1&parameter2=string2

headers = {'Accept': 'application/json'}

r = requests.get(url=url,headers=headers)

universities = list(r.json())
countries = list(map(lambda x: x['country'], universities))
countries.sort()
countries = dict(map(lambda t: (t[0], len(list(t[1]))), groupby( countries, lambda x: x )))
print(countries['United Kingdom'])
