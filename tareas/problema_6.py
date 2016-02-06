import numpy as np
import matplotlib.pyplot as plt

def escape(lbox=10.0, lstep=1.0):

#    x = np.random.random() * lbox
#    y = np.random.random() * lbox
    x = 0.5 * lbox
    y = 0.5 * lbox
    n_step = 0 
    while((x<lbox) and (y<lbox) and (x>0) and (y>0)):
        theta = 2.0 * np.pi * np.random.random()
        x = x + lstep * np.cos(theta)
        y = y + lstep * np.sin(theta)
        n_step = n_step + 1
    return n_step

lstep = 1.0
lbox =  20.0 * lstep
n_points = 1000
lista_escape = np.zeros(n_points)
for i in range(n_points):
    lista_escape[i] = escape(lstep=lstep, lbox=lbox)


plt.figure()
name = "lbox={}".format(lbox)
histo = plt.hist(lista_escape, bins=20, alpha=0.2, 
                 histtype="stepfilled", label=name)
plt.legend()
plt.savefig("escape.pdf")

