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


largeur_heatmap = 10
longueur_heatmap = 20
pas_distance = 1#m


nb_alphas = 20
nb_thetas = 20
def get_params_tab(x, y):   
    params_tab = []

    alphas = np.linspace(40, 160, nb_alphas)
    thetas = np.linspace(0, 180, nb_thetas)

    for alpha in alphas:
        for theta in thetas:
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

                'alpha': alpha,
                'theta': theta,
                
                'x0': x,
                'y0': y,
                'h0': h0,

                'v0_norme': [v0, v0, v0],
            }

            params_tab.append(params)

    return params_tab



# --------------------
ts = []
xs = []
ys = []
zs = []
vs = []
reussite_tab = []
color_tab = []
# --------------------

def compute_single_trajectory(param):
    trajectory = ComputeTrajectory(param)
    reussite = trajectory.compute_trajectory()

    if( (param["x0"] == 0) and (param["y0"] == 0)  ):
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

def get_probability(x, y, nb_rays_succ):
    params_tab = get_params_tab(x, y)

    somme = 0
    i = 0
    for param in params_tab:
        if compute_single_trajectory(param):
            nb_rays_succ = nb_rays_succ + 1
            somme = somme + 1
        i = i + 1

    return (round((somme/i)*100)/100, nb_rays_succ)


def generating_heatmap(v0, h0):
    # matrices heatmap
    heat_map = [ [ -1 for j in range(round(largeur_heatmap/pas_distance)) ] for i in range(round(longueur_heatmap/pas_distance)) ]

    nb_rays_succ = 0
    for i in range(len(heat_map)):
        for j in range(len(heat_map[i])):
            heat_map[i][j], nb_rays_succ = get_probability(i*pas_distance, j*pas_distance, nb_rays_succ)




    nb_rays = nb_alphas * nb_thetas * round(largeur_heatmap/pas_distance) * round(longueur_heatmap/pas_distance)
    print(f"{bcolors.OKCYAN}Résultats pour [v0:{v0}, h0:{h0}]{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}Nombre de lancés : {nb_rays} dont {nb_rays_succ} succès{bcolors.ENDC}")


    # Conversion du tableau en tableau NumPy
    heat_map_np = np.array(heat_map)

    #plt.imshow(heat_map_np, cmap='hot', interpolation='none')
    plt.imshow(heat_map_np, cmap='hot', interpolation='bicubic')

    # Inversion des axes
    #plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()

    # Ajustement de la légende de l'axe X
    x_ticks = np.arange(0, largeur_heatmap, 1)  # Positions des graduations
    x_labels = np.arange(0, largeur_heatmap * pas_distance, pas_distance)  # Étiquettes des graduations en mètres
    plt.xticks(x_ticks, x_labels)

    # Ajustement de la légende de l'axe Y
    y_ticks = np.arange(0, longueur_heatmap, 1)  # Positions des graduations
    y_labels = np.arange(0, longueur_heatmap * pas_distance, pas_distance)  # Étiquettes des graduations en mètres
    plt.yticks(y_ticks, y_labels)

    # Ajout d'une barre de couleur pour représenter l'échelle des valeurs
    #plt.colorbar()

    plt.title(f"Heatmap pour [v0:{v0}, h0:{h0}]")
    plt.savefig(f"heatmaps/{v0},{h0}.png")


v0 = 17
h0 = 2.3
plt.figure(figsize=(3, 5))
generating_heatmap(v0, h0)
plt.show()

"""
for i in range(8, 30):
    v0 = i
    plt.clf()
    generating_heatmap(v0, h0)
"""

#plot(ts, xs, ys, zs, vs, reussite_tab, color_tab, largeur_terrain, longueur_terrain, False)