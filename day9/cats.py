import mysql.connector 

catsdb = mysql.connector.connect(
    host='localhost',
    user='python',
    password='!QA2ws3ed'
)

cursor = catsdb.cursor()
cursor.execute('select * from study.cats')
cats = cursor.fetchall()
#print(cats)
# age - 4 price - 5

#filteredcats = filter( lambda x: x[4] > 3 and x[5] > 2000, cats)

#print(list(filteredcats))
cats.sort(key=lambda x: (x[5], x[1], x[4] ))

print(cats)
