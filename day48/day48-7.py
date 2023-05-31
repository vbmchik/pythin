import re


word = "the address is alice-123@gmail.com and mickey_mouse@disney.com and joe.biden@usa.gov"
# match = re.search(r'iii', "32iiip")
emails = re.findall(r'([\w\.-]+)@([\w\.-]+)', word)
for match in emails:
    print(f"name: {match[0]}, domain: {match[1]}")

   
