#!/usr/bin/env python
# coding: utf-8

# In[4]:


emptylist=[]
lst=['one','two','three','four']
     
lst2=[1,2,3,4]
     
lst3=[[1,2],[3,4]]
     
lst4=[1,"ramu",24,1.24]
     
print(lst4)


# In[5]:


lst=['one','two','three','four']
print(len(lst))


# In[6]:


lst=['one','two','three','four']
lst.append("five")


# In[7]:


lst


# In[8]:


lst.insert(2,"six")


# In[9]:


lst


# In[12]:


lst=['one','two','three','four']
lst.remove("two")
lst


# In[15]:


lst=['one','two','three','four']
lst2=["five","six"]
lst.extend(lst2)


# In[16]:


lst


# In[17]:


lst=['one','two','three','four']
del lst[1]
lst


# In[20]:


lst=['one','two','three','four']
a=lst.pop(1)
a
lst


# In[22]:


lst=['one','two','three','four']
lst.remove("one")
lst 


# In[28]:


lst=['one','two','three','one']
if "two" in lst:
    print("hiii")
if "six" in lst:
    print("hii")


# In[29]:


lst.reverse()


# In[30]:


lst


# In[31]:


lst.sort()


# In[32]:


lst


# In[35]:


numbers=[3,2,1,5,6,4,7]
a=sorted(numbers,reverse=True)
a


# In[36]:


lst=[1,20,5,5,4.2]


# In[37]:


lst.sort()


# In[38]:


lst


# In[39]:


lst=[1,20,"b",5,"a"]
lst.sort()
lst


# In[40]:


lst=[1,2,3,4,5,6]
abc=lst
abc.append(7)
lst


# In[41]:


dir(lst)


# In[43]:


a="atchut"
b=a.split("c")

a
b


# In[44]:


lst=["one","two","thre"]
for i in lst:
    print(i)


# In[46]:


sqr=[]
for i in range(10):
    sqr.append(i**2)
sqr


# In[49]:


sqr=[i**2 for i in range(10)]
sqr


# In[56]:


lst=[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
k=[i+10 for i in range(100) if not i%2==0]
print(k,end="")


# In[58]:


k=[i*30 for i in range(100) if i%2==0 if i%6==0]
print(k,end="")


# In[59]:


####matrix

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]


# In[69]:


for i in range(4):
    lst=[]
    
    for row in matrix:
        #print(row)
        lst.append(row[i])
        #print(lst)
        transposed.append(lst)
print(transposed)


# In[65]:


transposed=[[row[i] for row in matrix] for i in range(4)]


# In[66]:


transposed


# In[ ]:




