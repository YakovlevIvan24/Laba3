import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('classic')


vector1 = np.array([1,2,3]) # Создаем вектор
vector2 = np.array([4,5,6])

dot = np.dot(vector1, vector2) # скалярное произведение

#norm = np.linalgm.norm(vector1)

#-----------------------------------------------------------------------------------------------

z = np.linspace(1, 10, 20)

x = np.linspace(0, 10, 101)

y = np.sin(x)

T1 = time.perf_counter() # функция фиксирует текущее значение времени

plt.scatter(x, y) # Функция наносит на графиг точки из массивов
plt.show()

T2 = time.perf_counter()
print(f'{T2-T1:0.5f}')


plt.plot(x,y) # функция строит непрерывный график
plt.show()

#--------------------------------------------------------------------------------------------------

a = np.array([1,2,3])
b = np.array([1,5,5])
c = np.array([1,5,2])

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel("x") # подпишем ось x
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.scatter(a, b, c)
plt.show()

#--------------------------------------------------------------------------------------------------

t = np.linspace(0, 10, 1000)
d = np.sin(t)
e = np.cos(t)
f = t

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot(d, e, f)
plt.show()


#----------------------------------------------------------------------------------------------------

T1 = time.perf_counter()
x = np.sin(t)
y = t
z = t

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot(x, y, z)
T2 = time.perf_counter()
plt.show()
print(f'{T2-T1:0.5f}')