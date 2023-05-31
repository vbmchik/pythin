import re


word = "the address is alice-123@gmail.com and mickey_mouse@disney.com and joe.biden@usa.gov"
# match = re.search(r'iii', "32iiip")
t = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@microsoft.com', word)
print(t)
   
