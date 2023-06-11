import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]   # создание базы данных
collection = mydb["mycollection"] # создание коллекции
record = { 
          "description": "eert", 
          "tags": ["MySQL", "SQL", "database"], 
          "viewers": 232,
          "rating": "a"
          }
collection.insert_one(record)