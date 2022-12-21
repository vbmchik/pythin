import mysql.connector
from itertools import groupby

def remap( grouplist ):
    l = []
    group = list(grouplist)
    for t in group:
        l.append((t[1],t[2],t[3]))
    return l    


findb = mysql.connector.connect(
    host='localhost',
    user='python',
    password='!QA2ws3ed'
)


cursor = findb.cursor()
query = 'select * from Predicator.Finances order by year, month, business'

cursor.execute(query)
results = cursor.fetchall()

#print(results)


#d = dict(
#    map(
#        lambda y: (y[0],  remap(y[1])),
#        groupby(results, key=lambda x: x[0])
#    )
#)
# map берет список и превращает в другой список
#
#
#
#
print(list(groupby(results, key=lambda x: x[0])))
d = dict(
    map(
        lambda y: (y[0],  list( map(lambda x: (x[1:]), y[1])) ),
        groupby(results, key=lambda x: x[0])
    )
 )

#d = dict(
#    map(
#        lambda y: (y[0], list(y[1])),
#        groupby(results, key=lambda x: x[0])
#    )
#)

#d = dict( 
#    groupby(results, key=lambda x: x[0])
#)
#d = list( filter( lambda x: x[2] == 'Сантехника', results))
print(d)
# данные result
# ('2018', 'Апрель', 'Сантехника', 56948137.58)
#
