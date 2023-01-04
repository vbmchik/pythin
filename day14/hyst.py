from plotly.graph_objs import Bar, Layout
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np

years = [1998, 1999, 2000, 2001, 2002, 2003, 2004]
l = [1, 2, 3, 4, 5, 6, 7]
incomes = [1000000, 1500000, 1700000, 2300000, 2800000, 3200000, 4500000]
fig, axs = plt.subplots(1,1)
# data=[Bar(x=years,y=incomes)]
axs.scatter(x=years,y=incomes)
axs.bar(years,height=incomes)
axs.plot(years,incomes)
plt.show()
