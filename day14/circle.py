import matplotlib.pyplot as plt
import math

x=list(range(-100,101))
y=[math.sqrt(100**2-t**2) for t in x]
x.extend(range(100, -101, -1))
y.extend([-math.sqrt(100**2-t**2) for t in range(100, -101, -1)])
#y1=[-math.sqrt(100**2-t**2) for t in x]
fig, axs = plt.subplots()
axs.plot(x,y,c="blue")
#axs.plot(x,y1,c="blue")
plt.show()