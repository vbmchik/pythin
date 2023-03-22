def shout(text):
    return text.upper()

print( shout("Hello"))

yell = shout

print(yell("hello"))

print(shout)
print(yell)