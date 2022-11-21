import datetime

greetings = [
    ["Спокойной ночи","Доброе утро","Добрый день","Добрый вечер"],
    ["Good night","Good morning","Good day","Good evening"],
    ["לילה טוב","בוקר טוב","יום טוב","ערב טוב"]
    ]
lang = input("Enter language: \nRU - 1\nENG - 2\nHE - 3\n")
lang = int(lang)-1

time = datetime.datetime.now().hour


print(unit)
if 0 < time <= 6 :
        print (greetings[lang][0])
        pass
elif 6 < time <= 12 :
        print (greetings[lang][1])
        pass
elif 12 < time <= 18 :
        print (greetings[lang][2])
        pass
elif 18 < time <= 24 :
        print (greetings[lang][3])
        pass 
else : 
        print ("Incorrect time")
        pass