import json
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

# read after write correct actions!!!!
with open("beasts.txt", 'w+t') as f:
    f.write(json.dumps(beasts))
# синхронизироать файл на диск    
#    f.flush()
# 'перемотать' файл в начало    
    f.seek(0)
    t = f.read()
    print(t)



