from cmath import e, pi, sqrt
from math import comb
#1: Fundamental Theorem:
#Pr(K)=(nCk)(p)^k (q)^(n-k).
n=10
k=5
p=0.5
q=0.5

#a is the value of Pr(k).
a = comb(n,k)*((p)**k)*((q)**(n-k))
print("Value of Pr(5) = ",a)

#2: DeMoivre Theorem:
npq = 2.5
np = 5

b = (1/(2*(pi)*npq)**0.5)*((e)**((-(k-np)**2)/2*npq))

print("The value of Approximate Pr(k) :",b)
