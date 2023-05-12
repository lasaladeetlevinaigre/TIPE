import matplotlib.pyplot as plt
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
                reussite = int(line[4))
            else :
                x.append(float(line[0]))
                y.append(float(line[1]))
                z.append(float(line[2]))
                t.append(float(line[3]))
    return x, y, z, t1, t2, dt

path = "./data.csv"

x, y, z, t, tp1, tp2, dt, nb, reussite = read_csv(path)


t1 = np.linspace(0, tp1, tp1/dt)
t2 = np.linspace(tp1, tp2, (tp2-tp1)/dt)
t3 = np.linspace(tp2, t[nb-1], 



# Graphe des coordonnées x
plt.subplot(131)
plt.plot(t1, x1, label="Partie 1")
plt.plot(t2, x2, label="Partie 2")
plt.plot(t3, x3, label="Partie 3")
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée x")
plt.title("Trajectoire en x")
plt.legend()

# Graphe des coordonnées y
plt.subplot(132)
plt.plot(t1, y1, label="Partie 1")
plt.plot(t2, y2, label="Partie 2")
plt.plot(t3, y3, label="Partie 3")
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée y")
plt.title("Trajectoire en y")
plt.legend()

# Graphe des coordonnées z
plt.subplot(133)
plt.plot(t1, z1, label="Partie 1")
plt.plot(t2, z2, label="Partie 2")
plt.plot(t3, z3, label="Partie 3")
plt.xlabel("Temps (s)")
plt.ylabel("Coord")
plt.title("Trajectoire en z")
plt.legend()

plt.show()
