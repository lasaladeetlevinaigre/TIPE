from engine import ComputeTrajectory, bcolors
import matplotlib.pyplot as plt
import random
from ploting import compute_multiple_trajectories, plot
import numpy as np

largeur_terrain = 10
longueur_terrain = 20

def get_params_tab(x, y):   
    params_tab = []

    alphas = np.linspace(40, 160, 20)
    thetas = np.linspace(0, 180, 20)

    h0 = 2.3
    v0 = 13

    for alpha in alphas:
        for theta in thetas:
            params = {
                't_max': 10,
                'print_tab': False,
                'print_step': True,
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


params_tab = get_params_tab(1, 2)
ts, xs, ys, zs, vs, reussite_tab, color_tab = compute_multiple_trajectories(params_tab)

# Pourcentages
ok = 0
no = 0
for i in range(len(reussite_tab)):
    if reussite_tab[i] == True:
        ok = ok + 1
        if ploting:
            print(f"#{i}", end=" ")
    else:
        no = no + 1
print(" ")
if ok == 0:
    print(f"{bcolors.OKCYAN}Pourcentage de réussite : {ok/(ok+no)*100:06.2f}% ({ok}/{(ok+no)}){bcolors.ENDC}")
else:
    print(f"{bcolors.OKCYAN}Pourcentage de réussite : {ok/(ok+no)*100:05.2f}% ({ok}/{(ok+no)}){bcolors.ENDC}")
print(f"{bcolors.FAIL}Pourcentage d'échec     : {no/(ok+no)*100:05.2f}% ({no}/{(ok+no)}){bcolors.ENDC}")

plot(ts, xs, ys, zs, vs, reussite_tab, color_tab, largeur_terrain, longueur_terrain, False)