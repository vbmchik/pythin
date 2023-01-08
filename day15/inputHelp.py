import sys
from dbHelp import DataHelp

def inputImp(question):
    p = input(question + "\t")
    if p == '.':
        print('Operation cancelled ')
        sys.exit()
    try:
        n = int(p)
    except:
        print('Please enter number, nothing more!')
        return(inputImp(question))    
    return n

print('Hello. This is income processing unit')
print('you will be asked for values to enter')
print('For exit just enter .')


dataHelp = DataHelp()
while True:
    year = inputImp('Enter year: ')
    month = inputImp('Enter month: ')
    business = inputImp('Enter business: ')
    income = inputImp('Enter income: ')
    # All data saved
    if not dataHelp.checkNoExist(year,month,business):
        print('We already have record for those business and data!')
        y = input('if you want to replace input y   ')
        if y != 'y':
            print('Going to next input!')
            next
        else:
            dataHelp.replaceData(year,month,business,income)
            print('Record updated!')
    else:
       dataHelp.insertData(year,month,business,income) 
       print('Record inserted!')

