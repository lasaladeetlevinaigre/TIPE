#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>
#include <math.h>


/*
^ Uy
|
|   ^ v0
|  /
| /
O--------> Ux
Uz vers nous
*/

int nb = 1000; // nb de points
float dt = 0.001; //en s
float g = 9.81;

float v0[3];




// hauteur initiale
float h0 = 2.; //en m

float y_mur = 5.; //en m

float v0_norme = 2.; //m.s-1

// angle entre Ux et v0
float theta = 45.; //en DEG

// angle entre Uz et v0
float phi = 45.; // en DEG





float part1(float *x_tab, float *y_tab, float *z_tab, float* addr_x, float *addr_y, float t)
{
  float x;
  float y;
  float z;

  
  x = v0[0] * t;
  y = v0[1] * t;
  z = v0[2] * -1/2*g*t*t + h0;

  *addr_x = x;
  *addr_y = y;
  return z;
}

float part2(float *x_tab, float *y_tab, float *z_tab, float* addr_x, float *addr_y, float t)
{
  float x;
  float y;
  float z;

  x = v0[0] * t;
  y = v0[1] * t;
  z = v0[2] * 1/2*g*t*t;

  *addr_x = x;
  *addr_y = y;
  return z;
}

float part3(float *x_tab, float *y_tab, float *z_tab, float* addr_x, float *addr_y, float t)
{
  float x;
  float y;
  float z;

  
  x = v0[0] * t;
  y = v0[1] * t;
  z = v0[2] * -1/2*g*t*t;

  *addr_x = x;
  *addr_y = y;
  return z;
}


void plot(float *x_tab, float *y_tab, float *z_tab, float *addr_tp1, float *addr_tp2)
{
  float t = 0;
  int current_part = 1;
  for (int i  = 0 ; i < nb ; i++)
    {
      float x;
      float y;
      float z;

      if(current_part == 1)
	{
	  z = part1(x_tab, y_tab, z_tab, &x, &y, t);

	  if(z <= 0)
	    {
	      printf("Premier choc à %f sec en (%f, %f, %f)\n", t, x, y, z);
	      *addr_tp1 = t;
	      current_part = 2;
	    }
	}
      else if(current_part == 2)
	{
	  z = part2(x_tab, y_tab, z_tab, &x, &y, t);

	  if(y >= y_mur)
	    {
     	      printf("Deuxième choc à %f sec en (%f, %f, %f)\n", t, x, y, z);
	      *addr_tp2 = t;
	      current_part = 3;
	    }
	}
      else
	z = part2(x_tab, y_tab, z_tab, &x, &y, t);

      x_tab[i] = x;
      y_tab[i] = y;
      z_tab[i] = z;

      t = t + dt;
    }
  return;
}


void write_file(char *path, float *x_tab, float *y_tab, float *z_tab, float tp1, float tp2)
{

  FILE *f = fopen(path, "w");
  assert(f != NULL);

  int reussite = 1;
  fprintf(f, "%f, %f, %f, %d, %d\n", tp1, tp2, dt, nb, reussite);
  
  float t = 0;
  
  for (int i = 0 ; i < nb ; i++)
    {
      fprintf(f, "%f, %f, %f, %f\n", x_tab[i], y_tab[i], z_tab[i], t);
      t = t + dt;
    }

  fclose(f);
  return;
}

int main()
{
  float theta_rad = theta*M_PI/180;
  float phi_rad = phi*M_PI/180;

  v0[0] = v0_norme * cos(theta_rad);
  v0[1] = v0_norme * sin(theta_rad);
  v0[2] = v0_norme * cos(phi_rad);

  
  float *x_tab = calloc(nb, sizeof(float));
  float *y_tab = calloc(nb, sizeof(float));
  float *z_tab = calloc(nb, sizeof(float));

  float tp1 = 0.; float tp2 = 0.;
  plot(x_tab, y_tab, z_tab, &tp1, &tp2);
  
  write_file("data.csv", x_tab, y_tab, z_tab, tp1, tp2);
  
  return 0;
}
