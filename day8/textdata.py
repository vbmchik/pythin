from itertools import groupby
# берет файл и превращает его в список показателей как в первой части урока


class Textdata():

    def __init__(self) -> None:
        self.data = []
        self.map = {}
        self.calendar = {
            "JAN": 1,
            "FEB": 2,
            "MAR": 3,
            "APR": 4,
            "MAY": 5,
            "JUN": 6,
            "JLY": 7,
            "AUG": 8,
            "SEP": 9,
            "OCT": 10,
            "NOV": 11,
            "DEC": 12
        }

    def listprint(self):
        for x in self.data:
            print(x)

    def printdict(self):
        for x, y in self.map.items():
            print(f'key = {x}, value = {y}')

    def readfile(self, filename: str):
        try:
            with open(filename, "t+r") as file:
                for line in file.readlines():
                    l = []
                    for word in line.split():
                        l.append(''.join(filter(lambda x: x.isalnum(), word)))
                    self.data.append(l)
            self.data.sort(key=lambda x: x[2])
        except:
            print('file not found')    
        return self

    def maxmonth(self, year):
        month = max(self.map[year], key=lambda x: self.map[year][x])
        print(month)


    def sortlist(self,l):
        l.sort(key = lambda x: self.calendar[x[1]])
        return l

    def createdict(self):
        self.map = dict(
            map(
                lambda y: ( int(y[0]), 
                            {t[1]: int(t[0])
                             for t in self.sortlist(list(y[1]))}), 
                groupby(self.data, key=lambda t: t[2])
            )
        )
        return self

    def getresult(self, year:str, month:str):
        try:
            return self.map[year][month]
        except:
            return 'error'    





