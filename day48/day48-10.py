import re
with open('advs.txt') as file:
    text = file.read()
names = re.findall(r'\w\s([A-Z][a-z]+)', text)
names = [ name for name in names if len(name) > 3]
names = set(names)
for match in names:
    print(f"{match}")
    
print(len(names))
