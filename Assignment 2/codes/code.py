#!/usr/bin/env python
# coding: utf-8

# In[70]:


import numpy as np
from math import sqrt
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()

#As vec_a and vec_b are perpendicular. therefore for verification assume:

vec_a = np.array([0,0,5,0]) # mod(vec_a) = 5 {given}
vec_b = np.array([0,0,0,12]) #mod(vec_b) = 12 {obtained value}

#let resultant vec of a & b be c
vec_c = vec_a + vec_b #mod(vec_c) = 13 {given}

#plotting all 3 vectors and marking them.
plt.quiver(0,0,5,0,scale_units = 'xy',angles='xy',scale=1)
plt.quiver(0,0,0,12,scale_units = 'xy',angles='xy',scale=1)
plt.quiver(0,0,5,12,scale_units = 'xy',angles='xy',scale=1)
plt.xlim(-2,8)
plt.ylim(-2,14)

plt.annotate(('vec_a  = 5i'),(2,-1))
plt.annotate(('vec_b  = 12j'),(0.2,10))
plt.annotate(('vec_c  = 5i + 12j'),(2.8,6))

plt.show()

#finding mod of resultant vector c
mod_vec_c = sqrt(vec_c[2]**2 + vec_c[3]**2)

if(mod_vec_c == 13): print("Verified and Correct")


# In[ ]:





# In[ ]:





# In[ ]:




