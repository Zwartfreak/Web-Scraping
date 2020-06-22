#!/usr/bin/env python
# coding: utf-8

# # Scrapping a Wikipedia page
# 
# ### <a href=https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M>View page here</a>

# In[5]:


import urllib.request


# In[6]:


page = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')


# In[7]:


type(page)


# **Import the BeautifulSoup library so we can parse HTML and XML documents**

# In[8]:


from bs4 import BeautifulSoup


# In[9]:


soup = BeautifulSoup(page, "lxml")


# In[10]:


#print(soup.prettify())


# In[142]:


soup.title.string


# **To see all the tables present in the page**

# In[13]:


all_tables=soup.find_all("table")
#all_tables


# **We can see that there is a class named wikitable sortable from where the table begins**

# In[14]:


right_table=soup.find('table', class_='wikitable sortable')
#right_table


# In[15]:


A=[]
B=[]
C=[]


for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==3:
        b = cells[1].find(text=True)
        if b!='Not assigned\n': #To ignore rows which have Borough as Not assigned
            A.append(cells[0].find(text=True))
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))


# In[16]:


import pandas as pd

df=pd.DataFrame(A,columns=['Postal Code'])

df['Borough']=B
df['Neighborhood']=C

df.head()


# In[17]:


df.shape


# In[18]:


df['Borough'].unique()

