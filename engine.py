import numpy as np

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

class ComputeTrajectory:
    def __init__(self, params):
        self.params = params
        self.t_tab = []
        self.x_tab = []
        self.y_tab = []
        self.z_tab = []
        self.vx = 0
        self.vy = 0
        self.vz = 0

        self.print_tab = params['print_tab']
        self.print_step = params['print_step']
        self.g = 9.81
        self.x0 = params['x0']
        self.y0 = params['y0']
        self.h0 = params['h0']
        self.t_max = params['t_max']
        self.v0_norme = params['v0_norme']
        self.phi = params['phi']
        self.theta = params['theta']
        self.largeur_terrain = params['largeur_terrain']
        self.longueur_terrain = params['longueur_terrain']
        self.hauteur_mur1 = params['hauteur_mur1']
        self.hauteur_mur2 = params['hauteur_mur2']
        self.y_filet = params['longueur_terrain']/2
        self.hauteur_filet = params['hauteur_filet']
        self.e1 = params['e1']
        self.e2 = params['e2']

        self.t_rebond1 = -1
        self.x_rebond1 = -1
        self.y_rebond1 = -1
        self.z_rebond1 = -1

        self.t_rebond2 = -1
        self.x_rebond2 = -1
        self.y_rebond2 = -1
        self.z_rebond2 = -1

        self.t_rebond3 = -1
        self.x_rebond3 = -1
        self.y_rebond3 = -1
        self.z_rebond3 = -1

        self.zmax = -1

        self.y_mur1 = self.longueur_terrain
        self.z_mur1 = self.hauteur_mur1
        self.x_mur2 = self.largeur_terrain
        self.z_mur2 = self.hauteur_mur2

        self.dt = 0.0001

    def print_tab_func(self):
        for i in range(len(self.t_tab)):
            print("[t:%0.6f" % self.t_tab[i], ", x:%0.6f" % self.x_tab[i], ", y:%0.6f" % self.y_tab[i], ", z:%0.6f" % self.z_tab[i], "]")





    def part1(self):
        t = 0
        while True:
            self.vx = self.v0_norme * np.sin(self.theta * np.pi / 180) * np.cos(self.phi * np.pi / 180)
            self.vy = self.v0_norme * np.sin(self.theta * np.pi / 180) * np.sin(self.phi * np.pi / 180)
            self.vz = -self.g * t - self.v0_norme * np.cos(self.theta * np.pi / 180)                

            x = self.v0_norme * np.sin(self.theta * np.pi / 180) * np.cos(self.phi * np.pi / 180) * t + self.x0
            y = self.v0_norme * np.sin(self.theta * np.pi / 180) * np.sin(self.phi * np.pi / 180) * t + self.y0
            z = -0.5 * self.g * (t**2) - self.v0_norme * np.cos(self.theta * np.pi / 180) * t + self.h0

            #if (x-self.x0)**2 + (y-self.y0-1.8)**2 + (z-self.h0)**2 > 3**2:
            #    return False

            if z >= self.zmax:
                self.zmax = z


            if t > self.t_max:
                if self.print_step:
                    print(f"{bcolors.FAIL}[NO TEMPS] Temps écoulé{bcolors.ENDC}")
                return False

            if x >= self.largeur_terrain or x <= 0:
                if self.print_step:
                    print(f"{bcolors.FAIL}[NO DEHORS] La balle sort du terrain par les côtés{bcolors.ENDC}")
                return False


            if z <= 0 and y <= self.y_filet:
                if self.print_step:
                    print(f"{bcolors.FAIL}[NO FILET] La balle touche le sol devant le filet{bcolors.ENDC}")
                return False

            precision_filet = 0.1
            if abs(y - self.y_filet) <= precision_filet and z <= self.hauteur_filet:
                #print("NIVEAU FILET (y:%0.4f" % y, " z:%0.4f" % z, ")")
                if self.print_step:
                    print(f"{bcolors.FAIL}[NO FILET] La balle tape dans le filet{bcolors.ENDC}")
                return False

            if y >= self.y_mur1:
                if self.print_step:
                    print(f"{bcolors.FAIL}[NO DEHORS] La balle passe le mur1 avant le sol{bcolors.ENDC}")
                return False


            if z <= 0:
                if self.print_step:
                    print("[RB] Premier rebond contre sol à %0.4f" % t, "sec (y:%0.4f" % y, "m)")
                self.t_rebond1 = t
                self.x_rebond1 = x
                self.y_rebond1 = y
                self.z_rebond1 = z

                self.x_tab.append(x)
                self.y_tab.append(y)
                self.z_tab.append(z)
                self.t_tab.append(t)
                return True

            self.x_tab.append(x)
            self.y_tab.append(y)
            self.z_tab.append(z)
            self.t_tab.append(t)

            t = t + self.dt



    def part2(self):
        t = 0
        while True:
            x = self.e1 * self.vx * t + self.x_rebond1
            y = self.e1 * self.vy * t + self.y_rebond1
            z = -0.5 * self.g * (t**2) - self.e1 * self.vz * t


            if z >= self.z_mur1:
                if self.print_step:
                    print(f"{bcolors.FAIL}[NO DEHORS] La balle passe au-dessus du mur1{bcolors.ENDC}")
                return False

            if t > self.t_max:
                if self.print_step:
                    print(f"{bcolors.FAIL}[NO TEMPS] Temps écoulé{bcolors.ENDC}")
                return False

            if z < 0:
                if self.print_step:
                    print(f"{bcolors.FAIL}[NO DEHORS] La balle tombe avant de toucher le mur1{bcolors.ENDC}")
                return False

            if x >= self.x_mur2 or x <= 0:
                if self.print_step:
                    print(f"{bcolors.FAIL}[NO DEHORS] La balle frappe le mur2{bcolors.ENDC}")
                return False

            if y >= self.y_mur1:
                if self.print_step:
                    print("[RB] Deuxième rebond contre mur1 à %0.4f" % t, "sec (z:%0.4f" % z, "m)")
                self.t_rebond2 = t + self.t_rebond1
                self.x_rebond2 = x
                self.y_rebond2 = y
                self.z_rebond2 = z
                return True

            self.x_tab.append(x)
            self.y_tab.append(y)
            self.z_tab.append(z)
            self.t_tab.append(t + self.t_rebond1)

            t = t + self.dt


    def part3(self):
        t = 0
        f = False
        while not f and t < self.t_max:
            x = self.e2 * self.vx * t + self.x_rebond2
            y = -self.e2 * self.vy * t + self.y_rebond2
            z = -0.5 * self.g * (t**2) - self.e2 * self.vz * t + self.z_rebond2

            if t > self.t_max:
                if self.print_step:
                    print(f"{bcolors.FAIL}[NO TEMPS] Temps écoulé{bcolors.ENDC}")
                return f

            if z < 0:
                if self.print_step:
                    print(f"{bcolors.FAIL}[NO DEHORS] La balle tombe avant de passer le mur2{bcolors.ENDC}")
                return f

            if y < 0:
                if self.print_step:
                    print(f"{bcolors.FAIL}[NO DEHORS] La balle passe derrière le mur derrière nous{bcolors.ENDC}")
                return f

            if (x > self.x_mur2 or x < 0) and z < self.z_mur2:
                if self.print_step:
                    print(f"{bcolors.FAIL}[NO DEHORS] La balle frappe le mur2{bcolors.ENDC}")
                return f                

            if (x > self.x_mur2 or x < 0) and z > self.z_mur2:
                if self.print_step:
                    print("[RB] Passe au-dessus mur2 à %0.4f" % t, "sec")
                    print(f"{bcolors.OKGREEN}[OK] Réussite !{bcolors.ENDC}")
                f = True
                return f

            self.x_tab.append(x)
            self.y_tab.append(y)
            self.z_tab.append(z)
            self.t_tab.append(t + self.t_rebond2)
            t += self.dt




    def compute_trajectory(self):
        if self.y0 >= self.longueur_terrain // 2 and self.print_step:
            print(f"{bcolors.WARNING}[WARNING] x:{self.params['x0']} y:{self.params['y0']} est sur terrain adverse{bcolors.ENDC}")
            return False

        if self.part1() and self.part2() and self.part3():
            #print(f"{bcolors.OKGREEN}[OK] x:{self.params['x0']} y:{self.params['y0']} theta:{self.params['theta']:05.3f} phi:{self.params['phi']:05.3f}{bcolors.ENDC}")
            return True
        else:
            return False

    def get_trajectory(self):
        if self.print_tab == True:
            self.print_tab_func()
        return self.t_tab, self.x_tab, self.y_tab, self.z_tab







"""
params = {
    't_max': 8,
    'print_tab': False,
    'print_step': False,
    'largeur_terrain': largeur_terrain,
    'longueur_terrain': longueur_terrain,
    'e1': 1.6,
    'e2': 1.6,
    'hauteur_mur1': 3,
    'hauteur_mur2': 2,

    'theta': 90,
    'phi': 80,
    
    'x0': 2,
    'y0': 2,
    'h0': 2.3,

    'v0_norme': [20, 20, 20],
}

trajectory = ComputeTrajectory(params)
trajectory.compute_trajectory()
t, x, y, z, v = trajectory.get_trajectory()
"""
