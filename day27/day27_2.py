a = [[77,68,86,73],   # first student grades
     [96,87,89,81],  # second student grades
     [70,90,86,81]]  # third ...

marks = []

for s in a:
  summa = 0
  for m in s:
    summa += m    # summa = summa + m
  marks.append(summa/4)
print(marks)         
      
