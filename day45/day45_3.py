from typing import Any
import random

class B:
    def __call__(self) -> Any:
        return random.randint(1,200)
    
b = B()
print(b)

b.value = 6
print(b.value)
B.value=7
print(B.value)
print(b())
print(b())
print(b())
print(B())

print(type(type))
print(type(B))