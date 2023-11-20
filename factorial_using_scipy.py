#!/usr/bin/env python
# coding: utf-8

# In[5]:


# File: factorial_python_scipy.py

import time
from scipy.special import factorial as scipy_factorial

# Main program
if __name__ == "__main__":
    # Input from user
    n = int(input("Enter a non-negative integer: "))

    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Calculate and display factorial using SciPy and measure time
        start_time = time.time()
        result = scipy_factorial(n)
        end_time = time.time()

        print(f"Factorial of {n} = {result}")
        print(f"Time taken: {end_time - start_time} seconds")


# In[ ]:




