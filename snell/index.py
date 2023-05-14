from engine import ComputeTrajectory, bcolors
import matplotlib.pyplot as plt
import random

largeur_terrain = 10
longueur_terrain = 20
def generate_random_params(num_params):
    params_tab = []

    for _ in range(num_params):
        params = {
            't_max': 8,
            'print_tab': False,
            'print_step': False,
            'largeur_terrain': largeur_terrain,
            'longueur_terrain': longueur_terrain,
            'e1': 1.6,
            'e2': 1.6,
            'hauteur_mur1': 3,
            'hauteur_mur2': 2,
            'alpha': random.uniform(60, 120),
            'x0': 2,
            'y0': 2,
            'h0': 2.3,
            'v0_norme': [20, 20, 20],
            'theta': random.uniform(60, 90),
        }

        params_tab.append(params)

    return params_tab

def compute_multiple_trajectories(params_tab):
    ts = []
    xs = []
    ys = []
    zs = []
    vs = []
    reussite_tab = []

    for params in params_tab:
        trajectory = ComputeTrajectory(params)
        reussite = trajectory.compute_trajectory()
        t, x, y, z, v = trajectory.get_trajectory()
        ts.append(t)
        xs.append(x)
        ys.append(y)
        zs.append(z)
        vs.append(v)

        if reussite:
            clr = "c"
            print(f"{bcolors.OKBLUE}[OK] On garde{bcolors.ENDC}")
        else:
            clr = "#8a8a8a66"
        reussite_tab.append(clr)

    return ts, xs, ys, zs, vs, reussite_tab




num_params = 150
params_tab = generate_random_params(num_params)
ts, xs, ys, zs, vs, reussite_tab = compute_multiple_trajectories(params_tab)


# Graphe des coordonnées x
plt.subplot(131)
for i in range(len(ts)):
    t = ts[i]
    x = xs[i]
    #plt.plot(t, x, label= f"theta=%0.1f" % params_tab[i]['theta'])
    plt.plot(t, x, color=reussite_tab[i])
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée x")
plt.ylim(0, max(largeur_terrain, longueur_terrain))
plt.title("Trajectoire en x")
plt.legend()

# Graphe des coordonnées y
plt.subplot(132)
for i in range(len(ts)):
    t = ts[i]
    y = ys[i]
    plt.plot(t, y, color=reussite_tab[i])
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée y")
plt.ylim(0, max(longueur_terrain, largeur_terrain))
plt.title("Trajectoire en y")
plt.legend()

# Graphe des coordonnées z
plt.subplot(133)
for i in range(len(ts)):
    t = ts[i]
    z = zs[i]
    plt.plot(t, z, color=reussite_tab[i])
plt.xlabel("Temps (s)")
plt.ylabel("Coordonnée z")
plt.title("Trajectoire en z")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(len(ts)):
    x = xs[i]
    y = ys[i]
    z = zs[i]
    ax.plot(x, y, z, color=reussite_tab[i])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title("Trajectoire de la balle contre un mur perpendiculaire")

plt.show()
