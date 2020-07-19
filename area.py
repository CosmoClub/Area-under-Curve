#!/usr/bin/env python
# coding: utf-8

# In[14]:


from sympy import *


# In[15]:


# input equation
print('Enter equation of the curve')
print('to raise a variable to power use **')
inp = input()


# In[16]:


# input limits
print('Enter lower limit')
low = input()
print('Enter upper limit')
up = input()


# In[17]:


# variable with resp


# In[18]:


x,y,z = symbols('x,y,z')
area = integrate(inp,(x,low,up))
print(area)


# In[ ]:




