import requests
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from math import sqrt
#ip = '192.168.212.35' # Usually 192.168.212.X. Find X in oscilloscope settings

#if (ip == ''):
 #   print('Setup ip-address of Tekronix oscilloscope')
  #  quit()

#url = 'http://' + ip + '/Image.png'
#r = requests.get(url, allow_redirects=True)

#open('tektronix2.png', 'wb').write(r.content)


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
h2oX = np.linspace(0.325, 0.642, 101)
def speed(h2oX):
    return sqrt(y0 * ((p0 * R * temperature * Na) / (Ma * p0 * Na + Mco2 * co2Max * R * temperature + h2oX * R * temperature * Na)))


for i in range(101):
    s.append(speed(h2oX[i]))
#plt.scatter(h2oX, s) # Функция наносит на графиг точки из массивов
















#with open("/home/gr102/Desktop/Scripts/belkina-repo/settings.txt", "r") as settings:
 #   tmp=[float(i) for i in settings.read().split("\n")]

#data_array = np.loadtxt("/home/gr102/Desktop/Scripts/belkina-repo/data.txt", dtype=int)

fig, ax = plt.subplots(figsize=(16,10), dpi=400)

#time_array = []
#concet_air = 
#concet_breath = 
#markers = [concet_air, concet_breath]

ax.plot(h2oX, s, "m", linewidth = '1.0', marker = 'H', markevery=10, markersize = '5.0')

ax.set_xlim([min(h2oX), 1.1*max(h2oX)])
ax.set_ylim([min(s), 1.1*max(s)])

plt.title("График зависимости скорости звука от концетрации CO2", fontstyle = 'italic', horizontalalignment = 'center')
plt.xlabel("Концетрация CO2, n %")
plt.ylabel("Скорость звука, v м/c")
plt.legend("v(n)")

plt.grid(which='major', color='gray', linestyle='-', linewidth = 0.5)
plt.grid(which='minor', color='gray', linestyle='--', linewidth = 0.25)

#plt.text(20, 1, "Время зарядки = 16.08 с ", fontstyle = 'italic', fontsize = 'small')
#plt.text(20, 0.95, "Время разрядки = 9.52 с ", fontstyle = 'italic', fontsize = 'small')

plt.minorticks_on()

fig.savefig("graph_sound.svg")

plt.show()
