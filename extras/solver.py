import math

def solve(pattern):

    if pattern[:1] == '-':
        return -1.0*solve(pattern[1:])
    
    if not ifBracketsEqual(pattern):
        print('Non equal bracets!')
        return None
    pattern = removeBrackets(pattern)
    indOp = indexOfOperator(pattern)
    if indOp == -1:
        if pattern[:1] == '-':
            return -1.0*solve(pattern[1])
        else:
            return mathOperator(pattern)
    c = list(pattern)[indOp]
    if c == '+':
        return solve(pattern[:indOp])+solve(pattern[indOp+1:])
    if c == '-':
        return solve(pattern[:indOp])-solve(pattern[indOp+1:])
    if c == '*':
        return solve(pattern[:indOp])*solve(pattern[indOp+1:])
    if c == '/':
        return solve(pattern[:indOp])/solve(pattern[indOp+1:])
    if c == '%':
        return solve(pattern[:indOp])%solve(pattern[indOp+1:])
    return 0.0


def mathOperator(pattern):
    sum = 0.0
    parts=pattern.split('(')
    operat = parts[0]
    sw = switchOperator(operat)
    l = len(pattern)
    if sw == 1:
        if l > 1:
            pattern = pattern[1:]
        sum += math.exp(1)
    if sw == 2:
        sum += math.sin(math.radians(solve(pattern[4:l-1])))
    if sw == 3:
        sum += math.cos(math.radians(solve(pattern[4:l-1])))
    if sw == 4:
        ind = indexOfCharacter(';', pattern[4:l-1])+4
        sum += math.pow(solve(pattern[4:ind]),solve(pattern[ind+1:l-1]))
    if sw == 5:
        sum = math.sqrt(solve(pattern[5:l-1]))
    if sw == 6:
        sum = math.log(solve(pattern[3:l-1]))
    if sw == 7:
        sum = math.log10(solve(pattern[3:l-1]))
    if sw == 8:
        sum = math.abs(solve(pattern[4:l-1]))
    if sw == 9:
        ind = indexOfCharacter(';', pattern[4:l-1])+5
        sum = math.max(solve(pattern[:ind]),solve(pattern[ind+1:l-1]))
    if sw == 10:
        sum = math.exp(solve(pattern[4:l-1]))
    if sw == 0:
        sum = float(pattern)    
    
    return sum

    

def switchOperator(pattern):
    if pattern == 'e':
        return 1
    if pattern == 'sin':
        return 2
    if pattern == 'cos':
        return 3
    if pattern == 'pow':
        return 4
    if pattern == 'sqrt':
        return 5
    if pattern == 'ln':
        return 6
    if pattern == 'lg':
        return 7
    if pattern == 'abs':
        return 8
    if pattern == 'max':
        return 9
    if pattern == 'exp':
        return 10
    return 0

def ifBracketsEqual(pattern):
    return pattern.count('(') == pattern.count(')')

def removeBrackets(pattern):
    indOp = indexOfOperator(pattern)
    symbols= list(pattern)
    l = len(symbols)
    if l > 1 and indOp == -1:
        if symbols[0] == '(' and symbols[l-1] == ')':
            pattern = pattern[1:l-1]
    return pattern

def indexOfOperator(pattern):
    indOp = -1
    i = indexOfCharacter('+', pattern ) 
    if i != -1:
        return i
    i = indexOfCharacter('-', pattern ) 
    if i != -1:
        return i
    i = indexOfCharacter('*', pattern ) 
    if i != -1:
        return i
    i = indexOfCharacter('/', pattern ) 
    if i != -1:
        return i
    i = indexOfCharacter('%', pattern ) 
    if i != -1:
        return i
    return -1
    


def indexOfCharacter(symbol, pattern, fromBegin=False):
    index = -1
    flag=0
    symbols= list(pattern)
    for i in range(len(symbols)):
        if symbols[i]=='(' :
            flag+=1
        if symbols[i]==')' :
            flag-=1
        if symbols[i] == symbol and flag == 0:
            if fromBegin:
                return i
            else:
                index = i
    return index


print(solve('pow(sin(20);2)+pow(cos(20);2)'))