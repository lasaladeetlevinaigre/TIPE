from engine import ComputeTrajectory, bcolors
import matplotlib.pyplot as plt
import random


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





def plot(ts, xs, ys, zs, reussite_tab, color_tab, largeur_terrain, longueur_terrain, display_only_sucess = True):
	fig = plt.figure(figsize=(14, 4))
	# Graphe des coordonnées x
	plt.subplot(131)
	for i in range(len(ts)):
		if (display_only_sucess and reussite_tab[i]) or display_only_sucess == False:
			t = ts[i]
			x = xs[i]
			plt.plot(t, x, label=i)
	plt.xlabel("Temps (s)")
	plt.ylabel("Coordonnée x")
	plt.ylim(0, max(longueur_terrain, largeur_terrain))
	plt.title("Trajectoire en x")
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
	plt.title("Trajectoire en y")
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
	plt.title("Trajectoire en z")

	# Ajuster l'espacement entre les sous-graphiques
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	for i in range(len(ts)):
		if (display_only_sucess and reussite_tab[i]) or display_only_sucess == False:
			x = xs[i]
			y = ys[i]
			z = zs[i]
			ax.plot(x, y, z)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')

	ax.set_xlim(0, max(longueur_terrain, largeur_terrain))
	ax.set_ylim(0, max(longueur_terrain, largeur_terrain))
	ax.set_zlim(0)

	plt.title("Trajectoire de la balle")

	plt.show()
