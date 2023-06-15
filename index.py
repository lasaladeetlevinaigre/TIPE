from engine import ComputeTrajectory, bcolors
import matplotlib.pyplot as plt
import random
from ploting import compute_multiple_trajectories, plot
import numpy as np
import time

largeur_terrain = 10
longueur_terrain = 20

def get_params_tab(x, y, h0, v0):   
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


nb_thetas = 20*2
nb_phis = 20*2

h0 = 2.3
v0 = 40
params_tab = get_params_tab(4, 9, h0, v0)


ts = []
xs = []
ys = []
zs = []
reussite_tab = []
print(f"{bcolors.HEADER}{bcolors.BOLD}v0 = {v0} ms{bcolors.ENDC}")

st = time.time()

for param in params_tab:

    trajectory = ComputeTrajectory(param)
    reussite = trajectory.compute_trajectory()
    t, x, y, z = trajectory.get_trajectory()

    ts.append(t)
    xs.append(x)
    ys.append(y)
    zs.append(z)


    reussite_tab.append(reussite)

# Pourcentages
ok = 0
no = 0
for i in range(len(reussite_tab)):
    if reussite_tab[i] == True:
        ok = ok + 1
    else:
        no = no + 1
print(" ")

if ok == 0:
    print(f"{bcolors.OKCYAN}Pourcentage de réussite : {ok/(ok+no)*100:06.2f}% ({ok}/{(ok+no)}){bcolors.ENDC}")
else:
    print(f"{bcolors.OKCYAN}Pourcentage de réussite : {ok/(ok+no)*100:05.2f}% ({ok}/{(ok+no)}){bcolors.ENDC}")
print(f"{bcolors.FAIL}Pourcentage d'échec     : {no/(ok+no)*100:05.2f}% ({no}/{(ok+no)}){bcolors.ENDC}")

et = time.time()
elapsed_time = et - st
print(f"Calcul en {(elapsed_time):.3f}s")   
# Courbes
plot(ts, xs, ys, zs, reussite_tab, largeur_terrain, longueur_terrain, True)