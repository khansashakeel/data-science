#!/usr/bin/env python
# coding: utf-8

# Question 1 - Extracting Tesla Stock Data Using yfinance

# In[1]:


get_ipython().system('pip install yfinance')


# In[2]:


get_ipython().system('pip install plotly')


# In[3]:


get_ipython().system('pip install')


# In[2]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[3]:


tesla = yf.Ticker("TSLA")


# In[4]:


tesla_data = tesla.history(period="max")


# In[5]:


tesla_data.reset_index(inplace=True)


# In[6]:


tesla_data.head()


# In[7]:


url ="https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"


# In[8]:


html_data= requests.get(url).text
html_data


# In[10]:


soup = BeautifulSoup(html_data, 'html5lib')


# In[11]:


soup


# In[13]:


gamestop = yf.Ticker("GME")


# In[14]:


gme_data = gamestop.history(period="max")


# In[15]:


gme_data.reset_index(inplace=True)


# In[16]:


gme_data.head()


# In[17]:


url ="https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data= requests.get(url).text
html_data


# In[18]:


soup = BeautifulSoup(html_data, "html5lib")


# In[19]:


import bs4
gme_revenue= pd.read_html(url, "GameStop quarterly Revenue")[0]
gme_revenue=gme_revenue.rename(columns={"GameStop quarterly Revenue (millions of US$): 'Date', 'GameStop quarterly Revenue'"})
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(",", "").str.replace("$", "")


# In[22]:


#Q#6

make_graph(tesla_data, tesla_revenue, 'Tesla stock data graph')


# In[20]:


make_graph(gme_data, gme_revenue, 'GameStop stock data graph')


# In[ ]:





# In[ ]:




