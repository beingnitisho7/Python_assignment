#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Choose a list of your choice and find the sum of all elements of that list.
p=[6,9,7,5,4]

def sum(p):
    total=0
    for x in range(0,len(p)):
        total=total+p[x]
    print("Sum of all elements in given list: ", total) 
sum(p)   


# In[4]:



# Write a program that returns a list which contains common elements from two lists. Avoid the duplicate elements from lists. a = [1, 1, 3, 5, 7, 9, 9] 
b = [2, 1, 6 ,9, 2, 1, 3, 5]

def sett(a,b):
    c = set(a) & set(b)  
    print(c)
sett(a,b)    


# In[5]:


# Write a code to ask an input from the user which is a string and display the string along with its length.
def count(name):
    counter = 0
    for s in name:
        counter = counter+1
    print("Length of the input string is:", counter)
name="Nitish"
count(name)  


# In[ ]:




