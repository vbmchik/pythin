import mysql.connector
from itertools import groupby

def yearincome(fin, year):
    sum = 0.0
    for month in fin[year]:
        for business in fin[year][month]:
            sum = sum + fin[year][month][business]
    return sum


def bestmonth(fin, year):
    max = [year,'',0.0]
    for month in fin[year]:
        sum = 0.0
        for business in fin[year][month]:
            sum = sum + fin[year][month][business]
        if sum > max[2]:
            max = [year,month,sum]
    return max

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
#print(list(groupby(results, key=lambda x: x[0])))
#d = dict(
#    map(
#        lambda y: (y[0],  list(map(lambda x: (x[1:]), y[1]))),
#        groupby(results, key=lambda x: x[0])
#    )
#)
#
#
#
#print(list(groupby(results, key=lambda x: x[0])))
d = dict(
    map(
        lambda y: (y[0],  dict(
            map(
                lambda z: (z[0],  dict(
                    map(lambda q: (q[2],q[3]), z[1]))),
                        groupby(y[1], key=lambda p: p[1])
            )
        )),
        groupby(results, key=lambda x: x[0])
    )
)

print(d)

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
print(yearincome(d, '2018'))

bestyear = ['0',0]
for year in d:
    t = yearincome(d, year)
    if t > bestyear[1]:
        bestyear = [year,t] 
print(bestyear)    

for year in d:
    print(bestmonth(d, year))

# данные result
# ('2018', 'Апрель', 'Сантехника', 56948137.58)
#
