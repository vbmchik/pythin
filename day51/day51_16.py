import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Movies"]

mycol = mydb["Series"]

series = mycol.update_one({"name": "Suits"}, {"$set": {"year": 2010}})

# https://hevodata.com/learn/install-mongodb-python-on-windows/
