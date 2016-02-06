import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c, d):
    return a * np.sin(b * x + c ) + d

datos = np.loadtxt("monthrg.dat")
n_manchas_total = datos[:,3]
tiempo_total = datos[:,0] + (datos[:,1]-1.0)/12.0

n_manchas = n_manchas_total[(n_manchas_total>0) & (tiempo_total>1950)]
tiempo = tiempo_total[(n_manchas_total>0) & (tiempo_total>1950)]

popt, pcov = curve_fit(func, tiempo, n_manchas)

import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes()

ax.set_xlabel("Time [years]")
ax.set_ylabel("Spot number")
ax.set_title("Comparison")

plt.scatter(tiempo, n_manchas, label="Observations", s=0.1)

x = np.linspace(np.amin(tiempo), np.amax(tiempo), 2000)
y = func(x, popt[0], popt[1], popt[2], popt[3])
plt.plot(x, y, label="Fit!")

ax.legend()

plt.savefig('resultados.pdf')
plt.close()


print popt

