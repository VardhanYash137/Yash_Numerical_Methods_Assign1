#!/usr/bin/env python
# coding: utf-8

# In[1]:


#the function to add two strings, two lists, and two floating points. 

def adder(a, b):
    return a + b

# Call the function at the bottom of the file
result_string = adder("Hello ", "World")
result_list = adder([1, 2, 3], [4, 5, 6])
result_floats = adder(2.5, 3.5)

# Print the results
print("String concatenation:", result_string)
print("List concatenation:", result_list)
print("Floats addition:", result_floats)


# In[2]:


# Generalize the adder function for an arbitrary number of arguments
# add_numbers.py

def adder(*args):
    return sum(args)

# Call the function at the bottom of the file
result_arbitrary = adder(1, 2, 3, 4, 5)

# Print the result
print("Sum of arbitrary numbers:", result_arbitrary)


# In[3]:


# change the function so that it takes in three keyword arguments called good, bad, and ugly, with default values 1, 2, and 3 respectively. 
# add_numbers.py

def adder(*args, **kwargs):
    good = kwargs.get('good', 1)
    bad = kwargs.get('bad', 2)
    ugly = kwargs.get('ugly', 3)

    return sum(args) + good + bad + ugly

# Call the function at the bottom of the file
result_keywords = adder(1, 2, 3, good=5, ugly=1)

# Print the result
print("Sum with keyword arguments:", result_keywords)


# In[4]:


# Generalising the function for arbitary number of keyword argument
# add_numbers.py

def adder(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

# Call the function at the bottom of the file
result_arbitrary_keywords = adder(1, 2, 3, good=5, ugly=1)

# Print the result
print("Sum with arbitrary keyword arguments:", result_arbitrary_keywords)


# In[ ]:




