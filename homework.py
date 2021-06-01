import numpy as np
import matplotlib.pyplot as plt

tsp = 3e-9
G = 1e-6
N0 = 2e18
tph = 1e-12
b = np.array([[1e-5], [1e-2], [1e-1], [0.5]])

logR = np.linspace(25, 29, 100)
R = 10**logR
Z = -tsp*G*R-1/tph+G*(b-1)*N0
Ne =(Z-np.sqrt(Z**2+4*tsp/tph*G*R*b))/(2*G*(b-1))
logNe = np.log10(Ne)

Np = tph*R+tph/tsp*(b-1)*Ne

plt.figure(0)
plt.plot(logR, logNe[0])
plt.plot(logR, logNe[1])
plt.plot(logR, logNe[2])
plt.plot(logR, logNe[3])
plt.xlabel('log R)')
plt.ylabel('log Ne')
plt.legend(["β=1e-5", "β=1e-2", "β=1e-1", "β=0.5"])
plt.savefig("Ne.png")

plt.figure(1)
plt.plot(logR, logNp[0])
plt.plot(logR, logNp[1])
plt.plot(logR, logNp[2])
plt.plot(logR, logNp[3])
plt.xlabel('log R)')
plt.ylabel('log Np')
plt.legend(["β=1e-5", "β=1e-2", "β=1e-1", "β=0.5"])
plt.savefig("Np.png")