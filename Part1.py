#!/usr/bin/env python
# coding: utf-8

# # Values and Types

# ## Types

# In[1]:


type("Hello, World!")


# In[2]:


type(7)


# In[3]:


type(3.2)


# In[4]:


type("17")


# In[5]:


type("3.2")


# ## Variables

# In[8]:


message = "And now for something completely different"
n = 17 
pi = 3.14


# In[10]:


type(message)


# In[11]:


type(n)


# In[12]:


type(pi)


# ## Operators and Operands

# In[13]:


minute = 59 
minute/60


# In[14]:


minute//60


# In[15]:


minute*5


# In[16]:


minute % 2


# In[17]:


minute - 50


# In[18]:


minute + 65


# In[19]:


2 ** 4


# In[22]:


2*(3-1)


# In[23]:


(1+1)**(5-2)


# In[24]:


(minute*100)/60


# In[25]:


2**1 + 1


# In[26]:


3*2**2


# In[27]:


6+4/2


# In[29]:


customerAge = input("write customer's age: ")


# ## String Operations

# In[30]:


"2"-"1"


# In[32]:


first = "throat"
second = "warbler"
first + " " + second


# In[33]:


"spam" * 3


# In[34]:


newinput = input("new input : ")


# In[36]:


type(newinput)


# In[37]:


newinput + 5


# In[38]:


newinput2 =  int(input("new input : "))
                 


# In[39]:


type(newinput2)


# In[40]:


newinput2 + 5


# In[45]:


x = "34"
a = int(x)


# In[46]:


type(a)


# In[48]:


nameString = "Çisem Akman"


# In[49]:


nameString


# ## Index

# In[50]:


nameString[0]


# In[51]:


nameString[7]


# In[52]:


nameString[5]


# In[53]:


nameString[:]


# In[54]:


nameString[-1]


# In[57]:


nameString[0:4]


# In[59]:


nameString[0] + nameString[-1]


# In[61]:


nameString[2:6]


# In[62]:


newString = "0123456789"


# In[63]:


newString[2:6]


# In[64]:


newString[2:]


# In[65]:


newString[3:]


# In[66]:


newString[:3]


# ## Slicing
# 

# In[67]:


income = "AgeofAhmetis65"


# In[71]:


agePerson = income[-2:]
agePerson


# In[72]:


#Step Size


# In[75]:


income[1:5]


# In[76]:


income[1:5:2]


# In[79]:


income[::5]


# In[80]:


income[::3]


# In[81]:


income[::-1] 


# ## Methods of Strings

# In[84]:


myName = "çisem"


# In[85]:


myName.capitalize()  #upper first charachter


# In[87]:


myName #no change


# In[88]:


myNewName = myName.capitalize()


# In[89]:


myNewName


# In[90]:


myName


# In[91]:


myFullName = "Çisem Akman"


# In[92]:


myFullName.split()


# In[93]:


type(myFullName.split())


# In[94]:


myFullName.upper()


# In[95]:


myName * 10


# In[96]:


myName + "Akman"


# In[99]:


myLastName = "Akman"


# In[101]:


myName.capitalize() + " " +  myLastName.upper()

