from engine import ComputeTrajectory, bcolors
import matplotlib.pyplot as plt
import random
from ploting import compute_multiple_trajectories, plot


largeur_terrain = 10
longueur_terrain = 20

def generate_random_params(num_params):
    params_tab = []

    for _ in range(num_params):
        params = {
            't_max': 8,
            'print_tab': False,
            'print_step': True,
            'largeur_terrain': largeur_terrain,
            'longueur_terrain': longueur_terrain,
            'hauteur_filet': 0.9,
            'e1': 0.7,
            'e2': 0.7,
            'hauteur_mur1': 3,
            'hauteur_mur2': 2,

            'alpha': 122.105,
            'theta': 85.263,
            
            'x0': 9,
            'y0': 9,
            'h0': 2.3,

            'v0_norme': [13, 13, 13],
        }

        params_tab.append(params)

    return params_tab



num_params = 1

params_tab = generate_random_params(num_params)
ts, xs, ys, zs, vs, reussite_tab, color_tab = compute_multiple_trajectories(params_tab)

if num_params > 75:
    ploting = False
else:
    ploting = True

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

# Courbes
if ploting:
    plot(ts, xs, ys, zs, vs, reussite_tab, color_tab, largeur_terrain, longueur_terrain, False)