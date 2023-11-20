#!/usr/bin/env python
# coding: utf-8

# In[3]:


X = 5
L = [2 ** i for i in range(X + 1)]

if 2 ** X in L:
    print('at index', L.index(2 ** X))
else:
    print(X, 'not found')






# In[ ]:




