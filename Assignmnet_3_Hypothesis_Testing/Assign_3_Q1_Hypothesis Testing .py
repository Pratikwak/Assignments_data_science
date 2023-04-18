#!/usr/bin/env python
# coding: utf-8

# In[1]:


# A F&B manager wants to determine whether there is any significant difference in the diameter of the 
 #  cutlet between two units. A randomly selected sample of cutlets was collected from both units 
  # and measured? Analyze the data and draw inferences at 5% significance level. Please state the assumptions 
   # and tests that you carried out to check validity of the assumptions.


# In[16]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats 
from scipy.stats import norm

get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


df = pd.read_csv('Cutlets.csv')


# In[15]:


df


# In[ ]:


#population Parameter in unknown

#We use two tailed t Test

#two sample test 


# In[18]:


#Null Hypothesis = D(Ca = Cb)(dimeter of unit A and unit B are Same)

#Alternate Hypothesis = D(Ca =! Cb)( Diameter of unit A and Unit b are not the same)


# In[ ]:





# In[17]:


df.describe()


# In[22]:


unitA = pd.Series(df.iloc[:,0])
unitA.head()


# In[25]:


unitB = pd.Series(df.iloc[:,1])
unitB.head()


# In[65]:


#p value, two sample, two taile t test

p_value = stats.ttest_ind(unitA,unitB)

p_value


# In[ ]:


#significance Level is 5% means alfa value is 0.05


# In[63]:


alfa = 0.05


# In[64]:


if alfa  < p_value:
    
    print('Alternate Hypothesis = D(Ca =! Cb)( Diameter of unit A and Unit b are not the same')
else:
    print('Null Hypothesis = D(Ca = Cb)(dimeter of unit A and unit B are Same')


# In[ ]:





# In[ ]:




