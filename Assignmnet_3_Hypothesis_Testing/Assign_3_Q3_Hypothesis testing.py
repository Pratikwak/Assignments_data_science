#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy.stats import stats as st
from scipy.stats import chi2_contingency


# In[2]:


df = pd.read_csv('BuyerRatio.csv')


# In[3]:


df


# In[4]:


#null Hypothesis (Ho) =coloumns are independent(all proportions are equal)


#alternate Hypotheisi (Ha) = columns are dependent on each other(all proportions are not equal)


# In[11]:


df.drop(columns='Observed Values' ,inplace=True)
obs = np.array(df.values)
obs


# In[13]:


chi, p, degree_freedom,expected=chi2_contingency(obs)


# In[14]:


chi


# In[15]:


p


# In[16]:


degree_freedom


# In[17]:


expected


# In[19]:


alpha = 0.05


# In[26]:


if p < alpha:
    print('Reject the null hypothesis coloumns are dependentall proportions are  not equal')
else:
    print('Fail to reject null hypothesis = coloumns are independent that is all proportions are equal')


# In[ ]:





# In[ ]:





# In[ ]:




