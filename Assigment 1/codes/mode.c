// This code- Verification of mode of given data. {verification of x is done in python code by graphs}
// Pericherla Pranav Varma
// CS21BTECH11044

#include <stdio.h>
#include <stdlib.h>
#define N 100

int main(){
    int j,x,n,i,l=0,k=0,m=0; //n = length of array
    int array[N]= {13, 35, 43, 46, x, x + 4, 55, 61, 71, 80};
    int median = 48;
//n = strlen(array);  n=10 (number of elements in array)
n = 10;
if((n%2) != 0){ //n = 10
    i = (n-1)/2; //array[i] is the middle element i.e Median
    }
else     {
    i = n/2;
    // avg of array[i-1] & array [i] is the Median.
    /* array[4] = x and array[5] = x+4.
    [x + (x+4)]/2 = 48(median)
    x + 2 = 48(median)
    */
x = median - 2 ; // y axis : x and x axis : median 
    }
    if(x == 46) printf("True and x : verified\n"); //verification of obtained value x.
    else printf("False\n");

//verification of mode:
int val[N];
int *arr;
arr = (int*)calloc(N,sizeof(int));

for(i=0;i<10;i++){ //Arr stores the number of occurences of particular number >> using l.
    for(j=i;j<10;j++){
        if(array[i] == array[j]){
            arr[l] = arr[l] + 1;
            val[l] = array[i];
        }
        else break;  
    }
i = i + ( arr[l] - 1 );
l = l + 1;
}
// Number corresponding to highest Arr[i] value is the MODE of given data.
for(i=0;i<l;i++){ //figures out mode of data.
    for(j=0;j<l;j++){
        if((arr[i])>=(arr[j])){
            k = 1;
            m = i;
        }
        else {m = 0,k = 0;
            break;
        }
    }
}

if(k == 1){
    // arr[m] is the mode of the data.
    if(arr[m] == 46){ //in given quen mode = 46.
        printf("True and mode verified");
    }
}
return 0;
}