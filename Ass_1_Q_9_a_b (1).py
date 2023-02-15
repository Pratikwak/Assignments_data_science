#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q9)a) Calculate Skewness, Kurtosis & draw inferences on the following data
     # Cars speed and distance 
#Use Q9_a.csv
#b) SP and Weight(WT)
#Use Q9_b.csv






# In[14]:


import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt


# In[8]:


df1=pd.read_csv('Q9_a.csv')
df1


# In[26]:


x=df1.speed


# In[28]:


y=df1.dist


# In[31]:


plt.scatter(x,y)


# In[39]:


df1.plot.line(x='speed',y='dist')


# In[42]:


#speed 
#Speed data is left skewed 
plt.hist(x)


# In[ ]:


#dist
#dhe distance data is right skewed 


# In[43]:


plt.hist(y)


# In[45]:


df2=pd.read_csv('Q9_b.csv')


# In[47]:


df2


# In[69]:


p=df2.SP

print(p)


# In[73]:


q=df2.WT
print(q)


# In[81]:


plt.subplot(2,2,1)
plt.hist(p)


plt.subplot(2,2,2)
plt.hist(q)


plt.tight_layout()

