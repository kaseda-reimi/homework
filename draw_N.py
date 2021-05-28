import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
plt.figure(0)
plt.title('logistic map')
plt.plot(x, 4*x*(1-x))
plt.plot(x, x*(1-x))
plt.xlabel('x')
plt.ylabel('y')
plt.legend(["r=4", "r=1"])
plt.show()
