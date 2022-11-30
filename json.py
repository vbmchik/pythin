# Что такое кодировка?
import json

def printJson(object):
    l = json.dumps(object)
    print(l)

def string2Json(string):
    l = json.loads(string)
    return l

d2 = { 
    "key" : 3,
    "key2" : 'abc', 
    "key3" : [2, '34', 'c']
    }

l1 = [1,2,3,"33"]
s1 = "\"Hello!\""
print(s1)
s1 = '{"filename":"input.doc", "version":"2.1.2", "owner":"Johnson"}'
#printJson(s1)    
beasts = list()

beasts.append({ 
    "name" : "One",
    "color" : "White", 
    "series" : ["1","2","3"]
    })

beasts.append({ 
    "name" : "two",
    "color" : "black", 
    "series" : [1, 3, 4]
    })
printJson(beasts)
