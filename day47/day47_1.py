def flat_list(data: list):
    s = str(data)
    s = ''.join(x for x in s if x != '[' and x != ']').split(", ")
    return [int(x) for x in s]

print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))
