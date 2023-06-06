from engine import ComputeTrajectory, bcolors
import matplotlib.pyplot as plt
import random
import numpy as np
from ploting import compute_multiple_trajectories, plot
from matplotlib import colors

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


largeur_terrain = 10 #m
longueur_terrain = 20 #m




def get_params_tab(x, y):   
    params_tab = []

    thetas = np.linspace(40, 160, nb_thetas)
    phis = np.linspace(0, 180, nb_phis)

    for theta in thetas:
        for phi in phis:
            params = {
                't_max': 10,
                'print_tab': False,
                'print_step': False,
                'largeur_terrain': largeur_terrain,
                'longueur_terrain': longueur_terrain,
                'hauteur_filet': 0.9,
                'e1': 0.7,
                'e2': 0.7,
                'hauteur_mur1': 3,
                'hauteur_mur2': 2,

                'theta': theta,
                'phi': phi,
                
                'x0': x,
                'y0': y,
                'h0': h0,

                'v0_norme': [v0, v0, v0],
            }

            params_tab.append(params)

    return params_tab



# --------------------
global ts
ts = []
global xs
xs = []
global ys
ys = []
global zs
zs = []
global vs
vs = []
global reussite_tab
reussite_tab = []
color_tab = []
# --------------------

def compute_single_trajectory(param, i):
    trajectory = ComputeTrajectory(param)
    reussite = trajectory.compute_trajectory()

    if(param["x0"] == 2 and param["y0"] == 5):
        # --------------------
        t, x, y, z, v = trajectory.get_trajectory()
        ts.append(t)
        xs.append(x)
        ys.append(y)
        zs.append(z)
        vs.append(v)
        reussite_tab.append(reussite)
        # --------------------


    return reussite



def get_probability(x, y):
    global nb_rays_succ
    params_tab = get_params_tab(x, y)

    somme = 0
    i = 0
    for param in params_tab:
        if compute_single_trajectory(param, i):
            nb_rays_succ = nb_rays_succ + 1
            somme = somme + 1
        i = i + 1
    proba = round((somme/i)*100)/100

    print(f"[{x:.2f}, {y:.2f}]: {proba:.4f}")
    return proba



pas = 1  # Pas entre chaque mesure
nb_thetas = 6
nb_phis = 6

nb_rays_succ = 0
def generating_heatmap(v0, h0):
    global nb_rays_succ

    # Créer un tableau 2D de dimensions largeur_terrain x longueur_terrain rempli de zéros
    probabilites = np.zeros((largeur_terrain, longueur_terrain))

    for x in range(largeur_terrain):
        for y in range(longueur_terrain):
            probabilites[x][y] = get_probability(x, y)

    nb_rays = nb_thetas * nb_phis * int(largeur_terrain/pas) * int(longueur_terrain/pas)
    print(f"{bcolors.OKCYAN}Résultats pour [v0:{v0}, h0:{h0}]{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}Nombre de lancés : {nb_rays} dont {nb_rays_succ} succès{bcolors.ENDC}")

        # Afficher le terrain sous forme de heatmap
    plt.imshow(probabilites, cmap='hot', origin='lower')
    plt.colorbar()
    plt.xlabel('Longueur')
    plt.ylabel('Largeur')
    plt.title('Heatmap des probabilités')
    plt.show()

    """
    # Conversion du tableau en tableau NumPy
    heat_map_np = np.array(probabilites)
    print(heat_map_np)


    plt.figure(figsize=(3, 5))
    plt.imshow(heat_map_np, cmap='hot', interpolation='none')
    #plt.imshow(heat_map_np, cmap='hot', interpolation='bicubic')

    # Inversion des axes
    #plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()

    # Ajustement de la légende de l'axe X
    x_ticks = np.arange(0, int(largeur_terrain/pas), 1)  # Positions des graduations
    x_labels = np.arange(0, largeur_terrain, pas)  # Étiquettes des graduations en mètres
    plt.xticks(x_ticks, x_labels)

    # Ajustement de la légende de l'axe Y
    y_ticks = np.arange(0, int(longueur_terrain/pas), 1)  # Positions des graduations
    y_labels = np.arange(0, longueur_terrain, pas)  # Étiquettes des graduations en mètres
    plt.yticks(y_ticks, y_labels)

    plt.title(f"Heatmap pour [v0:{v0}, h0:{h0}]")
    plt.show()
    """

    #plot(ts, xs, ys, zs, vs, reussite_tab, color_tab, largeur_terrain, longueur_terrain)
    #plt.savefig(f"heatmaps/{v0},{h0}.png")


v0 = 23
h0 = 2.3
generating_heatmap(v0, h0)


"""
for i in range(8, 9):
    v0 = i
    plt.clf()
    #enerating_heatmap(v0, h0)
#   plot(ts, xs, ys, zs, vs, reussite_tab, color_tab, largeur_terrain, longueur_terrain, True)
"""