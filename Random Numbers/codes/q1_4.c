#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
//Mean of RandomNumber
printf("mean = %lf\n",mean("uni.dat"));

//Variance of RandomNumbers
printf("variance = %lf\n",variance("uni.dat"));
return 0;
}
