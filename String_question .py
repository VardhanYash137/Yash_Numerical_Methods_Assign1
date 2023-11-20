#!/usr/bin/env python
# coding: utf-8

# In[5]:


# String
S = 'mumbai'

# Print each character and its Unicode code point
print("Characters and their Unicode code points (using for loop):")
for char in S:
    code_point = ord(char)
    print(f"{char}: {code_point}")

# Compute the sum of Unicode code points
sum_of_code_points = 0
for char in S:
    sum_of_code_points += ord(char)
print("\nSum of Unicode code points:", sum_of_code_points)


# Using list comprehension to create a list of Unicode code points
unicode_list_comprehension = [ord(char) for char in S]
print("List of Unicode code points using list comprehension:", unicode_list_comprehension)

# Using the map class to create a list of Unicode code points
unicode_map_class = list(map(ord, S))
print("List of Unicode code points using map class:", unicode_map_class)


# In[ ]:




