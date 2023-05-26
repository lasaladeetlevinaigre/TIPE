from engine import ComputeTrajectory, bcolors
import matplotlib.pyplot as plt
import random
import numpy as np
from ploting import compute_multiple_trajectories, plot
from matplotlib import colors


largeur_terrain = 10 #m
longueur_terrain = 20 #m
v0 = 20 #m/s
h0 = 2.3 #m


largeur_heatmap = 10
longueur_heatmap = 20
pas_distance = 1#m


def get_params_tab(x, y):
    params_tab = []

    interval_alpha = [85, 110] #ex : [80, 140]
    pas_alpha = 5              #ex : 5
    alphas = [interval_alpha[0] + pas_alpha*i for i in range( round((interval_alpha[1]-interval_alpha[0])/pas_alpha)+1 )]
    #ex t: [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140]

    interval_theta = [30, 85] #ex : [80, 140]
    pas_theta = 5              #ex : 5
    thetas = [interval_theta[0] + pas_theta*i for i in range( round((interval_theta[1]-interval_theta[0])/pas_theta)+1 )]
    #ex t: [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140]



    for i in range( len(alphas) ):
        for j in range( len(thetas) ):
            params = {
                't_max': 10,
                'print_tab': False,
                'print_step': False,
                'largeur_terrain': largeur_terrain,
                'longueur_terrain': longueur_terrain,
                'e1': 0.7,
                'e2': 0.7,
                'hauteur_mur1': 3,
                'hauteur_mur2': 2,

                'alpha': alphas[i],
                'theta': thetas[j],
                
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



def get_probability(x, y):
    params_tab = get_params_tab(x, y)

    somme = 0
    i = 0
    for param in params_tab:
        if compute_single_trajectory(param):
            somme = somme + 1
        i = i + 1

    return round((somme/i)*100)/100



# matrices heatmap
heat_map = [ [ -1 for j in range(round(largeur_heatmap/pas_distance)) ] for i in range(round(longueur_heatmap/pas_distance)) ]

for i in range(len(heat_map)):
    for j in range(len(heat_map[i])):
        pass
        heat_map[i][j] = get_probability(i*pas_distance, j*pas_distance)



# Conversion du tableau en tableau NumPy
heat_map_np = np.array(heat_map)


# Création de la heatmap avec Matplotlib
plt.imshow(heat_map_np, cmap='hot', interpolation='bicubic')

# Inversion de l'axe y
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
plt.colorbar()
plt.show()
#plot(ts, xs, ys, zs, vs, reussite_tab, color_tab, largeur_terrain, longueur_terrain, False)