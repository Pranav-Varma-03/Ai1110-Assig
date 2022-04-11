#!/usr/bin/env python
# coding: utf-8

# In[43]:


#Code- for calculation of mode of given data.

# Pericherla Pranav Varma
# CS21BTECH11044

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# x is the data given.
x = [13,35,43,46,46,50,55,61,71,80]
#y is a bin (class interval of length 10)
y = [10,20,30,40,50,60,70,80]
plt.hist(x,y)
#labelling axes of the graph
plt.xlabel("class intervals (X axis)")
plt.ylabel("frequency (Y axis)");
plt.title("Mode Determination")

a = [40,50]
b = [3,2]
c = [1,3]
d = [2.33,0]
e = [46.66,46.66]

plt.plot(a,b)
plt.plot(a,c)
plt.plot(46.66,2.33,marker='o',markersize=5,markerfacecolor='Black',markeredgecolor='Black')
plt.annotate("A--(POI)",xy=(47.7,2.3))
plt.plot(e,d)
plt.plot(46.66,0,marker='o',markersize=5,markerfacecolor='Black',markeredgecolor='Black')
plt.annotate("B(MODE)",xy=(47.7,0.09))
#Point of Intersection [POI] = mode = 46.66
mode_approx = 46.66
plt.show()

if(mode_approx//1 == 46):print("Correct value of mode ") #mode = 46


# In[ ]:





# In[ ]:




