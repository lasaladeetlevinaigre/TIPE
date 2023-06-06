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

    thetas = np.linspace(0, 180, nb_thetas)
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
                'e1': 0.4,
                'e2': 0.8,
                'hauteur_mur1': 4,
                'hauteur_mur2': 2,

                'theta': theta,
                'phi': phi,
                
                'x0': x,
                'y0': y,
                'h0': h0,

                'v0_norme': v0,
            }

            params_tab.append(params)

    return params_tab



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
color_tab = []
reussite_tab = []



def compute_single_trajectory(param, i):
    trajectory = ComputeTrajectory(param)
    reussite = trajectory.compute_trajectory()

    if(False):
        t, x, y, z = trajectory.get_trajectory()
        ts.append(t)
        xs.append(x)
        ys.append(y)
        zs.append(z)
        reussite_tab.append(reussite)
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




# ~ 1min pour 500k lancés
# ~ 10sec pour 20k

pas = 1  # Pas entre chaque mesure
nb_thetas = 10
nb_phis = 10
print(f"{int(largeur_terrain*longueur_terrain*1/pas*nb_thetas*nb_phis)}l")

nb_rays_succ = 0
def generating_heatmap(v0, h0, save = False, dossier_sortie = False):
    st = time.time()
    global nb_rays_succ

    print("-"*35)

    print(f"{bcolors.HEADER}{bcolors.BOLD}v0 = {v0} ms{bcolors.ENDC}")
    nb_rays_succ = 0

    
    heat = np.zeros((longueur_terrain +1, largeur_terrain +1))

    for y in range(len(heat)):
        for x in range(len(heat[y])):
            if(y < longueur_terrain/2):
                heat[y][x] = get_probability(x, y)

    et = time.time()
    elapsed_time = et - st
    print(f"Calcul en {(elapsed_time):.3f}s")

    moyenne = np.mean(heat)

    plt.figure(figsize=(4.5, 6))
    plt.imshow(heat, cmap='hot', origin='lower', interpolation='bicubic')
    plt.colorbar()
    plt.xlabel('Largeur')
    plt.ylabel('Longueur')
    plt.title(f'Heatmap des probabilités pour {v0:.1f}m/s')


    nb_rays_tot = nb_thetas*nb_phis*longueur_terrain*largeur_terrain
    print(f"{bcolors.OKCYAN}{nb_rays_succ} lancés réussis sur {nb_rays_tot}{bcolors.ENDC}")

    print(f"Probabilité moyenne: {bcolors.BOLD}{moyenne:.8f}{bcolors.ENDC}")


    print("-"*35)

    #Enregistrement du fichier
    if save:
        nom_fichier = f"{v0}__{h0}.png"
        chemin_fichier = os.path.join(dossier_sortie, nom_fichier)
        plt.savefig(chemin_fichier)
    else:
        plt.show()
        #plot(ts, xs, ys, zs, reussite_tab, color_tab, largeur_terrain, longueur_terrain)


v0 = 40 #en m/s
h0 = 2.1 #en m
generating_heatmap(v0, h0)

"""
v0_tab = np.arange(2, 70+2, 2)
print(f"{bcolors.FAIL}Calcul de {len(v0_tab)} heatmaps{bcolors.ENDC} pour h0={h0}")

dossier_sortie = f"heatmaps/{int(time.time()%10e7)}"
os.makedirs(dossier_sortie, exist_ok=True)
for v0 in v0_tab:
    plt.clf()
    generating_heatmap(v0, h0, True, dossier_sortie)
"""