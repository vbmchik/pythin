import requests
from itertools import groupby

class GetFromApi():

    def __init__(self, baseURL) -> None:
        self.baseURL = baseURL

    
    def addMethod(self, method: str, parameters = {}) :
        self.URL = ""
        if self.baseURL[-1] != '/':
            self.URL = self.baseURL + '/'
        else:
            self.URL = self.baseURL

        self.URL = self.URL + method
#        {
#           [parameter1 name] : value,
#           [parameter2 name] : value
#        }    
        if len( parameters):
            self.URL = self.URL + "?"
        else:
            return self  
          
        notfirst = False
        for key, value in parameters.items():
            if notfirst :
                self.URL = self.URL + "&"
            self.URL = self.URL + key + "="
            self.URL = self.URL + str(value).capitalize().replace(" ","+")
            notfirst = True
        return self
    
    def GetDataFromApi(self):
        headers = {'Accept': 'application/json'}
        self.result = requests.get(self.URL, headers=headers)
        return self

    def GetValueFromKey(self, key: str):
        return dict(self.result.json())[key]
    
    def GetResultAsDict(self):
        return dict(self.result.json())

    def GetResultAsList(self):
        return list(self.result.json())
    
    def GetDictionaryByParameter(self, key:str):
        firstlist = list(map(lambda x: x[key], list(self.result.json())))
        firstlist.sort()
        return  dict(
            map(lambda t: (t[0], len(list(t[1]))), groupby(firstlist, lambda x: x)))
    


