#include <stdio.h>
#include <complex.h>

#define steps 1000

int mandelbrot(double complex c, double bound, int maxIters) {
	double complex z;
	int i = 0;
	while (i < maxIters  && cabs(z) < bound) {
		z = z * z + c;
		i++;
	}
	
	if (i == maxIters) {
		return -1; // Represents NaN value
	}
	
	return i;
}

int mandelbrot_wrapper(double c1, double c2, double bound, int maxIters) {
	double complex c = c1 + c2 * I;
	double complex z;
	int i = 0;
	while (i < maxIters  && cabs(z) < bound) {
		z = z * z + c;
		i++;
	}
	
	if (i == maxIters) {
		return -1; // Represents NaN value
	}
	
	return i;
}

void mandelbrotArr(double min, double max, int numSteps, double bound, int maxIters, int *outArr){
	double stepSize = (max - min) / numSteps;
	for (int i = 0; i < numSteps; i++){
		for (int j = 0; j < numSteps; j++){
			double complex c = (min + i * stepSize) + (min + j * stepSize) * I;
			*(outArr + i * numSteps + j) = mandelbrot(c, 100, 100);
		}
	}
	
}


int main(){
	double min = -2, max = 2;
	//const int steps = 100000;
	
	static int n[steps][steps];
	
	double stepSize = (max - min) / steps;
	for (int i = 0; i < steps; i++){
		for (int j = 0; j < steps; j++){
			double complex c = (min + i * stepSize) + (min + j * stepSize) * I;
			n[i][j] = mandelbrot(c, 100, 100);
		}
	}

	printf("%d", n[0][0]);
	
	return 0;
}