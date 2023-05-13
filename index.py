import matplotlib.pyplot as plt
import numpy as np

g = 9.81
h0 = 2
y_mur = 8
v0_norme = 7
theta = 45 #angle entre Ux et v0
alpha = 90 #angle entre Uz et v0



"""
^ Uy
|
|   ^ v0
|  /
| /
O--------> Ux
Uz vers nous
"""


v0 = [-1, -1, -1]
v0[0] = v0_norme * np.cos(theta * np.pi / 180)
v0[1] = v0_norme * np.sin(theta * np.pi / 180)
v0[2] = v0_norme * np.cos(alpha * np.pi / 180)

x0 = 0
y0 = 0



t_tab = []
x_tab = []
y_tab = []
z_tab = []
v_tab = []
dt = 0.01 # integrate in hundredths of a second


t_rebond1 = -1
t_rebond2 = -1
x_rebond1 = -1
i_rebond1 = -1

t_zmax = -1

def print_tab(tab):
    for i in range(len(tab)):
        print("t:",t_tab[i], "  x:",x_tab[i], "  y:",y_tab[i], "  z:",z_tab[i], "  v:",v_tab[i])


def part1():
    global t_rebond1
    global x_rebond1
    global i_rebond1

    t = 0
    i = 0

    x_tab.append(0)
    y_tab.append(0)
    z_tab.append(h0)
    t_tab.append(0)
    v_tab.append(v0)
    t = t + dt

    while True:

        x = v0[0] * t + x0
        y = v0[1] * t + y0
        z = h0 + v0[2] * t - 1/2*g * t**2

        if z >= z_tab[-1]:
            t_zmax = t

        if z <= 0 or t > t_max:
            print("Premier rebond à ", t, "sec")
            t_rebond1 = t
            x_rebond1 = x
            i_rebond1 = i
            return t


        x_tab.append(x)
        y_tab.append(y)
        z_tab.append(z)
        t_tab.append(t)
        v_tab.append([v0[0], v0[1], v0[2]])
        t = t + dt
        i = i+1


def part2():
    t = t_tab[-1] + dt
    e = 1.3

    while True:

        v1 = v0_norme * 1 # = np.cos(alpha = 0)

        x = v0[0] * t + x0
        y = v0[1] * t + y0

        t_prim = -t + 2 * t_rebond1
        z = e*(h0 + v0[2] * t_prim - 1/2*g * t_prim**2)



        if y >= y_mur or t > t_max:
            print("Deuxième rebond à ", t, "sec")
            t_rebond2 = t
            return t


        x_tab.append(x)
        y_tab.append(y)
        z_tab.append(z)
        t_tab.append(t)
        v_tab.append([v0[0], v0[1], v0[2]])
        t = t + dt


t_max = 8
part1()
part2()
#print_tab(z_tab)

# Graphe des coordonnées x
plt.subplot(131)
plt.plot(t_tab, x_tab, label="x")
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée x")
plt.title("Trajectoire en x")
plt.legend()

# Graphe des coordonnées y
plt.subplot(132)
plt.plot(t_tab, y_tab, label="y")
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée y")
plt.title("Trajectoire en y")
plt.legend()

# Graphe des coordonnées z
plt.subplot(133)
plt.plot(t_tab, z_tab, label="z")
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée z")
plt.title("Trajectoire en z")
plt.legend()

plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_tab, y_tab, z_tab)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("Trajectoire de la balle contre un mur perpendiculaire")
plt.show()