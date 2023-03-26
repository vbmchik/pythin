d1 = { 'A': 1, 'B': 2 } ; d2 = { 'C': 3, 'D': 4 }
d3 = d1.update(d2)
d4 = {**d1, **d2}

print(d3)
print(d4)
