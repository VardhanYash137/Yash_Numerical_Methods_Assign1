#!/usr/bin/env python
# coding: utf-8

# In[6]:


import time

# Recursive function to compute factorial in Python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Main program
if __name__ == "__main__":
    # Input from user
    n = int(input("Enter a non-negative integer: "))

    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Calculate and display factorial and measure time
        start_time = time.time()
        result = factorial(n)
        end_time = time.time()

        print(f"Factorial of {n} = {result}")
        print(f"Time taken: {end_time - start_time} seconds")


# In[ ]:




