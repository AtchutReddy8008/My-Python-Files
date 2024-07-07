#!/usr/bin/env python
# coding: utf-8

# In[26]:


import ipywidgets as w
import math


# ### new caluclator with inverved functions

# In[1]:


import ipywidgets as w
import math

bw = '100px'
bh = '50px'
l = w.Layout(width=bw, height=bh)
i = w.Text(description="")
output = w.FloatText(description="")
b1 = w.Button(description="1")
b2 = w.Button(description="2")
b3 = w.Button(description="3")
b4 = w.Button(description="4")
b5 = w.Button(description="5")
b6 = w.Button(description="6")
b7 = w.Button(description="7")
b8 = w.Button(description="8")
b9 = w.Button(description="9")
b0 = w.Button(description="0")
bdot = w.Button(description=".")
bstar = w.Button(description="*")
bmin = w.Button(description="-")
bdiv = w.Button(description="/")
bplus = w.Button(description="+")
bEQ = w.Button(description="=")
bAC = w.Button(description="AC")
back = w.Button(description="<")
bsin = w.Button(description="sin")
bcos = w.Button(description="cos")
btan = w.Button(description="tan")
bsinin = w.Button(description="sin⁻¹")
bcosin = w.Button(description="cos⁻¹")
btanin = w.Button(description="tan⁻¹")
bexp = w.Button(description="EXP")
bEQ.style.button_color = "blue"
bbra1 = w.Button(description="(")
bbra2 = w.Button(description=")")
bmod = w.Button(description="%")
bpi = w.Button(description="π")
bln = w.Button(description="ln")
blog = w.Button(description="log")
bdeg = w.Button(description="Deg")
bsqrt = w.Button(description="√")
bpow = w.Button(description="x\u02b8")
bxnot = w.Button(description="x!")
be = w.Button(description="e")
brad = w.Button(description="rad")
bANS = w.Button(description="Ans")
blnv = w.Button(description="lnv")

H0 = w.HBox([brad, bdeg, bxnot, bbra1, bbra2, bmod, bAC])
H1 = w.HBox([i, output])
H2 = w.HBox([bsin, blnv, bln, b7, b8, b9, bdiv])
H3 = w.HBox([bcos, bpi, blog, b4, b5, b6, bstar])
H4 = w.HBox([btan, be, bsqrt, b1, b2, b3, bmin])
H5 = w.HBox([bANS, bexp, bpow, b0, bdot, bEQ, bplus])
tab = w.VBox([H1, H0, H2, H3, H4, H5])

def f1(self): i.value += "1"
def f2(self): i.value += "2"
def f3(self): i.value += "3"
def f4(self): i.value += "4"
def f5(self): i.value += "5"
def f6(self): i.value += "6"
def f7(self): i.value += "7"
def f8(self): i.value += "8"
def f9(self): i.value += "9"
def f0(self): i.value += "0"
def fstar(self): i.value += "*"
def fdiv(self): i.value += "/"
def fplus(self): i.value += "+"
def fEQ(self): output.value = eval(i.value)
def fmin(self): i.value += "-"
def fAC(self): i.value, output.value = "", 0
def fback(self): i.value = i.value[:-1]
def fsin(self): output.value = math.sin(eval(i.value))
def fcos(self): output.value = math.cos(eval(i.value))
def ftan(self): output.value = math.tan(eval(i.value))
def fbra1(self): i.value += "("
def fbra2(self): i.value += ")"
def flog(self): output.value = math.log10(eval(i.value))
def fe(self): i.value += str(math.e)
def fpi(self): i.value += str(math.pi)
def fdeg(self): output.value = math.degrees(eval(i.value))
def fxnot(self): output.value = math.factorial(eval(i.value))
def fsqrt(self): output.value = math.sqrt(eval(i.value))
def ln(self): output.value = math.log(eval(i.value))
def frad(self): output.value = math.radians(eval(i.value))
def ffmod(self): i.value += "%"

# Inverse functions
def fsinin(self): output.value = math.degrees(math.asin(eval(i.value)))
def fcosin(self): output.value = math.degrees(math.acos(eval(i.value)))
def ftanin(self): output.value = math.degrees(math.atan(eval(i.value)))
def ftaninh(self): output.value = math.degrees(math.atanh(eval(i.value)))

# Toggle inverse functions
def flnv(self):
    if bsin.description == "sin":
        bsin.description = "sin⁻¹"
        bsin.on_click(fsinin)
    else:
        bsin.description = "sin"
        bsin.on_click(fsin)
    if bcos.description == "cos":
        bcos.description = "cos⁻¹"
        bcos.on_click(fcosin)
    else:
        bcos.description = "cos"
        bcos.on_click(fcos)
    if btan.description == "tan":
        btan.description = "tan⁻¹"
        btan.on_click(ftanin)
    else:
        btan.description = "tan"
        btan.on_click(ftan)

# Assign button actions
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
bsin.on_click(fsin)
bcos.on_click(fcos)
btan.on_click(ftan)
bbra1.on_click(fbra1)
bbra2.on_click(fbra2)
bmod.on_click(ffmod)
bpi.on_click(fpi)
bln.on_click(ln)
blog.on_click(flog)
bdeg.on_click(fdeg)
bsqrt.on_click(fsqrt)
##bpow.on_click(lambda self: i.value += "**")
bxnot.on_click(fxnot)
be.on_click(fe)
brad.on_click(frad)
bANS.on_click(fEQ)
blnv.on_click(flnv)

display(tab)


# In[ ]:




