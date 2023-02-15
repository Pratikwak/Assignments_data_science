#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q7) Calculate Mean, Median, Mode, Variance, Standard Deviation, Range &   
#comment about the values / draw inferences, for the given dataset


# In[5]:


import numpy as np
import pandas as pd


# In[7]:


df=pd.read_csv('Cars.csv')


# In[9]:


df


# In[18]:


df.describe()


# In[25]:


df1=pd.read_csv('Q7.csv')


# In[24]:


df1.describe()

