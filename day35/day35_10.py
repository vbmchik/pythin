def fact(n):
    for val in range(1, n+1):
        if not n % val:
            print("!!!")
            yield val


s = fact(20)
d = fact(20)
next(s)
l = list(s)
print(l)

