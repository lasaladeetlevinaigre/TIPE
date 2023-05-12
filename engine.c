#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <stdbool.h>
#include <math.h>

/*
^ Uy
|
|
|
|
O--------> Ux
Uz vers nous
*/

float y_mur = 15.; //en m

int nb = 1000; // nb de points
float dt = 0.001; //en s
float g = 9.81;

float part1(float *x_tab, float *y_tab, float *z_tab, float* addr_x, float *addr_y, float t)
{
  float v0[] = {10., 5., 3.};
  float x;
  float y;
  float z;

  
  x = v0[0] * t;
  y = v0[1] * t;
  z = v0[2] * t*t;

  *addr_x = x;
  *addr_y = y;
  return z;
}

float part2(float *x_tab, float *y_tab, float *z_tab, float* addr_x, float *addr_y, float t)
{
  float v0[] = {10., 5., 3.};
  float x;
  float y;
  float z;

  
  x = v0[0] * t;
  y = v0[1] * t;
  z = v0[2] * t*t;

  *addr_x = x;
  *addr_y = y;
  return z;
}

float part3(float *x_tab, float *y_tab, float *z_tab, float* addr_x, float *addr_y, float t)
{
  float v0[] = {10., 5., 3.};
  float x;
  float y;
  float z;

  
  x = v0[0] * t;
  y = v0[1] * t;
  z = v0[2] * t*t;

  *addr_x = x;
  *addr_y = y;
  return z;
}


void plot(float *x_tab, float *y_tab, float *z_tab)
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
	    current_part = 2;
	}
      else if(current_part == 2)
	{
	  z = part2(x_tab, y_tab, z_tab, &x, &y, t);

	  if(y >= y_mur)
	    current_part = 3;
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
  fprintf(f, "%f, %f, %f, %d, %d", tp1, tp2, dt, nb, reussite)
  
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
  float *x_tab = calloc(nb, sizeof(float));
  float *y_tab = calloc(nb, sizeof(float));
  float *z_tab = calloc(nb, sizeof(float));

  plot(x_tab, y_tab, z_tab);
  
  write_file("data.csv", x_tab, y_tab, z_tab);
  
  return 0;
}
