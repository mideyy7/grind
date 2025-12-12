import matplotlib.pyplot as plt
import numpy as np


x = np.array([1,2,3,4,5,6,7,8,9])
y = np.array([10,20,30,40,50,60,70,80, 90])

style = dict(marker = ".", ms = 10, markerfacecolor = "red", markeredgecolor = "red", linestyle = "dotted", linewidth = 2, color = "purple")
plt.show()


print(style)
plt.plot(x,y, **style)
plt.show()