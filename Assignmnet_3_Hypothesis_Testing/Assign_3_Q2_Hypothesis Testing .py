#!/usr/bin/env python
# coding: utf-8

# In[1]:


#A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT) of 
#reports of the laboratories on their preferred list. They collected a random sample and recorded TAT for 
#reports of 4 laboratories. TAT is defined as sample collected to report dispatch.
   
#Analyze the data and determine whether there is any difference in average TAT among the different 
#laboratories at 5% significance level.


# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from scipy.stats import stats as st


# In[3]:


df = pd.read_csv('LabTAT.csv')


# In[4]:


df


# In[5]:


#Hypotheis define

#Null Hypothesis(Ho) = there is no difference in the average Turn Around Time (TAT) (lab1=Lab2=Lab3=Lab4)

#Alternate Hypothesis(Ha) = there is  difference in the average Turn Around Time (TAT)


# In[6]:


df.describe()


# In[7]:


grand_mean = (178.361583+178.902917+199.913250+163.68275)/4
grand_mean


# In[8]:


st.f_oneway(df.iloc[:,0],df.iloc[:,1], df.iloc[:,2], df.iloc[:,3])


# In[ ]:


#p Value is very much less the alfa value (0.05)  therefore we reject null Hypothesis


# # Alternate Hypothesis(Ha) = there is  difference in the average Turn Around Time (TAT)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




