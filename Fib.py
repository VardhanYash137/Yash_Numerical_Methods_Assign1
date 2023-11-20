#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
from functools import reduce

def fib_series(n):
    ans_list=np.ones((n))
    ans_list[0]=0
    for i in range(3,n):
        ele=ans_list[i-1]+ans_list[i-2]
        ans_list[i]=ele
    return ans_list

print(fib_series(10))


# In[6]:


# Define a lambda function to generate Fibonacci series
fibonacci = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 2), [0, 1]) if n > 1 else [0] * n
# Example: Print the first 10 Fibonacci numbers
print(fibonacci(10))


# In[ ]:




