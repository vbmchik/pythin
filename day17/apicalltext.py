from superclassapi import GetFromApi

url = 'http://universities.hipolabs.com/'
p = {'country': 'russian federation', "name": "mos"}


universities = GetFromApi(url).addMethod(method='search').GetDataFromApi()
print(universities.GetDictionaryByParameter("country")['United Kingdom'])
