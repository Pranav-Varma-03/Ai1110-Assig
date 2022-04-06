#!/usr/bin/env python
# coding: utf-8

# In[20]:





# In[30]:


#Code- for verification of obtained x value from given median.

# Pericherla Pranav Varma
# CS21BTECH11044

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# x,y are points that satisfy line equation (y = x - 2) where, x = median & y = x.
x = [20,30,40,50,60]
y = [18,28,38,48,58]

# z is median of given data 
z = [48,48,48,48,48]

#labelling axes of the graph
plt.xlabel("Median --- X axis  -->")
plt.ylabel("x --- Y axis  -->");
plt.title("Graph Verification for Median")

#Highlighting and annotating the point of intersection to find x for given median.
plt.plot([48], [46], 'o') 
plt.annotate('A(48,46)', xy=(49, 45), textcoords='data')

#obtained A : for given median i.e.,48 we obtained value of x i.e., 46.
plt.plot(x,y)
plt.plot(z,y)
plt.show()


# In[7]:





# In[ ]:




