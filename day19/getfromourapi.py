from superclassapi import GetFromApi

url = 'http://127.0.0.1:5000/'




get = GetFromApi(url)
#get.addMethod("api/v1/income", {"year": 2020, "month": "Октябрь", "business":"Heater"})
get.addMethod("api/v1/income", {
              "month": "Октябрь", "business": "Heater"})
get.GetDataFromApi()
print(get.GetResultAsList())