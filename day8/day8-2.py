from textdata import Textdata

t = Textdata().readfile('input.txt').createdict()

print(t.getresult(2002,'JUN'))
t.maxmonth(2002)
t.printdict()