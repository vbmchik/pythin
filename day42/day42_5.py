# У вас есть девять цифр: 1, 2, …, 9. 
# Именно в таком порядке. 
# Вы можете вставлять между ними знаки «+», «-» или ничего. 
# У вас будут получаться выражения вида 123+45-6+7+89. Найдите все из них, которые равны 100.

def signs():
    for x in ["+", "-", "", "/", "*"]:
        yield x

def combo(input, index, output):
    if index == len(input):
        if output[-1] not in ["+", "-", "/", "*"]  and eval(output) == 200 :
            print(output)
    else:
        for x in signs():
            combo(input, index+1, output+input[index]+x)
        

num = '123456789'
combo(num,0,"")

# 1     1_
# 12  12_   1_2   1_2_
# 
