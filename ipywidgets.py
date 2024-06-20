#!/usr/bin/env python
# coding: utf-8

# In[10]:


import ipywidgets as w


# In[8]:


from ipywidgets import *


# In[ ]:


w.RadioButtons


# In[4]:


len(dir(w))


# In[5]:


def h(a,b):
    return a+b
w.interact(h,a=10,b=30)


# In[6]:


def k(l,p):
    return l
    return p
w.interactive(k,l=True,p=30)
#     Returns the value of l. The line return p is unreachable and thus has no effect.
#     Creates an interactive widget to adjust l and p, showing the result of k in real-time. Only the value of l will affect the output.
#     The correct method for creating the widget should be w.interact instead of w.interactive.


# In[7]:


def k(l,p):
    return l
    return p
w.interact(k,l=True,p=30)


# In[8]:


def k(s):
    return s
#     Returns the value of s.
#     Creates an interactive widget dropdown to select a value for s from the list [1, 2, 3], showing the result of k(s) in real-time.


# In[9]:


w.interact(k,s=[1,2,3])


# In[10]:


def z(s):
    for i in range(s):
        print(i)


# In[11]:


w.interact(z,s=10)


# In[12]:


def f(x):
    return x+12


# In[13]:


g=w.interact(f,x=10)


# In[14]:


display(g)


# In[15]:


def h(p,q):
    return (p,q)
#     p: A BoundedFloatText widget for entering a float value with bounds.
#     q: A FloatText widget for entering any float value.
#     Function h():Returns the current values of p and q as a tuple.
#     Function inter(self):Uses w.interact to create an interactive widget with the h function.
#     A button labeled "Click me" that, when clicked, triggers the inter function to display the interactive widget.
#     Enter values in the p and q widgets.
#     Click the "Click me" button to display the interactive output of the h function, showing the current values of p and q.


# In[16]:


p=w.BoundedFloatText()
q=w.FloatText()
def h():
    return (p.value,q.value)
def inter(self):
    w.interact(h);
b=w.Button(description="click me")
display(p)
display(q)
display(b)
b.on_click(inter)


# In[17]:


slider1=w.IntSlider()
slider2=w.IntSlider()
display(slider1)
display(slider2)
def out_put():
    print(slider1.value+slider2.value)
def execution(self):
    w.interact(out_put)
button=w.Button(description="click")
button.on_click(execution)
display(button)

#     slider1: An integer slider (IntSlider widget) for selecting an integer value.
#     slider2: Another integer slider (IntSlider widget) for selecting another integer value.
#     out_put(): Outputs the current values of slider1 and slider2 to the console.
#     execution(self): Uses w.interact to create an interactive output of the out_put function.
#     button: A button labeled "Click me" that, when clicked, triggers the execution function to display the interactive output of out_put.
#     Adjust slider1 and slider2 to desired integer values.
#     Click the "Click me" button to display the current values of slider1 and slider2 in the console.


# In[18]:


a1=w.IntSlider(value=40,min=30,max=60,step=5)
b1=w.IntSlider(value=40,min=20,max=100,step=1)
j=w.Button(description="submit")
j1=w.Text(description="value:")
display(w.HBox([a1,b1,j,j1]))
def add():
    j1.value=str(a1.value+b1.value)
    #print(str(a1.value+b1.value))
def display1(self):
    w.interact(add)
j.on_click(display1)



#     a1: An integer slider (IntSlider widget) for selecting an integer value.
#     b1: Another integer slider (IntSlider widget) for selecting another integer value.
#     j: A button (Button widget) labeled "Submit".
#     j1: A text box (Text widget) labeled "Value:" to display the sum of a1 and b1
#     Widgets (a1, b1, j, j1) are displayed in a vertical box (VBox) layout using display(w.VBox([...]))
#     add(): Updates the j1 text widget with the sum of a1.value and b1.value.
#     display1(self): Uses w.interact to create an interactive output of the add function.
#     Clicking the "Submit" button (j) triggers the display1 function, which updates j1 with the current sum of a1 and b1.
#     Adjust a1 and b1 sliders to desired integer values.
#     Click the "Submit" button (j) to display the sum of a1 and b1 in the j1 text box.


# In[5]:


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# In[6]:


@interact(start=6,end=22)
def primes_between(start, end):
    """Return a list of prime numbers between start and end (inclusive)."""
    return [num for num in range(start, end + 1) if is_prime(num)]


# In[13]:


import ipywidgets as widgets
from IPython.display import display

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
        i += 6
    return True

def primes_between(start, end):
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
    """Return a list of prime numbers between start and end (inclusive)."""
    return [num for num in range(start, end + 1) if is_prime(num)]

def find_primes(start, end):
    """Display prime numbers between start and end."""
    primes = primes_between(start, end)
    print(f"Prime numbers between {start} and {end}: {primes}")

# Create widgets
start_widget = widgets.IntText(value=10, description='Start:')
end_widget = widgets.IntText(value=50, description='End:')
button = widgets.Button(description="Find Primes")

# Define button click event
def on_button_click(b):
    start = start_widget.value
    end = end_widget.value
    find_primes(start, end)

# Assign the event to the button
button.on_click(on_button_click)

# Display widgets
display(start_widget, end_widget, button)


# In[15]:


import ipywidgets as widgets
from IPython.display import display

# Function to calculate tax based on income
def calculate_tax(income):
    if income > 0 and income <= 3:
        #print("s1")
        tax = 0
    elif income > 3 and income <= 6:
        #print("s2")
        tax = (income - 3) * (5 / 100)
    elif income > 6 and income <= 9:
        #print("s3")
        tax = (income - 6) * (10 / 100) + (3) * (5 / 100)
    elif income > 9 and income < 12:
        #print("s4")
        tax = (income - 9) * (15 / 100) + (6) * (10 / 100) + (3) * (5 / 100)
    elif income >= 12 and income <= 15:
        #print("s5")
        tax = (income - 12) * (20 / 100) + (9) * (15 / 100) + (6) * (10 / 100) + (3) * (5 / 100)
    elif income > 15:
        #print("s6")
        tax = (income - 15) * (30 / 100) + (12) * (20 / 100) + (9) * (15 / 100) + (6) * (10 / 100) + (3) * (5 / 100)
    print(int(tax * 100000))

# Create widgets
income_widget = widgets.FloatText(value=0.0, description='Income:')
button = widgets.Button(description="Calculate Tax")

# Define button click event
def on_button_click(b):
    income = income_widget.value / 100000
    calculate_tax(income)

# Assign the event to the button
button.on_click(on_button_click)

# Display widgets
display(income_widget, button)


# In[11]:


import ipywidgets as widgets
from IPython.display import display
@interact(income=600000)
def calculate_tax(income):
    income /= 100000
    if income > 0 and income <= 3:
        tax = 0
    elif income > 3 and income <= 6:
        tax = (income - 3) * 0.05
    elif income > 6 and income <= 9:
        tax = (income - 6) * 0.10 + 3 * 0.05
    elif income > 9 and income < 12:
        tax = (income - 9) * 0.15 + 3 * 0.10 + 3 * 0.05
    elif income >= 12 and income <= 15:
        tax = (income - 12) * 0.20 + 3 * 0.15 + 3 * 0.10 + 3 * 0.05
    else:
        tax = (income - 15) * 0.30 + 3 * 0.20 + 3 * 0.15 + 3 * 0.10 + 3 * 0.05
    print(int(tax * 100000))

# income_widget = widgets.FloatText(value=0.0, description='Income:')
# button = widgets.Button(description="Calculate Tax")

# button.on_click(lambda b: calculate_tax(income_widget.value))

# display(income_widget, button)


# In[17]:


import ipywidgets as widgets
from IPython.display import display

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primes_between(start, end):
    """Return a list of prime numbers between start and end (inclusive)."""
    return [num for num in range(start, end + 1) if is_prime(num)]

def on_button_click(b):
    start = start_input.value
    end = end_input.value
    prime_numbers = primes_between(start, end)
    output.value = str(prime_numbers)

start_input = widgets.IntText(
    value=10,
    description='Start:',
    disabled=False
)

end_input = widgets.IntText(
    value=50,
    description='End:',
    disabled=False
)

button = widgets.Button(
    description='Find Primes',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check' # (FontAwesome names without the `fa-` prefix)
)

output = widgets.Text(
    value='',
    description='Primes:',
    disabled=True
)

button.on_click(on_button_click)

display(start_input, end_input, button, output)


# In[10]:


@interact(l=900,u=1000)
def p(l,u):
    for num in range(l, u+1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)


# In[14]:


import ipywidgets as widgets
from IPython.display import display

@interact(income=600000)
def calculate_tax(income):
    income /= 100000
    if income > 0 and income <= 3:
        tax = 0
    elif income > 3 and income <= 6:
        tax = (income - 3) * 0.05
    elif income > 6 and income <= 9:
        tax = (income - 6) * 0.10 + 3 * 0.05
    elif income > 9 and income < 12:
        tax = (income - 9) * 0.15 + 3 * 0.10 + 3 * 0.05
    elif income >= 12 and income <= 15:
        tax = (income - 12) * 0.20 + 3 * 0.15 + 3 * 0.10 + 3 * 0.05
    else:
        tax = (income - 15) * 0.30 + 3 * 0.20 + 3 * 0.15 + 3 * 0.10 + 3 * 0.05
    print(int(tax * 100000))


# In[18]:


import ipywidgets as w
a1=w.HTML("<H1>application form")                                                     # h1 tag will gives header 
b1=w.Text(description="Name:")                                                        #    
c1=w.DatePicker(description="date of birth")
d1=w.RadioButtons(description="gender",options=["Male","Female"])
e1=w.Text(description="F.N:",value="Name")
f1=w.Text(description="school")
g1=w.Textarea(description="Address")
h1=w.Button(description="values")
h3=w.Textarea(description="values")
display(w.VBox([a1,b1,c1,d1,e1,f1,h1,h3]))
def prt():
    h3.value=("{},{},{},{},{},{}".format(b1.value,c1.value,d1.value,e1.value,(f1.value),(g1.value)))
def send(self):
    w.interact(prt)
h1.on_click(send)


# In[18]:


name=w.Text(description="name:",padding=4)
color=w.Dropdown(description="color:",padding=4,options=["red","orange","yellow","green","blue"])
page1=w.Box(children=[name,color],padding=4)
age=w.IntSlider(description="age:",padding=4,min=0,max=120,value=25)
gender=w.RadioButtons(description="gender",padding=4,options=["male","female"])
page2=w.Box(children=[age,gender],adding=4)
tabs=w.Tab(children=[page1,page2])
hn=w.Textarea(description="value")
display(tabs)
tabs.set_title(0,"name")
tabs.set_title(1,"details")
pri=0
def g():
    global pri
    pri+=1
    s=(str(pri)+".name:"+name.value)
    h=("age:"+str(age.value))
    k=("color:"+str(color.value))
    j=("gender"+str(gender.value))
    hn.value="{}.{}.{}.{}".format(s,h,k,j)
button=w.Button(description="submit")
button.style.button_color="yellow"
display(button)
def u(self):
    w.interact(g)
button.on_click(u)
display(hn)
         
       


# In[24]:


from ipywidgets import *


# In[25]:


RadioButtons(description="gender",padding=4,options=["male","female"])


# In[26]:


exec("print(5+6)")


# In[29]:


def test():
    print("fun")
exec("test()")


# In[28]:


h=w.Text(description="enter operation")
button=w.Button(description="click me")
hn=w.Textarea(description="value")
def operation():
    g="print({})".format(h.value)
    exec(g)
    
def execute(self):
    hn.value=w.interact(operation)
button.on_click(execute)
display(h)
display(button)


# In[3]:


import ipywidgets as w
from IPython.display import display

# Create the widgets
h = w.Text(description="Enter operation")
button = w.Button(description="Click me")
hn = w.Textarea(description="Value")

def operation(change):
    try:
        # Safely evaluate the input expression
        result = eval(h.value)
        hn.value = str(result)
    except Exception as e:
        hn.value = str(e)

# Function to be called on button click
def execute(b):
    operation(None)

# Bind the button click to the execute function
button.on_click(execute)

# Display the widgets
display(h)
display(hn)
display(button)


# In[7]:


import ipywidgets as w
from IPython.display import display

# Create the widgets
h = w.Text(description="Enter operation")
button = w.Button(description="Click me")
hn = w.Textarea(description="Value")

def operation():
    # Evaluate the input expression
    result = eval(h.value)
    # Set the result in the Textarea widget
    hn.value = str(result)

# Function to be called on button click
def execute(b):
    operation()

# Bind the button click to the execute function
button.on_click(execute)

# Display the widgets
display(h)
display(hn)
display(button)



# In[21]:


import ipywidgets as widgets
from IPython.display import display

# Input widgets
number1 = widgets.FloatText(description="Number 1:")
number2 = widgets.FloatText(description="Number 2:")
operation = widgets.Dropdown(
    options=['+', '-', '*', '/'],
    description='Operation:'
)

# Button and output widget
calculate_button = widgets.Button(description="Calculate")
output = widgets.Output()

# Function to perform calculation
def calculate(button):
    with output:
        output.clear_output()
        num1 = number1.value
        num2 = number2.value
        op = operation.value
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        output.append_stdout(f"Result: {result}\n")

# Attach function to button
calculate_button.on_click(calculate)

# Display widgets
display(number1, number2, operation, calculate_button, output)


# In[26]:


import ipywidgets as widgets
from IPython.display import display

# Input widgets
number1 = widgets.FloatText(description="Number 1:")
number2 = widgets.FloatText(description="Number 2:")
operation = widgets.Dropdown(
    options=['+', '-', '*', '/'],
    description='Operation:'
)
hn = w.Textarea(description="Value")
# Button and result widget
calculate_button = widgets.Button(description="Calculate")
result_label = widgets.Label(value="Result: ")

# Function to perform calculation
def calculate(button):
    num1 = number1.value
    num2 = number2.value
    op = operation.value
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    hn.value = f"{result}"

# Attach function to button
calculate_button.on_click(calculate)

# Display widgets
display(number1, number2, operation, calculate_button,hn)


# In[ ]:




