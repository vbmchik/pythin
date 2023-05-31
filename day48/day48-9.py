import re
def between_markers(word, start, end):
    s = -1
    e = -1
    if not start in word:
        start = ""
    else:
        s = word.find(start)
    if not end in word: 
        end = "" 
    else:
        e = word.find(end)
    if start != "" and end != "" and e < s :
        return ""
    pat = f'{re.escape(start)}(.+?){re.escape(end)}' if end != "" else f'{re.escape(start)}(.+)'
    match = re.search(re.compile(pat), word)
    return match.group(1) if match else ""


word = "the address is alice-123@gmail.com and mickey_mouse@disney.com and joe.biden@usa.gov"
print(between_markers( word, "", ""))