from engine import ComputeTrajectory, bcolors
import matplotlib.pyplot as plt
import random
from ploting import compute_multiple_trajectories, plot
import numpy as np
import time

largeur_terrain = 10
longueur_terrain = 20

h0 = 2.3
v0 = 70
params_tab = [
    {
        't_max': 10,
        'print_tab': False,
        'print_step': True,
        'largeur_terrain': largeur_terrain,
        'longueur_terrain': longueur_terrain,
        'hauteur_filet': 0.9,
        'e1': 0.24,
        'e2': 0.8,
        'hauteur_mur1': 3,
        'hauteur_mur2': 2,

        'theta': 75,
        'phi': 65,
        
        'x0': 1,
        'y0': 6,
        'h0': h0,

        'v0_norme': v0,
    }
]


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
plot(v0, ts, xs, ys, zs, reussite_tab, largeur_terrain, longueur_terrain, False)