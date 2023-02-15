#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q11)  Suppose we want to estimate the average weight of an adult male in    Mexico.
#We draw a random sample of 2,000 men from a population of 3,000,000 men and weigh them. 
#We find that the average person in our sample weighs 200 pounds, and the standard deviation of the sample is 30 pounds. 
#Calculate 94%,98%,96% confidence interval?


# In[9]:


import numpy as np
import pandas as pd 
from scipy import stats
from scipy.stats import norm
import math


# In[13]:


#data is given
#sample size=2000
#population size = 3,000,000
#average weight=200
#standard deviation = 30
a=math.sqrt(2000)
s=30/a
s


# In[17]:


#average weight od adult in mexico with 94% Confidence interval
stats.norm.interval(0.94,200,0.6708203932499369)


# In[19]:


##average weight od adult in mexico with 98% Confidence interval
stats.norm.interval(0.98,200,0.6708203932499369)


# In[20]:


#average weight od adult in mexico with 96% Confidence interval
stats.norm.interval(0.96,200,0.6708203932499369)

