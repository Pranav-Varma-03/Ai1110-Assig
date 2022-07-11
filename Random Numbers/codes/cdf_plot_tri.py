#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt
import math


x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
#--------------------------------------------------------------------------
#--------------------------------------PRACTICAL-------------------------
#--------------------------------------------------------------------------
randvar = np.loadtxt('tri.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

#--------------------------------------------------------------------------
#--------------------------------------THEORETICAL-------------------------
#--------------------------------------------------------------------------

#Defining Q function
#def Q(x):
#	return 0.5 - (math.erf(x/np.sqrt(2)))*0.5

#Defining CDF from Q function
#def gauss_cdf(x):
#	return 1 - Q(x)
	
#vec_gauss_cdf = scipy.vectorize(gauss_cdf,otypes=[float])
#---------------------------------------------------------------------------
plt.plot(x.T,err)#plotting the CDF
#plt.plot(x,vec_gauss_cdf(x)) #plotting the CDF (Continuous Graph Theoretical)
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])
plt.show() #opening the plot window
