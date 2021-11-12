from math import sqrt
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

y0 = 1.4076
p0 = 10**5
k = 1.380649e-23
Na = 6.02e+23
R = Na * k
Mco2 = 44.01e-3
Mh2o = 18.01
Ma = 28.97e-3
temperature = 296
s = []

co2Max = 0.01
h2oX = np.linspace(6.695e-3, 13.2252e-3, 101)

#speed = sqrt(y0 * ((p0 * R * temperature * Na) / (Ma * p0 * Na + Mco2 * co2Max * R * temperature + h2oX * R * temperature * Na)))

for i in range(101):
    s.append(sqrt(y0 * ((p0 * R * temperature * Na) / (Ma * p0 * Na + Mco2 * co2Max * R * temperature + h2oX[i] * R * temperature * Na))))
plt.plot(h2oX, s) # Функция наносит на графиг точки из массивов
plt.show()




