#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[10]:


def clean_data(data):
    
    # drop null values
    data.dropna(inplace=True)
    
    return data


# In[1]:


def test_function():
    return 'This string is coming from a Jupyter Notebook'


# In[4]:

# In[ ]:




