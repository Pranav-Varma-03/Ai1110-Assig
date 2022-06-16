import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()
plt.ylabel("$S_x$ $(w)$")
plt.xlabel("$w$")
A = np.array([1.732,1.732])
B = np.array([0,1000])
C = np.array([-1.732,-1.732])
a,b=np.polyfit(A,B,1)
plt.plot(C,B,marker='o')
plt.plot(A,B,marker='o')
print(a,b)
#plt.plot(A,a*A+b,marker = 'o')
#plt.annotate('A', xy=(1.732, 0), textcoords='data')
plt.legend()
#plt.grid()
plt.show()