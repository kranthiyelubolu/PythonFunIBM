#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install yfinance pandas requests beautifulsoup4 matplotlib plotly notebook')
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd

import yfinance as yf


# In[7]:


# Download Tesla stock data
gme_data = yf.download('GME')

# Reset the index
gme_data.reset_index(inplace=True)

# Display the first five rows
print(gme_data.head())


# In[8]:


# Download Tesla's financial data
GME = yf.Ticker("GME")

# Extract quarterly revenue data
GME_financials = tesla.quarterly_financials

# Convert to a DataFrame and select only the 'Total Revenue' row
GME_revenue = GME_financials.loc['Total Revenue'].to_frame().reset_index()
GME_revenue.columns = ['Date', 'Revenue']

# Display the last five rows of the tesla_revenue DataFrame
print(GME_revenue.tail())


# In[10]:


import yfinance as yf
import matplotlib.pyplot as plt

# Download Tesla stock data
tesla_data = yf.download('GME')

# Reset the index to make 'Date' a column
tesla_data.reset_index(inplace=True)

# Define the make_graph function
def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Close'], color='blue', label="Closing Price")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Stock Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Call the make_graph function with Tesla stock data and a title
make_graph(tesla_data, "Gamestop Stock Price Over Time")


# In[6]:





# In[ ]:




