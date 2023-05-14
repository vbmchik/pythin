def merge_the_tools(string, k):
    n = len(string)  # your code goes here
    l = []
    for i in range(n//k):
        t = ""
        for c in range(k):
            if string[i*k+c] not in set(t):
                t += string[i*k+c]
        l.append(t)
    print(l)

merge_the_tools("AABCAAADA", 3)
