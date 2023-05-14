import matplotlib.pyplot as plt
import numpy as np


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'






g = 9.81

x0 = 2 #2
y0 = 2 #2
h0 = 2.3 #2.3

t_max = 60

v0_norme = [20, 20, 20] #20,20,20
theta = 80 #angle entre Ux et v0 #75
alpha = 90 #angle entre Uz et v0 #90
e = 1.6 #1.6

largeur_terrain = 8
longueur_terrain = 20
hauteur_mur1 = 3 #3
hauteur_mur2 = 2 #2


y_mur1 = longueur_terrain
z_mur1 = hauteur_mur1
x_mur2 = largeur_terrain
z_mur2 = hauteur_mur2


"""
^ Uy
|----------------- mur1 en face
|
|
|                 mur2 coté
|                 |
|   ^ v0          |
|  /              |
| /               |
O---------------------> Ux
Uz vers nous
"""


v0 = [-1, -1, -1]
v0[0] = v0_norme[0] * np.cos(theta * np.pi / 180)
v0[1] = v0_norme[1] * np.sin(theta * np.pi / 180)
v0[2] = v0_norme[2] * np.cos(alpha * np.pi / 180)



t_tab = []
x_tab = []
y_tab = []
z_tab = []
v_tab = []
dt = 0.01 # integrate in hundredths of a second


t_rebond1 = -1
x_rebond1 = -1
y_rebond1 = -1

t_rebond2 = -1
x_rebond2 = -1
y_rebond2 = -1
z_rebond2 = -1

t_rebond3 = -1
x_rebond3 = -1
y_rebond3 = -1
z_rebond3 = -1

zmax = -1

def print_tab(tab):
    for i in range(len(tab)):
        print("t:",t_tab[i], "  x:",x_tab[i], "  y:",y_tab[i], "  z:",z_tab[i], "  v:",v_tab[i])


def part1():
    global t_rebond1
    global x_rebond1
    global y_rebond1
    global zmax

    t = 0
    i = 0

    x_tab.append(x0)
    y_tab.append(y0)
    z_tab.append(h0)
    t_tab.append(0)
    v_tab.append(v0)
    t = t + dt

    while True:

        x = v0[0] * t + x0
        y = v0[1] * t + y0
        z = h0 + v0[2] * t - 1/2*g * t**2

        if z >= zmax:
            zmax = z


        if t > t_max:
            print(f"{bcolors.FAIL}[NO] Temps écoulé{bcolors.ENDC}")
            return 0

        if z <= 0:
            print("[OK] Premier rebond contre sol à %0.4f" % t, "sec")
            t_rebond1 = t
            x_rebond1 = x
            y_rebond1 = y
            return 1

        if x >= largeur_terrain or x <= 0:
            print(f"{bcolors.FAIL}[NO] La balle sort du terrain par les côtés{bcolors.ENDC}")
            return 0

        if y >= y_mur1:
            print(f"{bcolors.FAIL}[NO] La balle frappe le mur1 avant le sol{bcolors.ENDC}")
            x_tab.append(x)
            y_tab.append(y)
            z_tab.append(z)
            t_tab.append(t)
            return 0



        x_tab.append(x)
        y_tab.append(y)
        z_tab.append(z)
        t_tab.append(t)
        v_tab.append([v0[0], v0[1], v0[2]])
        t = t + dt
        i = i+1


def part2():
    global t_rebond2
    global x_rebond2
    global y_rebond2
    global z_rebond2
    global zmax

    t = t_tab[-1] + dt

    while True:
        x = v0[0] * t + x0
        y = v0[1] * t + y0

        t_prim = -t + 2 * t_rebond1
        z = e*(h0 + v0[2] * t_prim - 1/2*g * t_prim**2)

        if z >= zmax:
            zmax = z

        if z >= z_mur1:
            print(f"{bcolors.FAIL}[NO] La balle passe au dessus du mur1{bcolors.ENDC}")
            x_tab.append(x)
            y_tab.append(y)
            z_tab.append(z)
            t_tab.append(t)
            return 0

        if t > t_max:
            print(f"{bcolors.FAIL}[NO] Temps écoulé{bcolors.ENDC}")
            return 0

        if y >= y_mur1:
            print("[OK] Deuxième rebond contre mur1 à %0.4f" % t, "sec")
            t_rebond2 = t
            x_rebond2 = x
            y_rebond2 = y
            z_rebond2 = z
            return 1



        x_tab.append(x)
        y_tab.append(y)
        z_tab.append(z)
        t_tab.append(t)
        v_tab.append([v0[0], v0[1], v0[2]])
        t = t + dt


def part3():
    global t_rebond2

    global t_rebond3
    global x_rebond3
    global y_rebond3
    global z_rebond3
    global zmax

    t = t_tab[-1] + dt

    while True:
        x = v0[0] * t + x0

        y = -(v0[1] * t + y0) + 2*y_rebond2

        t_prim = -t + 2 * t_rebond1
        z = e*(h0 + v0[2] * t_prim - 1/2*g * t_prim**2)


        if z >= zmax:
            zmax = z

        if t > t_max:
            print(f"{bcolors.FAIL}[NO] Temps écoulé{bcolors.ENDC}")
            return 0

        if z <= 0:
            print(f"{bcolors.FAIL}[NO] La balle tombe avant de passer le mur2{bcolors.ENDC}")
            x_tab.append(x)
            y_tab.append(y)
            z_tab.append(z)
            t_tab.append(t)
            return 0

        if x >= x_mur2 and z >= z_mur2:
            print("[OK] Passe au dessus mur2 à %0.4f" % t, "sec")
            t_rebond2 = t
            return 1

        if x >= x_mur2 and z < z_mur2:
            print(f"{bcolors.FAIL}[NO] La balle frappe le mur2{bcolors.ENDC}")
            return 0



        x_tab.append(x)
        y_tab.append(y)
        z_tab.append(z)
        t_tab.append(t)
        v_tab.append([v0[0], v0[1], v0[2]])
        t = t + dt

if part1() == 1:
    if part2() == 1:
        if part3() == 1:
            print(f"{bcolors.OKGREEN}[OK] Réussite !{bcolors.ENDC}")
#print_tab(z_tab)

# Graphe des coordonnées x
plt.subplot(131)
plt.plot(t_tab, x_tab, label="x")
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée x")
plt.ylim(0, max(largeur_terrain, longueur_terrain))
plt.title("Trajectoire en x")
plt.legend()

# Graphe des coordonnées y
plt.subplot(132)
plt.plot(t_tab, y_tab, label="y")
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée y")
plt.ylim(0, max(largeur_terrain, longueur_terrain))
plt.title("Trajectoire en y")
plt.legend()

# Graphe des coordonnées z
plt.subplot(133)
plt.plot(t_tab, z_tab, label="z")
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée z")
plt.ylim(-max(zmax, z_mur1)/30, max(zmax, z_mur1)+ max(zmax, z_mur1)/30)
plt.title("Trajectoire en z")
plt.legend()

#plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_tab, y_tab, z_tab)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim(0, largeur_terrain)
ax.set_ylim(0, longueur_terrain)
ax.set_zlim(0, max(zmax, z_mur1))

plt.title("Trajectoire de la balle contre un mur perpendiculaire")
plt.show()