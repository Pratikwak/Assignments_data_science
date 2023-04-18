#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 3_Q4.
#TeleCall uses 4 centers around the globe to process customer order forms.
#They audit a certain %  of the customer order forms. Any error in order form renders 
#it defective and has to be reworked before processing.  The manager wants to check
#whether the defective %  varies by centre. Please analyze the data at 5% significance level and help the
#manager draw appropriate inferences


# In[8]:


import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import stats 
from scipy.stats import norm
from scipy.stats import chi2_contingency


# In[ ]:


#Define Hypothesis

#Null Hypothesis :  defective %  varies by centre


#Alternate Hypothesis:  defective %  not varies by centre


# In[4]:


df = pd.read_csv('Costomer+OrderForm.csv')


# In[5]:


df


# In[10]:


df['Phillippines'].value_counts()


# In[11]:


df['Indonesia'].value_counts()


# In[12]:


df['Malta'].value_counts()


# In[14]:


df['India'].value_counts()


# In[16]:


obs = np.array([[271,267,269,280],[29,33,31,20]])


# In[17]:


obs


# In[18]:


chi,p,degree_freedom,Expected = chi2_contingency(obs)


# In[19]:


chi


# In[20]:


p


# In[21]:


degree_freedom


# In[22]:


Expected


# In[24]:


alfa = 0.05


# In[26]:


if p< alfa:
    print('we  reject null hypothesis that is defective %  not varies by centre ')
else:
    print('Failed to reject null hypothesis that is defective %  varies by centre')


# In[ ]:





# In[ ]:





# In[ ]:




