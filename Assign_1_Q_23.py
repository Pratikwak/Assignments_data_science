#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm


# In[3]:


#t vale for 95 % CI Where n = 25
# degree of freedom n-1 =25-1=24
stats.t.ppf(0.975,24)


# In[4]:


#96%
stats.t.ppf(0.98,24)


# In[5]:


#99%
stats.t.ppf(0.995,24)


# In[ ]:





# In[ ]:





# In[ ]:




