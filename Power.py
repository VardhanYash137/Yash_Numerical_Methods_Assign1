#!/usr/bin/env python
# coding: utf-8

# In[3]:


L = [1, 2, 4, 8, 16, 32, 64]
X = 5

for i, value in enumerate(L):
    if 2 ** X == value:
        print('at index', i)
        break
else:
    print(X, 'not found')




# In[ ]:




