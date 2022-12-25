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

print(cats)