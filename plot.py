import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv




def read_csv(path):
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        x = []
        y = []
        z = []
        t = []
        for line in reader:
            if (len(line) == 5):
                tp1 = float(line[0])
                tp2 = float(line[1])
                dt = float(line[2])
                nb = int(line[3])
                reussite = int(line[4])
            else :
                x.append(float(line[0]))
                y.append(float(line[1]))
                z.append(float(line[2]))
                t.append(float(line[3]))
    return x, y, z, t, tp1, tp2, dt, nb, reussite

path = "./data.csv"

x, y, z, t, tp1, tp2, dt, nb, reussite = read_csv(path)

"""
t1 = np.linspace(0, tp1, tp1/dt)
t2 = np.linspace(tp1, tp2, (tp2-tp1)/dt)
t3 = np.linspace(tp2, t[nb-1], (t[nb-1]-tp2)/dt)

t1 = [t*dt for t in range(0, int(tp1/dt))]
t2 = [t*dt for t in range(int(tp1/dt), int( (tp2)/dt ))]
t3 = [t*dt for t in range(int(tp2/dt), int((t[nb-1]-tp2)/dt))]
"""

# Graphe des coordonnées x
plt.subplot(131)
plt.plot(t, x, label="Partie 1")
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée x")
plt.title("Trajectoire en x")
plt.legend()

# Graphe des coordonnées y
plt.subplot(132)
plt.plot(t, y, label="Partie 1")
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée y")
plt.title("Trajectoire en y")
plt.legend()

# Graphe des coordonnées z
plt.subplot(133)
plt.plot(t, z, label="Partie 1")
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée z")
plt.title("Trajectoire en z")
plt.legend()

plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("Trajectoire de la balle contre un mur perpendiculaire")
plt.show()
