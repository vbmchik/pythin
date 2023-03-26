def my():
    n = 3
    print(n)
    yield 'first'
    n+=1
    print(n)
    yield 'second'
    n += 1
    print(n)
    yield 'third'
    n += 1
    print(n)
    yield 'fourth'
    n += 1
    print(n)
    yield 'fifth'
    
print("creating")
y = my()
print("created")
print(next(y))
print(next(y))

print(next(y))

print(next(y))

print(next(y))
