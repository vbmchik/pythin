def iter_letters(word):
    yield from word


def iter_list(l):
    yield from l

s = iter_letters("Haifa")
t = iter_list([1,2,3,4,5])
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
