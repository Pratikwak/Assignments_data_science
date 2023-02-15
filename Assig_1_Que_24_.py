#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#  Q 24)   A Government  company claims that an average light bulb lasts 270 days.
#A researcher randomly selects 18 bulbs for testing. The sampled bulbs last an average of 260 days, 
#with a standard deviation of 90 days. If the CEO's claim were true, 
#what is the probability that 18 randomly selected bulbs would have an average life of no more than 260 days


# In[1]:


from scipy import stats
from scipy.stats import norm


# In[2]:


# Assume Null Hypothesis is: Ho = Avg life of Bulb >= 260 days
# Alternate Hypothesis is: Ha = Avg life of Bulb < 260 days


# In[4]:


# find t-scores at x=260; t=(s_mean-P_mean)/(s_SD/sqrt(n))
t=(260-270)/(90/18**0.5)
t


# In[5]:


# Find P(X>=260) for null hypothesis
# p_value=1-stats.t.cdf(abs(t_scores),df=n-1)
p_value=1-stats.t.cdf(abs(-0.4714),df=17)
p_value


# In[ ]:




