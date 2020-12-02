
# coding: utf-8

# In[6]:


import json
import threading 
from threading import*
import time
dt={} 


# In[7]:


def getdict():
     return dt


# In[8]:


def create(key,value,timeout=0):
    if key in dt:
        print("Error: This key already exists") 
    else:
        if(key.isalpha()):
            if len(dt)<(1024*1020*1024) and  value<=(16*1024*1024): #file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    li=[value,timeout]
                else:
                    li=[value,time.time()+timeout]
                if len(key)<=32:              #input key_name capped at 32chars
                    dt[key]=li
                else:
                    print("Error: Memory limit exceeded ")
        else:
            print("Error: Key_name must contain only Alphabets.There should be any Special characters and numbers")

                    


# In[9]:


def read(key):
    if key not in dt:
        print("Error:Key not found.Please try to read for key existing in the datastore")
    else:
        b=dt[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                json_object=json.dumps(b[0]) #return the value in the format of JsonObject "key_name:value"
                return json_object
            else:
                print("Error: time-to-live of",key,"has expired") #error message5
        else:
            json_object=json.dumps(b[0])
            return json_object


# In[10]:


def delete(key):
    if key not in dt:
        print("Error: Given key is not present in the datastore.Please enter a valid key") 
    else:
        b=dt[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del dt[key]
                print("Key ",key," is successfully deleted")
            else:
                print("Error: Time-to-live of ",key," has expired") 
        else:
            del dt[key]
            print("key ",key," is successfully deleted")

