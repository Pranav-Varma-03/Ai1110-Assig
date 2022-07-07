#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
//Mean of RandomNumber
printf("mean = %lf\n",mean("gau.dat"));

//Variance of RandomNumbers
printf("variance = %lf\n",variance("gau.dat"));
return 0;
}
