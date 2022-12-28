import mysql.connector
from itertools import groupby

catdb = mysql.connector.connect(
    host='localhost',
    user='python',
    password='!QA2ws3ed'
)

catcursor = catdb.cursor()
query =  'select exhibit.name, exhibit.data, exhibit.address, cats.name, cats.age, cats.color, cat_owners.name, '
query += 'cat_owners.surname from study.cat_exhibit_relation '
query += 'left join study.exhibit ' 
query += 'on '
query += 'cat_exhibit_relation.exhibitid = exhibit.idexhibit '
query += 'left join study.cats '
query += 'on cat_exhibit_relation.catid = cats.id '
query += 'left join study.cat_owner_relation '
query += 'on cats.id = cat_owner_relation.catid '
query += 'left join study.cat_owners '
query += 'on cat_owner_relation.ownerid = cat_owners.idcat_owners '

catcursor.execute(query)
cats = catcursor.fetchall()

#print(cats)
# 0 - имя мероприятия 3 - имя кота 
cats.sort(key= lambda x: x[0])
#print(cats)
dcats = dict(map( lambda record: (record[0], list(map(lambda t: t[3], record[1]))),
     groupby(cats, lambda x: x[0])))
ddd={}
for y in groupby(cats, lambda q: q[0]):
    ddd[y[0]] = list(map(lambda x: x[3], y[1]))
print(ddd)
newcats = dict(map(
      lambda e: (e[0], list(map( lambda p: p[3], e[1]))),
      groupby(cats, lambda q:  q[0])
))
print(newcats)
