def part1():
        t = 0
        rebond = False
        while not rebond and t < t_max:
            # Calcul des vecteurs vitesse
            vx = v0_norme * np.sin(theta) * np.cos(phi)
            vy = v0_norme * np.sin(theta) * np.sin(phi)
            vz = -g * t - v0_norme * np.cos(theta)                

            # Calcul des coordonnées
            x = v0_norme * np.sin(theta) * np.cos(phi) * t + x0
            y = v0_norme * np.sin(theta) * np.sin(phi) * t + y0
            z = -0.5 * g * (t**2) - v0_norme * np.cos(theta) * t + h0

            # [FAIL] La balle sort du terrain par les côtés
            if x >= largeur_terrain or x <= 0:
                return False

            # [FAIL] La balle touche le sol devant le filet
            if z <= 0 and y <= y_filet:
                return False

            # [FAIL] La balle tape dans le filet
            if abs(y - y_filet) <= 0.1 and z <= hauteur_filet:
                return False

            # [FAIL] La balle passe le mur1 avant le sol
            if y >= y_mur1:
                return False

            # La balle frappe le sol dans la bonne zone
            if z <= 0:
                x_rebond1, y_rebond1, z_rebond1 = x, y, z
                rebond = True

            x_tab.append(x)
            y_tab.append(y)
            z_tab.append(z)
            t_tab.append(t)

            t = t + dt
        return rebond
