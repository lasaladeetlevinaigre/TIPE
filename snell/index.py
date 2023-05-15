from engine import ComputeTrajectory, bcolors
import matplotlib.pyplot as plt
import random

def generate_random_hex_color(opacity):
    # Generate three random integers between 0 and 255
    r = int(random.uniform(128, 255))
    g = int(random.uniform(128, 255))
    b = int(random.uniform(128, 255))

    # Convert the integers to hexadecimal and format them
    hex_color = "#{:02x}{:02x}{:02x}{:02x}".format(r, g, b, int(opacity*255))
    return hex_color


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

            'alpha': random.uniform(45, 90),
            'theta': random.uniform(45, 90),
            
            'x0': 2,
            'y0': 2,
            'h0': 2.3,

            'v0_norme': [20, 20, 20],
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
    color_tab = []

    i = 0

    for params in params_tab:
        #print(i,"-"*50)

        trajectory = ComputeTrajectory(params)
        reussite = trajectory.compute_trajectory()
        t, x, y, z, v = trajectory.get_trajectory()
        ts.append(t)
        xs.append(x)
        ys.append(y)
        zs.append(z)
        vs.append(v)

        if reussite:
            clr = generate_random_hex_color(1)
            state = True
            #print(f"{bcolors.OKBLUE}[OK] Affichage{bcolors.ENDC}")
            pass
        else:
            clr = generate_random_hex_color(0.6)
            state = False
            pass
        reussite_tab.append(state)
        color_tab.append(clr)

        i = i + 1

    return ts, xs, ys, zs, vs, reussite_tab, color_tab




num_params = 20000
ok = 0
no = 0

params_tab = generate_random_params(num_params)
ts, xs, ys, zs, vs, reussite_tab, color_tab = compute_multiple_trajectories(params_tab)


ploting = False

for i in range(len(reussite_tab)):
    if reussite_tab[i] == True:
        ok = ok + 1
        if ploting:
            print(f"#{i}", end=" ")
    else:
        no = no + 1


print(f"{bcolors.OKCYAN}Pourcentage de réussite : {ok/(ok+no)*100:05.2f}% ({ok}/{(ok+no)}){bcolors.ENDC}")
print(f"{bcolors.FAIL}Pourcentage d'échec     : {no/(ok+no)*100:05.2f}% ({no}/{(ok+no)}){bcolors.ENDC}")

if ploting:
    fig = plt.figure(figsize=(14, 4))
    # Graphe des coordonnées x
    plt.subplot(131)
    for i in range(len(ts)):
        t = ts[i]
        x = xs[i]
        plt.plot(t, x, label=i, color=color_tab[i])
    plt.xlabel("Temps (s)")
    plt.ylabel("Coordonnée x")
    plt.ylim(0, max(longueur_terrain, largeur_terrain))
    plt.title("Trajectoire en x")
    plt.legend()

    # Graphe des coordonnées y
    plt.subplot(132)
    for i in range(len(ts)):
        t = ts[i]
        y = ys[i]
        plt.plot(t, y, color=color_tab[i])
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
        plt.plot(t, z, color=color_tab[i])
    plt.xlabel("Temps (s)")
    plt.ylabel("Coordonnée z")
    plt.title("Trajectoire en z")

    # Ajuster l'espacement entre les sous-graphiques
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(len(ts)):
        x = xs[i]
        y = ys[i]
        z = zs[i]
        ax.plot(x, y, z, color=color_tab[i])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim(0, max(longueur_terrain, largeur_terrain))
    ax.set_ylim(0, max(longueur_terrain, largeur_terrain))
    ax.set_zlim(0)

    plt.title("Trajectoire de la balle contre un mur perpendiculaire")

    plt.show()
