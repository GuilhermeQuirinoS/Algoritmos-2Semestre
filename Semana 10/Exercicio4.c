#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	FILE *fr = fopen("prodMistoR.txt", "r");

	float x[3] = {}, y[3] = {}, z[3] = {}, valor = 0, num1;
	int d1 = 0, d2 = 0, d3 = 0;

	for (int i = 0; i < 9; i++)
	{
		fscanf(fr, "%f", &num1);

		if (i >= 0 && i < 3)
		{
			x[d1] = num1;
			d1++;
		}
		else if (i >= 3 && i < 6)
		{
			y[d2] = num1;
			d2++;
		}
		else if (i >= 6 && i < 9)
		{
			z[d3] = num1;
			d3++;
		}
	}

	fclose(fr);

	valor = x[0] * ((y[1] * z[2]) - (z[1] * y[2])) + y[0] * ((z[1] * x[2]) - (z[2] * x[1])) + z[0] * ((x[1] * y[2]) - (y[1] * x[2]));

	printf("x = (%.4f, %.4f, %.4f)\n", x[0], y[0], z[0]);
	printf("y = (%.4f, %.4f, %.4f)\n", x[1], y[1], z[1]);
	printf("z = (%.4f, %.4f, %.4f)\n", x[2], y[2], z[2]);
	printf("Volume: %.4f\n", valor);
}