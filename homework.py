import numpy as np
import matplotlib.pyplot as plt

tsp = 3e-9
G = 1e-6
N0 = 2e18
tph = 1e-12
b = np.array([[1e-5], [1e-2], [1e-1], [0.5]])

logR = np.linspace(25, 29, 100)
R = 10**logR
logR = np.log(R)
Ne = (-tsp*G*R-1/tph+G*(b-1)*N0)/(2*G*(b-1))
logNe = np.log(Ne)


plt.figure(0)
plt.plot(logR, logNe[0])
plt.plot(logR, logNe[1])
plt.xlabel('log R)')
plt.ylabel('log Ne')
plt.legend(["β=1e-5", "β=1e-2"])
plt.savefig("Ne.png")
