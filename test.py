import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = 30
phi = 75
g = 9.8
v0 = 12
h = 2.3
e1 = 0.4 # contre sol
e2 = 0.8 # contre vitre
x0 = 2
y0 = 6

t = 0
x_values = []
y_values = []
z_values = []




while True:

    vx = v0 * np.sin(theta * np.pi / 180) * np.cos(phi * np.pi / 180)
    vy = v0 * np.sin(theta * np.pi / 180) * np.sin(phi * np.pi / 180)
    vz = -g * t - v0 * np.cos(theta * np.pi / 180)


    x = v0 * np.sin(theta * np.pi / 180) * np.cos(phi * np.pi / 180) * t + x0
    y = v0 * np.sin(theta * np.pi / 180) * np.sin(phi * np.pi / 180) * t + y0
    z = -0.5 * g * (t**2) - v0 * np.cos(theta * np.pi / 180) * t + h

    
    x_values.append(x)
    y_values.append(y)
    z_values.append(z)
    if z < 0:
        break
    
    t += 0.01



t2 = np.linspace(0, 10, 1000)
x2 = e1 * vx * t2 + x_values[-1]
y2 = e1 * vy * t2 + y_values[-1]
z2 = -0.5 * g * (t2**2) - e1 * vz * t2

for i in range(len(t2)):
    if y2[i] > 20:
        break
    x_values.append(x2[i])
    y_values.append(y2[i])
    z_values.append(z2[i])


t3 = np.linspace(0, 10, 1000)
x3 = e2 * vx * t3 + x_values[-1]
y3 = -e2 * vy * t3 + y_values[-1]
z3 = -0.5 * g * (t3**2) - e2 * vz * t3 +z_values[-1]

for i in range(len(t3)):
    if z3[i] < 0:
        break
    x_values.append(x3[i])
    y_values.append(y3[i])
    z_values.append(z3[i])



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x_values, y_values, z_values)

ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_zlim(0)

plt.title("Trajectoire de la balle")

plt.show()
