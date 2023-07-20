
# coding: utf-8

# In[3]:


import numpy as np


# In[2]:


list1=[6,7,8]
np.array(list1)


# In[3]:


list_of_list=[[1,2,3],[4,5,6],[7,8,9]]
np.array(list_of_list)


# In[4]:


np.arange(2,5)


# In[6]:


np.arange(1,100)


# In[9]:


np.arange(1,30,5)


# In[10]:


np.arange(5)


# In[15]:


np.zeros(5)


# In[16]:


np.zeros(5,int)


# In[18]:


np.ones(5,int)


# In[19]:


np.zeros((2,5),int)


# In[20]:


np.ones((3,3))


# In[21]:


np.ones((3,4),int)


# In[37]:


np.linspace(0,2,5) #linearly space


# In[29]:


np.linspace(0,20,8)


# In[8]:


a=np.eye(5) #gives identity matrix of 5*5
a


# In[35]:


np.random.rand(2,2)


# In[41]:


arr=np.random.randn(2,4) # randn includes -ve numbers also
arr


# In[42]:


np.random.randint(0,100)


# In[47]:


np.random.randint(20,56,10) # 10 represents number of items to display


# In[4]:


sample=np.arange(12)
sample


# In[5]:


sample1=np.random.randint(0,100,20)
sample1


# In[6]:


sample.reshape(3,4)


# In[7]:


sample.argmax()


# In[9]:


a.T


# In[12]:


samp=np.arange(10,21)
samp


# In[14]:


samp[3::2]


# In[16]:


samp[0:2]=100
samp


# In[17]:


sub_samp=samp[0:5]
sub_samp


# In[18]:


sub_samp[:]=5
sub_samp


# In[19]:


samp # subset array changes original array also


# ### 2d array

# In[22]:


sample_matrix=np.array([[50,10,30,12],[48,24,75,86],[74,45,85,78]])
sample_matrix


# In[24]:


sample_matrix[2,2]


# In[29]:


sample_matrix[1,:]


# In[26]:


sample_matrix[2]


# In[34]:


sample_matrix[:,(3,1,0)] #3,1,0 represents column number here

