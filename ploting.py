from engine import ComputeTrajectory, bcolors
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import random
import numpy as np

def generate_random_hex_color(opacity):
	# Generate three random integers between 0 and 255
	r = int(random.uniform(128, 255))
	g = int(random.uniform(128, 255))
	b = int(random.uniform(128, 255))

	# Convert the integers to hexadecimal and format them
	hex_color = "#{:02x}{:02x}{:02x}{:02x}".format(r, g, b, int(opacity*255))
	return hex_color


def compute_multiple_trajectories(params_tab):
	ts = []
	xs = []
	ys = []
	zs = []
	reussite_tab = []
	color_tab = []

	i = 0

	for params in params_tab:
		#print(i,"-"*50)

		trajectory = ComputeTrajectory(params)
		reussite = trajectory.compute_trajectory()
		t, x, y, z = trajectory.get_trajectory()
		ts.append(t)
		xs.append(x)
		ys.append(y)
		zs.append(z)

		if reussite:
			clr = generate_random_hex_color(1)
			state = True
			#print(f"{bcolors.OKBLUE}[OK] Affichage{bcolors.ENDC}")
			pass
		else:
			clr = generate_random_hex_color(0.1)
			state = False
			pass
		reussite_tab.append(state)
		color_tab.append(clr)

		i = i + 1

	return ts, xs, ys, zs, reussite_tab, color_tab





def plot(v0, ts, xs, ys, zs, reussite_tab, largeur_terrain, longueur_terrain, display_only_sucess = True):
	fig = plt.figure(figsize=(14, 4))
	# Graphe des coordonnées x
	plt.subplot(131)
	for i in range(len(ts)):
		if (display_only_sucess and reussite_tab[i]) or display_only_sucess == False:
			t = ts[i]
			x = xs[i]
			plt.plot(t, x, label=None)
	plt.xlabel("Temps (s)")
	plt.ylabel("Coordonnée x")
	plt.ylim(0, max(longueur_terrain, largeur_terrain))
	plt.legend()

	# Graphe des coordonnées y
	plt.subplot(132)
	for i in range(len(ts)):
		if (display_only_sucess and reussite_tab[i]) or display_only_sucess == False:
			t = ts[i]
			y = ys[i]
			plt.plot(t, y)
	plt.xlabel("Temps (s)")
	plt.ylabel("Coordonnée y")
	plt.ylim(0, max(longueur_terrain, largeur_terrain))
	plt.legend()

	# Graphe des coordonnées z
	plt.subplot(133)
	for i in range(len(ts)):
		if (display_only_sucess and reussite_tab[i]) or display_only_sucess == False:
			t = ts[i]
			z = zs[i]
			plt.plot(t, z)
	plt.xlabel("Temps (s)")
	plt.ylabel("Coordonnée z")

	fig.suptitle(f"Trajectoires pour {v0}ms")









	# Ajuster l'espacement entre les sous-graphiques
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')


	# Traçage du rectangle (mur)
	wall_width = 0.1  # x
	wall_len = max(longueur_terrain, largeur_terrain)  # y

	wall_height = 2  # x

		
	x = [
		[0, 0, 0, 0],
		[10, 10, 10, 10],
		[0, 10, 10, 0],
		[0, 10, 10, 0],
	]
	y = [
		[0, 20, 20, 0],
		[0, 20, 20, 0],
		[10, 10, 10, 10],
		[20, 20, 20, 20],
	]
	z = [
		[0, 0, 2, 2], #mur gauche
		[0, 0, 2, 2], #mur droit
		[0, 0, 0.9, 0.9], #filet
		[0, 0, 3, 3],#mur en face
	]
	opacity = [0.15, 0.2, 0.3, 0.3]
	colors = ["grey", "#942929", "grey", "#403d39"]
	surfaces = []

	for i in range(len(x)):
		surfaces.append( [list(zip(x[i],y[i],z[i]))] )

	for i in range(len(surfaces)):
		ax.add_collection3d(Poly3DCollection(surfaces[i], alpha=opacity[i], facecolor=colors[i]))


	for i in range(len(ts)):
		if (display_only_sucess and reussite_tab[i]) or display_only_sucess == False:
			x = xs[i]
			y = ys[i]
			z = zs[i]
			#ax.scatter(x, y, z, marker='x')
			ax.plot(x, y, z)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')

	ax.set_xlim(0, max(longueur_terrain, largeur_terrain))
	ax.set_ylim(0, max(longueur_terrain, largeur_terrain))
	ax.set_zlim(0, 4)

	plt.title(f"Trajectoire de la balle pour {v0}ms")

	plt.show()
