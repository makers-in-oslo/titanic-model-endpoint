#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


def clean_data(data):
    
    # drop null values
    data.dropna(inplace=True)
    
    return data


# In[3]:


def test_function():
    return 'You died.'


# In[4]:


#get_ipython().system('jupyter nbconvert data_prep.ipynb --to script')


# In[ ]:




