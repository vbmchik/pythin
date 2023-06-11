import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db = myclient["Post"]
customers = db["customers"]
for customer in customers.find({"name":"Chuck"}):
    print(customer)
db = myclient["mydatabase"]
collection = db["mycollection"]
for customer in collection.find({"rating": 12}):
    print(customer)
