import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, norm, centro, sigma):
    return norm * np.exp(-(x-centro)**2/(2.0*sigma**2))

def get_sigma(n_points=2):
    n_series = 5000

    series_sum = np.zeros(n_series)
    for i in range(n_series):
        serie = 2.0*np.random.random(n_points) - 1.0
        series_sum[i] = np.sum(serie)
    

    #valores numericos del histograma y ajuste
    histo, edges = np.histogram(series_sum, bins=20)
    centros = 0.5 * (edges[0:-1] + edges[1:])
    popt, pcov = curve_fit(func, centros, histo)

    plt.figure()
    name = "np= {} ns={}".format(n_points,n_series)
    histo = plt.hist(series_sum, bins=20,alpha=0.2, histtype="stepfilled", label=name)
    x = np.linspace(np.min(series_sum), np.max(series_sum),100)
    fit_name = "fit sigma={}".format(popt[2])
    plt.plot(x, func(x, popt[0], popt[1], popt[2]), label=fit_name)
    plt.legend()
    filename = "experiment_{}_{}.pdf".format(n_points, n_series)
    plt.savefig(filename)

    return np.abs(popt[2])

npoints = np.array([2,10,20,100,200,500,1000])
nsigma = np.zeros(len(npoints))
for i in range(len(npoints)):
    nsigma[i] = get_sigma(n_points=npoints[i])
    print npoints[i], nsigma[i]

plt.figure()
plt.scatter(npoints, nsigma, label='experiment')
x = np.linspace(0,2000,100)
plt.plot(x, np.sqrt(x), label='theory')
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.savefig("all_series.pdf")

