#!/usr/bin/env python
# coding: utf-8

# In[7]:


# boolean on any data type returns true
bool(1)


# In[8]:


bool(0)


# In[4]:


bool('yes')


# In[1]:


bool([2,'j',4.66])


# In[5]:


print(2 > 5)


# In[13]:


print(5 >= 5)


# In[17]:


#comparison between variables
x=100
y=100.1
print(y < x)


# In[20]:


isinstance(100.1, int)


# In[19]:


isinstance('name', str)


# In[26]:


any([2,1,0])


# In[28]:


any([0,''])


# In[2]:


#using booleans in if statement
if (45 <= 40) == False:
    print('Yes')
else:
    print('No')


# In[12]:


def function():
    return True

function()

