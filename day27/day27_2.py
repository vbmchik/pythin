a = [[77,68,86,73],   # first student grades
     [96,87,89,81],  # second student grades
     [70,90,86,81]]  # third ...

marks = []
print(a[0][2])
for s in a:
  summa = 0
  for m in s:
    summa += m    # summa = summa + m
  marks.append(summa/4)
print(marks)         
      
for row in a:
  for item in row:
    print(item, end=' ')
  print()

for t in enumerate(a):
  print(t)  

for i, row in enumerate(a, start=1):
  for j, item in enumerate(row, start=1):
    print(f'a[{i}][{j}]={item}', end=' ')
  print()
  
x,y=(1,2)