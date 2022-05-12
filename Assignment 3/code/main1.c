/* 
NAME : PERICHERLA PRANAV VARMA
ROLL NO : CS21BTECH11044
*/

/* CH16 question 14(i) CBSE 11  */

#include<stdio.h>

int main(){
    float P_A = 0.5 ;
    float P_B = 0.7 ;
    float P_AB = 0.6;

    if((P_AB < P_A)&&(P_AB < P_B)) printf("Given Probabilities are consistent\n");
    else printf("Given Probabilities are not consistent\n") ;

    return 0;
}