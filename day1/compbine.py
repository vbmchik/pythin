import copy 

def fact(n):
    if n == 1 :
        return n
    else:
        return n*fact(n-1)

def combine(files, n, pres):
    flag = n == len(files)-1
    for x in files[n]:
        res = copy.copy(pres)
        res.append(x)
        if( flag ):
            print(res)
        else:
            combine(files,n+1,res)
    
 # 1 2
 # 3 4
 # 1 2 1 4 2 3 2 4     


if __name__ == "__main__":    
    files = [[1,2,3,4], ['a','b','c'], [5,6,7], ['tree', 'stone', 'field', 'grass'],[1,2,3,4,5]]
    #combine(files,0,[])
    print(fact(10))
    #print(set(files[0])&set(files[2]))