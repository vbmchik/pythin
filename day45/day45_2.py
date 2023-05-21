class A:
    pass

o = object()
a = A()

print(type(o))
print(type(a))
print(isinstance(o, object))
print(isinstance(a, A))
print(isinstance(a, object))
print(type(A))