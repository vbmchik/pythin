import matplotlib.pyplot as plot

x = list(range(1,1001))
y = list(map(lambda y: y**2, x))

fig, axe = plot.subplots()
axe.scatter(x,y, c=y, cmap=plot.cm.Blues, s=5)
plot.show()
