
# coding: utf-8

# In[1]:


import Main_file_1 as d
d.create("Nitrogen",7)


# In[2]:


d.read("Nitrogen")


# In[3]:


print(type(d.read("Nitrogen")))          #int value as json object


# In[4]:


d.create("sulfur",16)


# In[5]:


d.delete("Nitrogen")


# In[6]:


#write dictionary into pickle file 
import pickle
import os
os.remove('examplePickle')
dt=d.getdict()
dbfile = open('examplePickle', 'ab')
pickle.dump(dt, dbfile)                     
dbfile.close()


# In[7]:


#read from pickle file
import pickle 
dbfile = open('examplePickle', 'rb')      
dt = pickle.load(dbfile) 
print(dt) 
dbfile.close() 


# In[9]:


d.create("Oxygen",8)


# In[10]:


d.delete("Nitrogen")


# In[11]:


d.read("Nitrogen")


# In[16]:


import threading
import time
t1=threading.Thread(target=(d.create),args=("K",18,0)) #as per the operation
t1.start()
time.sleep(5)
t2=threading.Thread(target=(d.delete),args=("K")) #as per the operation
t2.start()
time.sleep(5)


# In[17]:


d.create("Titanium",22,5)    


# In[18]:


import pickle
import os
os.remove('examplePickle')
dt=d.getdict()
dbfile = open('examplePickle', 'ab')
pickle.dump(dt, dbfile)                     
dbfile.close()


# In[19]:


import pickle 
dbfile = open('examplePickle', 'rb')      
dt = pickle.load(dbfile) 
print(dt) 
dbfile.close()

