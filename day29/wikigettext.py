import wikipedia, re
from wikipedia import DisambiguationError
wikipedia.set_lang("ru")
def getwiki(s):
    try:
        my = wikipedia.page(s)
        wikitext = my.content[:500]
        wikimas=wikitext.split(".")
        wikimas = wikimas[:-1]  # отбросили незаконченные предложения
        wikires = ""
        for line in wikimas:
            if( len(line.strip())>5):
                 wikires += line+"."

        wikires = re.sub('\([^()]*\)','', wikires)
        wikires = re.sub('\{^\{\}]*\}','',wikires)
        return wikires
    except DisambiguationError as ex:
        errorText = "Выберите конкретную статью:\n"
        for t in ex.options:
            errorText += t + "\n"   
        return errorText
    except :
            return "Текст не найден"