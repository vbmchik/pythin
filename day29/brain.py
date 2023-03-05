from fuzzywuzzy import fuzz

def answer(text, brain):
    try:
        text = text.lower().strip()
        a = 0
        n = 0
        nn = 0
        for q in brain:
            if( 'u: ' in q):
                aa = fuzz.token_sort_ratio(q.replace("u: ", ''), text)
                if aa > a and aa != a:
                    a = aa
                    nn = n
            n = n + 1
        s = brain[nn+1]
        return s       
    except Exception as e:
        return "Что то пошло не так!"