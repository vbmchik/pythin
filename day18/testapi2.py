from superclassapi import GetFromApi
from pprint import pprint



url = "https://api.restful-api.dev"
method = "objects"

g = GetFromApi(url).addMethod(method).GetDataFromApi()
apple = list(
    filter( 
           lambda x: "apple" in x["name"].lower(), g.GetResultAsList()))
pprint(apple)

print("Apple" in "Apple iphone")
