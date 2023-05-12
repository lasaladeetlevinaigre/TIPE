import matplotlib.pyplot as plt
import numpy as np

"""
^ Uy
|
|
|
|
O--------> Ux
Uz vers nous
"""


g = 9.81
y_mur = 10 # en metres à partir du JOUEUR


# Définition des fonctions pour chaque partie de la trajectoire
def part1(t, v0):
    x = v0[0] * t
    y = v0[1] * t
    z = v0[2] * t**2
    return x, y, z

def part2(t, v0):
    x = v0[0] + v0[0] * t
    y = v0[1] + v0[1] * t
    z = v0[2] + v0[2] * t - 0.5 * 9.81 * t**2
    return x, y, z

def part3(t, v0):
    x = v0[0] + v0[0] * t + 0.5 * 2 * t**2
    y = v0[1] + v0[1] * t
    z = v0[2] + v0[2] * t - 0.5 * 9.81 * t**2
    return x, y, z

# Vecteur vitesse initial
v0 = [10, 5, 3]

# Création de la liste des temps pour chaque partie de la trajectoire
t1 = np.linspace(0, 1, 50)
t2 = np.linspace(1, 2, 50)
t3 = np.linspace(2, 3, 50)

# Création des listes des coordonnées x, y et z pour chaque partie de la trajectoire
x1, y1, z1 = zip(*[part1(t, v0) for t in t1])
x2, y2, z2 = zip(*[part2(t, v0) for t in t2])
x3, y3, z3 = zip(*[part3(t, v0) for t in t3])

# Affichage des graphes des coordonnées x, y et z en fonction du temps
plt.figure(figsize=(12, 4))



"""
xmax_ter = 20
ymax_ter = 40
t_graph_x = [0, 0, xmax_ter, xmax_ter, 0]
t_graph_y = [0, ymax_ter, ymax_ter, 0, 0]
plt.plot(t_graph_x, t_graph_y, '-k')
"""

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
