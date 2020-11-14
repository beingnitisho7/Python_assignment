#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Write a program that will convert Fahrenheit to Celsius in degrees.
def celsius(num):
    fahrenheit = (num * 9/5) + 32
    print('%.3f Celsius is: %0.2f Fahrenheit' %(num, fahrenheit))
celsius(23)  


# In[10]:


# Write  a  program  that  takes  seconds  as  time  units  and  converts  it  to  minutes  and seconds. 
def time(time_units):
    minutes = time_units // 60
    time_units %= 60
    seconds = time_units
    print("Converted time-> %d minute and %dsecond" % (minutes, seconds))
time(3800)    


# In[11]:


# Consider a list of any arbitrary elements. Your codeshould print the length of the list and first and fourth element of the list.
Elements=['apple','mango','pine apple','Banana']

def element(elements):
    print(len(Elements))
    print(Elements[0])
    print(Elements[3])
Elements=['apple','mango','pine apple','Banana'] 
element(Elements)


# In[12]:


# Create a list of any arbitrary elements. Your code should show the list methods as pop, insert and remove. 
Elements=['apple','mango','pine apple','Banana']

def element_pop(elements):
    Elements.pop(0)
    print(Elements)
    Elements.insert(1,'lichy')
    print(Elements)
    Elements.remove('mango')
    print(Elements)
    
element_pop(Elements)  


# In[ ]:




