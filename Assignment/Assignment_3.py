#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1. Write a program to display all prime numbers from 1 to 100.
for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(Number)


# In[3]:


# Ask the user for a string and print out whether this string is a palindrome or not.
def palindrom():
    name = input("Please Enter a word")
    if name[::-1] == name[0:]:
        print(name, " is a palindrome")
    else:
        print(name, " is not a palindrome")
palindrom()        


# In[4]:


# Create a dictionary that has a key value pair of lettersand the number of occurrencesof that letter in a string
def pypart(n): 
    myList = [] 
    for i in range(1,n+1): 
        myList.append("*"*i) 
    print("\n".join(myList)) 
pypart(4)


# In[ ]:




