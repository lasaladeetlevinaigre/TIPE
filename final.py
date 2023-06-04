import numpy as np
import matplotlib.pyplot as plt

# Dimensions du terrain
largeur_terrain = 10
longueur_terrain = 20

# Créer un tableau 2D de dimensions largeur_terrain x longueur_terrain rempli de zéros
terrain = np.zeros((largeur_terrain, longueur_terrain))

# Définir la fonction get_probability(x, y) qui retourne la probabilité de succès en fonction de x et y
def get_probability(x, y):
    # Vérifier si la position en longueur est dans le carré adverse
    if y >= longueur_terrain // 2:
        return 0.0  # Retourner 0 si dans le carré adverse
    
    # Calculer la probabilité en fonction de x et y
    return x / largeur_terrain + y / longueur_terrain

# Parcourir chaque position du terrain et remplir le tableau en utilisant get_probability(x, y)
for x in range(largeur_terrain):
    for y in range(longueur_terrain):
        terrain[x][y] = get_probability(x, y)

# Afficher le terrain sous forme de heatmap
plt.imshow(terrain, cmap='hot', origin='lower')
plt.colorbar()
plt.xlabel('Longueur')
plt.ylabel('Largeur')
plt.title('Heatmap des probabilités')
plt.show()
