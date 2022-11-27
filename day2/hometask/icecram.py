import copy

def combine(files, n, pres):
    flag = n == len(files)-1
    for x in files[n]:
        res = copy.copy(pres)
        res.append(x)
        if flag:
            print(res)
        else:
            combine(files,n+1,res)    
    
def ice(icecream):
    for i in [0,1]:
        for j in [0,1]:
            print(icecream[0][i],icecream[1][j])

machine = [["vanilla", "chocolate"], ["chocolate sauce", "liquor"]]
#           1 .                 2     
# 1 .   ["vanilla",         "chocolate"]
# 2 .   ["chocolate sauce", "liquor"]
# .   1,1 - 1,2 - 2,1 - 2,2
# .   0,0 - 0,1 - 1,0 - 1,1
ice(machine)
#combine(machine,0,[])