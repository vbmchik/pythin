from superclassapi import GetFromApi
from pprint import pprint
import json
url = "https://jsonplaceholder.typicode.com/"
method = "posts"
g = GetFromApi(url)
g.addMethod(method=method)
g.GetDataFromApi()
pprint(g.GetResultAsList())
body = {
    "title": 'foo',
    "body": 'bar',
    "userId": 1
}
g.GetDataFromApi(data=json.dumps(body))
pprint(g.GetResultAsDict())
