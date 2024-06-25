#!/usr/bin/env python
# coding: utf-8

# In[23]:


import ipywidgets as w


# In[24]:


i=w.Text(description="")
output=w.FloatText(description="")
b1=w.Button(description="1")
b2=w.Button(description="2")
b3=w.Button(description="3")
b4=w.Button(description="4")
b5=w.Button(description="5")
b6=w.Button(description="6")
b7=w.Button(description="7")
b8=w.Button(description="8")
b9=w.Button(description="9")
b0=w.Button(description="0")
bstar=w.Button(description="*")
bmin=w.Button(description="-")
bdiv=w.Button(description="/")
bplus=w.Button(description="+")
bEQ=w.Button(description="=")
bAC=w.Button(description="AC")
back=w.Button(description="<")
H1=w.HBox([i,output])
H2=w.HBox([b7,b8,b9,bAC,back])
H3=w.HBox([b4,b5,b6,bplus])
H4=w.HBox([b1,b2,b3,bmin])
H5=w.HBox([b0,bstar,bstar,bEQ])
tab=w.VBox([H1,H2,H3,H4,H5])
display(tab)


# In[25]:


def f1(self):
    i.value+="1"
def f2(self):
    i.value+="2"
def f3(self):
    i.value+="3"
def f4(self):
    i.value+="4"
def f5(self):
    i.value+="5"
def f6(self):
    i.value+="6"
def f7(self):
    i.value+="7"
def f8(self):
    i.value+="8"
def f9(self):
    i.value+="9"
def f0(self):
    i.value+="0"
def fstar(self):
    i.value+="*"
def fdiv(self):
    i.value+="/"
def fplus(self):
    i.value+="+"
def fEQ(self):
    s=eval("{}".format(i.value))
    output.value=str(s)
def fmin(self):
    i.value+="-"
def fAC(self):
    i.value=""
    output.value=0
def fback(self):
    i.value=i.value[:-1]



# In[27]:


try:
    b1.on_click(f1)
    b2.on_click(f2)
    b3.on_click(f3)
    b4.on_click(f4)
    b5.on_click(f5)
    b6.on_click(f6)
    b7.on_click(f7)
    b8.on_click(f8)
    b9.on_click(f9)
    b0.on_click(f0)
    bplus.on_click(fplus)
    bmin.on_click(fmin)
    bdiv.on_click(fdiv)
    bstar.on_click(fstar)
    bEQ.on_click(fEQ)
    bAC.on_click(fAC)
    back.on_click(fback)
    display(tab)
except:
    pass


# In[ ]:





# In[ ]:




