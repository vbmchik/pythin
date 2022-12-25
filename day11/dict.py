import mysql.connector
from itertools import groupby

class Finance():

    def yearincome(self, fin, year):
        sum = 0.0
        for month in fin[year]:
            for business in fin[year][month]:
                sum = sum + fin[year][month][business]
        return sum

    def bestmonth(self, fin, year):
        max = [year, '', 0.0]
        for month in fin[year]:
            sum = 0.0
            for business in fin[year][month]:
                sum = sum + fin[year][month][business]
            if sum > max[2]:
                max = [year, month, sum]
        return max

    def remap(self, grouplist):
        l = []
        group = list(grouplist)
        for t in group:
            l.append((t[1], t[2], t[3]))
        return l

    def __init__(self):

        self.findb = mysql.connector.connect(
            host='localhost',
            user='python',
            password='!QA2ws3ed'
        )


        self.cursor = self.findb.cursor()
        self.query = 'select * from Predicator.Finances order by year, month, business'

        self.cursor.execute(self.query)
        self.results = self.cursor.fetchall()

        self.d = dict(
            map(
                lambda y: (y[0],  dict(
                    map(
                        lambda z: (z[0],  dict(
                            map(lambda q: (q[2], q[3]), z[1]))),
                        groupby(y[1], key=lambda p: p[1])
                    )
                )),
                groupby(self.results, key=lambda x: x[0])
            )
        )


