import math
n_puntos = 21
L = 1.0
for x in range(n_puntos):
    pos_x = x * L/2.0/(n_puntos-1)
    pos_y = math.sqrt((L/2.0)**2 - pos_x**2)
    print pos_x, pos_y
