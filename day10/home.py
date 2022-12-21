from file import fileOperator

fo = fileOperator('localhost','python','!QA2ws3ed')

print(fo.getData())
query = 'SELECT year, month, sum(income) FROM Predicator.Finances group by year, month;'

print(fo.setQuery(query).getData())

# найти лучший год по доходам
# найти в каждом году лучший месяц по доходам
# 
# #*** 
# получить из базы такую сруктуру - словарь 
# ключ год - значение  словарь - ключ месяц - значение - словарь - ключ - бизнес значение доход

#  {
#  "2018" : 
#             {
#                'march': {otop: 23000, sant: 33434, climat: 343434}
#              }
#             

#
#
#
#
#           )
# }
#  d[2018]['Май']['Сантехника'] = 58908467.26
