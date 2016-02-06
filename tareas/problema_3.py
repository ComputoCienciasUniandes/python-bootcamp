import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c, d):
    return a * np.sin(b * x + c ) + d

datos = np.loadtxt("monthrg.dat")
n_manchas_total = datos[:,3]
tiempo_total = datos[:,0] + (datos[:,1]-1.0)/12.0

n_manchas = n_manchas_total[n_manchas_total>0]
tiempo = tiempo_total[n_manchas_total>0]

popt, pcov = curve_fit(func, tiempo, n_manchas)

print popt

