import numpy as np
import matplotlib.pyplot as plt

tsp = 3e-9
G = 1e-6
N0 = 2e18
tph = 1e-12
b = np.array([[1e-5], [1e-2], [1e-1], [0.5]])

logR = np.linspace(25, 29, 100)
R = 10**logR
Ne = (G*tsp*R+1/tph+(1-b)*N0 + np.sqrt((1/tph+(1-b)*G*N0-G*tsp*R)**2+4*b*G*tsp/tph*R))/(2*(1-b)*G)
logNe = np.log10(Ne)

Np = tph*R - (1-b)*tph/tsp*Ne
logNp = np.log10(Np)

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
