def clearword(word):
    # [x for x in word ]
    # [x for x in word if x.isalpha()]
 #   l = []
 #   for x in word:
 #       if x.isalpha():
 #           l.append(x)
    cleanword = ''.join([x for x in word if x.isalpha()])
    return cleanword

with open("beasts.txt", 'r+t') as f:
    words = [ word.lower() for line in f for word in line.split() ]
    #words = []
    #for line in f:
    #    for word in line.split():
    #        words.append(word.lower())
    # [ x**2 for x in [1,2,3,4,5] ]
cwords = list(map(clearword, words))
cwords = filter( lambda x : x != '', cwords)
cwords = list(cwords)
print(cwords)

# .  lines in file для каждой строки
#    line.split() для каждого элемента этого списка word вставляем в итоговый список