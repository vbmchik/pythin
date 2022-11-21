
def owner( files ):
    owners = dict()
    for key, value in files.items():
        #print( key + value)
        if value in owners.keys():
            owners[value].append(key)
        else:
            owners[value] = [key]
    return owners 

if __name__ == "__main__":    

    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy',
        'text.py': 'Randy',
        'list.py': 'Stan'#,  #key exists? No! Create!
        #'list.py': 'Liza',  #key exists? Yes! Change!
        #'list.py': 'Vasya'  #key exists? Yes! Change!
    }   
    
    print(files)

    #print(owner(files))

    # сделать список со многими ключами ( повторяющиеся ключи меняем
    #  например ключ ключ1 ключ11  )
