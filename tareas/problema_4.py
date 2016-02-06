import numpy as np
import matplotlib.pyplot as plt

plt.figure()

theta = np.linspace(0.0, 2.0*np.pi, 100)

k = 1
n_side = 5
for a in range(n_side):
    for b in range(n_side):
        plt.subplot(n_side,n_side,k)
        x = np.sin((a+1) * theta)
        y = np.sin((b+1) * theta)
        k += 1

        plt.plot(x,y)
        plt.axis("off") 
        plt.axis("equal")

plt.savefig('lissajous.pdf')
