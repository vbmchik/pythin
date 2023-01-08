from dbHelp import DataHelp
import matplotlib.pyplot as plt
import sys


def inputImp(question):
    print('1 income grouped by business for all period')
    p = input(question + "\t")
    if p == '.':
        print('Operation cancelled ')
        sys.exit()
    try:
        n = int(p)
    except:
        print('Please enter number, nothing more!')
        return (inputImp(question))
    return n


print('Welcome to manager command center')
print('please choose your option')
print('For exit just enter .')



dataHelp = DataHelp()
while True:
    print('1 income grouped by business for all period')
    choice = input('Enter your choice: ')
    if choice == '1':
        query = 'SELECT sum(income), business FROM Predicator.train group by business order by business;'
        l = dataHelp.executeSomeQuery(query)
        # (1, 2323)
        # (2, 232 )
        #
        y = list(map(lambda x: x[0], l))
        x = list(map(lambda x: x[1], l))
        fig, axs = plt.subplots(1,1)
        axs.bar(x,height = y)
        plt.show()


