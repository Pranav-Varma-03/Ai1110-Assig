k = 1/6
x = k #Pr(X=0)
y = 2*k #Pr(X=1)
z = 3*k #Pr(X=2)

#Need to verify that sum of probabilities == 1 (i.e., x+y+z = 1)

if(x+y+z ==1 ):
    print("verified and correct\n")
else : 
    print("False\n")



#Pr(X<2): Pr(X=0) i.e "x" + Pr(X=1) i.e "y"
a = x  +  y
if(a == 1/2):
    print("Correct\n")

else :
    print("False\n")

#Pr(X<=2): Pr(X=0) i.e., "x" + Pr(X=1) i.e., "y" + Pr(X=2) i.e.,"z"
b = x + y + z

if (b == 1):
    print("Correct\n")
else:
    print("False\n")

#Pr(X>=2): Pr(X=2) i.e., "z" + Pr(X>2) i.e., 0 
c = z + 0

if (c == 1/2):
    print("Correct\n")
else:
    print("False\n")