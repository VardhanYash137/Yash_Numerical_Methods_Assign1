#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fib_module import fib_series
import timeit

print(fib_series(100))
print()
# Measure the time it takes to produce 100 Fibonacci numbers
time_taken = timeit.timeit(lambda: fib_series(100), number=1)
print(f"Time taken to produce 100 Fibonacci numbers: {time_taken} seconds")


# In[ ]:




