from superclassapi import GetFromApi

# https://datausa.io/api/data?drilldowns=Nation&measures=Population

url = 'https://datausa.io/api/'
method = 'data'
#params = {'drilldowns': 'Nation', 'measures': 'Population'}
# https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest
params = {'drilldowns': 'State', 'measures': 'Population', "year": "2018"}
l = GetFromApi(baseURL=url).addMethod(
    method=method, parameters=params).GetDataFromApi().GetValueFromKey("data")
print(l)
