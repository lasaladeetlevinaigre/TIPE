from engine import ComputeTrajectory, bcolors
import matplotlib.pyplot as plt
import os
import random
import time
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
                'hauteur_mur1': 4,
                'hauteur_mur2': 3,

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

    if(False):
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
    proba = somme/i

    #print(f"[{x:.2f}, {y:.2f}]: {proba:.4f}")
    return proba





pas = 1  # Pas entre chaque mesure
nb_alphas = 24
nb_thetas = 24

nb_rays_succ = 0
def generating_heatmap(v0, h0, save = False, dossier_sortie = False):
    st = time.time()
    global nb_rays_succ
    nb_rays_succ = 0
    heat = np.zeros((longueur_terrain +1, largeur_terrain +1))

    for y in range(len(heat)):
        for x in range(len(heat[y])):
            if(y < longueur_terrain/2):
                heat[y][x] = get_probability(x, y)

    moyenne = np.mean(heat)

    plt.figure(figsize=(4.5, 6))
    plt.imshow(heat, cmap='hot', origin='lower', interpolation='none')
    plt.colorbar()
    plt.xlabel('Largeur')
    plt.ylabel('Longueur')
    plt.title(f'Heatmap des probabilités pour {v0:.1f}m/s')

    print("-"*35)
    print(f"{bcolors.HEADER}{bcolors.BOLD}v0 = {v0} ms{bcolors.ENDC}")

    nb_rays_tot = nb_alphas*nb_thetas*longueur_terrain*largeur_terrain
    print(f"{bcolors.OKCYAN}{nb_rays_succ} lancés réussis sur {nb_rays_tot}{bcolors.ENDC}")

    print(f"Probabilité moyenne: {bcolors.BOLD}{moyenne:.8f}{bcolors.ENDC}")

    et = time.time()
    elapsed_time = et - st
    print(f"Calcul en {(elapsed_time):.3f}s")

    #Enregistrement du fichier
    if save:
        nom_fichier = f"{v0}__{h0}.png"
        chemin_fichier = os.path.join(dossier_sortie, nom_fichier)
        plt.savefig(chemin_fichier)
    else:
        plt.show()

        #plot(ts, xs, ys, zs, vs, reussite_tab, color_tab, largeur_terrain, longueur_terrain)


v0 = 50 #en m/s
h0 = 2.4 #en m
#generating_heatmap(v0, h0)


v0_tab = np.arange(2, 70+2, 2)
print(f"{bcolors.FAIL}Calcul de {len(v0_tab)} heatmaps{bcolors.ENDC} pour h0={h0}")

dossier_sortie = f"heatmaps/{int(time.time()%10e7)}"
os.makedirs(dossier_sortie, exist_ok=True)
for v0 in v0_tab:
    plt.clf()
    generating_heatmap(v0, h0, True, dossier_sortie)
