#!/usr/bin/env python
# coding: utf-8

# In[3]:


L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0

while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    i += 1
else:
    print(X, 'not found')



# In[ ]:




