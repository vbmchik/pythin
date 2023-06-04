def checker(s):
    stack = []
    opened = '{[('
    closed = '}])'
    for l in s:
        if l in opened:
            stack.append(l)
        if l in closed:
            if len(stack) == 0:
                return False
            if stack.pop() != l:
                return False
    return len(stack) == 0
input = "[1+1]+(2*2)-{3/3}"  # {1+[2-(3+4)]}
print(checker(input))

