import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Movies"]

mycol = mydb["Series"]

mylist = [
#    {"name": "Game of Thrones", "year": 2022},
#    {"name": "House of Cards", "year": 2013},
#    {"name": "Suits", "year": 2011}
    {"name": "The Blacklist", "year": 2013}
]

x = mycol.insert_many(mylist)
print(x)