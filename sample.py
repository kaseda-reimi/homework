import numpy as np
import matplotlib.pyplot as plt

print('Hello World!')
a = 2
b = 3
print(a+b)

try:
    n = 1000
    x = np.linspace(0, 30, n)
    y = np.sin(x)*np.exp(-x/10)
    plt.plot(x, y)
    plt.title('Sample Output')
    plt.savefig("sample.png")
    print('Accepted')

except:
    print('Error : Some Module are not installed!')