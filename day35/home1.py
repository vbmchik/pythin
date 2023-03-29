def show_letters(some_str):
    clean_str = ''.join(letter for letter in some_str if letter.isalpha())
    for symbol in clean_str:
        yield symbol


for x in show_letters("dfdfdsfs lkajsdhfjkl2esdkjf aksjfkl"):
    print(x)