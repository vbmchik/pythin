# Вводится строка пользователем в ней слова и запятые и пробелы
# подсчитать количество уникальных букв не считая пробелы и запятые
# Jacob, Mike, Helen, Louise, Mike
phrase = input("Input your phrase: ")
words = phrase.replace(',','').split()
print(len(set(words)))
print(words)
print(len(set(phrase.lower().replace(' ', '').replace(',',''))))
#text = 'show must go on'
#l = list(text)
#print(l)
#s = set(l)
#print(s)
