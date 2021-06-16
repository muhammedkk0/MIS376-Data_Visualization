#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[2]:


df=pd.read_csv("import_goods.csv") #the data of import goods in the world
df1=pd.read_csv("export_goods.csv") #the data of export goods in the world
df2=pd.read_csv("GDP_Country.csv")
df3=pd.read_csv("Services_Value.csv")


# In[3]:


#merge 'Value' from two datasets
df.rename(columns={"Value": "Import_Value"},inplace=True)
df1.rename(columns={"Value": "Export_Value"},inplace=True)
df['Export_Value']=df1['Export_Value'].values


# In[4]:


df['TIME'] = pd.to_datetime(df['TIME'])
df3['TIME'] = pd.to_datetime(df3['TIME'])


# In[5]:


df.head()


# In[6]:


plt.figure(figsize=(20,10)) #creating subplots and determining the dimensions

plt.subplot(2,2,1) #specifies the plane of the graphs and which graph it is
plt.plot(df.TIME[:13],df.Import_Value[:13],color="red",linewidth=3,marker="o") #import line and properties(color,line width)
plt.plot(df.TIME[:13],df.Export_Value[:13],color="black",linewidth=3,marker="o")#Export line and properties(color,line width
plt.xlabel("Date") #to name the x column
plt.ylabel("Billion US Dollars") #to name the y column
plt.title("The Amount of Goods Import and Export in Australia",fontsize=15,color="black") #to name the title of the graph and properties
plt.legend(['Import', 'Export']) #to add legend
plt.grid() #gives the graph a grid structure

plt.subplot(2,2,2)
plt.plot(df.TIME[13:26],df.Import_Value[13:26],color="blue",linewidth=3,marker="o")
plt.plot(df.TIME[13:26],df.Export_Value[13:26],color="dimgray",linewidth=3,marker="o")
plt.xlabel("Date")
plt.ylabel("Billion US Dollars")
plt.title("The Amount of Goods Import and Export in Canada",fontsize=15,color="black")
plt.legend(['Import', 'Export'])
plt.grid()

plt.subplot(2,2,3)
plt.plot(df.TIME[26:39],df.Import_Value[26:39],color="purple",linewidth=3,marker="o")
plt.plot(df.TIME[26:39],df.Export_Value[26:39],color="hotpink",linewidth=3,marker="o")
plt.xlabel("Date")
plt.ylabel("Billion US Dollars")
plt.title("The Amount of Goods Import and Export in France",fontsize=15,color="black")
plt.legend(['Import', 'Export'])
plt.grid()

plt.subplot(2,2,4)
plt.plot(df.TIME[39:52],df.Import_Value[39:52],color="magenta",linewidth=3,marker="o")
plt.plot(df.TIME[39:52],df.Export_Value[39:52],color="tomato",linewidth=3,marker="o")
plt.xlabel("Date")
plt.ylabel("Billion US Dollars")
plt.title("The Amount of Goods Import and Export in Germany",fontsize=15,color="black")
plt.legend(['Import', 'Export'])
plt.grid()
plt.show()


# In[7]:


plt.figure(figsize=(20,10))

plt.subplot(2,2,1)
plt.plot(df.TIME[65:78],df.Import_Value[65:78],color="black",linewidth=3,marker="o")
plt.plot(df.TIME[65:78],df.Export_Value[65:78],color="olive",linewidth=3,marker="o")
plt.xlabel("Date")
plt.ylabel("Billion US Dollars")
plt.title("The Amount of Goods Import and Export in Japan",fontsize=15,color="black")
plt.legend(['Import', 'Export'])
plt.grid()

plt.subplot(2,2,2)
plt.plot(df.TIME[104:117],df.Import_Value[104:117],color="chocolate",linewidth=3,marker="o")
plt.plot(df.TIME[104:117],df.Export_Value[104:117],color="black",linewidth=3,marker="o")
plt.xlabel("Date")
plt.ylabel("Billion US Dollars")
plt.title("The Amount of Goods Import and Export in Turkey",fontsize=15,color="black")
plt.legend(['Import', 'Export'])
plt.grid()

plt.subplot(2,2,3)
plt.plot(df.TIME[143:156],df.Import_Value[143:156],color="yellow",linewidth=3,marker="o")
plt.plot(df.TIME[143:156],df.Export_Value[143:156],color="navy",linewidth=3,marker="o")
plt.xlabel("Date")
plt.ylabel("Billion US Dollars")
plt.title("The Amount of Goods Import and Export in Argentina",fontsize=15,color="black")
plt.legend(['Import', 'Export'])
plt.grid()

plt.subplot(2,2,4)
plt.plot(df.TIME[195:207],df.Import_Value[195:207],color="teal",linewidth=3,marker="o")
plt.plot(df.TIME[195:207],df.Export_Value[195:207],color="skyblue",linewidth=3,marker="o")
plt.xlabel("Date")
plt.ylabel("Billion US Dollars")
plt.title("The Amount of Goods Import and Export in Saudi Arabia",fontsize=15,color="black")
plt.legend(['Import', 'Export'])
plt.grid()
plt.show()


# In[8]:


labels = ["Australia", "Canada", "France", "Germany", "Italy","japan","Netherlands","Spain","Turkey","United Kıngdom",
          "United States","Brazil","China","India","Argentina","Saudi Arabia"]

# Create subplots: use 'domain' type for Pie subplot
fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels,values=[54.1782, 113.878, 165.955, 310.638, 120.78, 182.355,
                                           158.101, 94.2466, 51.265, 152.723, 630.589, 43.886, 
                                           536.125, 42.133, 12.4974, 39.3424 ], name="Import Goods"),
              1, 1)
fig.add_trace(go.Pie(labels=labels, values=[46.7704, 80.2758, 118.579, 250.724, 84.2188, 156.303,
                                           132.571, 62.8175, 42.54, 104.693, 506.861, 35.1314,
                                           489.083, 32.7008, 8.97283,32.6459], name="Import Goods"),
              1, 2)

# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+value+name",textinfo='value')

fig.update_layout(
    title_text="Comparison of Goods Imported by Countries in Q2 2019 and Q2 2020(Million US Dollars)",
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="green",
    title_x=0.5,
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='Q2 2019', x=0.16, y=0.5, font_size=20, showarrow=False),
                 dict(text='Q2 2020', x=0.84, y=0.5, font_size=20, showarrow=False)])
fig.show()


# In[9]:


labels = ["Australia", "Canada", "France", "Germany", "Italy","Japan","Netherlands","Spain","Turkey","United Kıngdom",
          "United States","Argentina","Brazil","China","India","Saudi Arabia"]

# Create subplots: use 'domain' type for Pie subplot
fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels,values=[69.9985, 114.991, 145.325, 371.471, 134.633, 175.6,
                                           175.239, 84.5841, 44.4283, 109.868, 408.63, 15.207, 
                                           56.5922, 620.958, 40.0063, 68.8716], name="Export Goods"),
              1, 1)
fig.add_trace(go.Pie(labels=labels, values=[59.568, 76.7594, 92.8984, 277.214, 93.2468, 133.451, 146.459, 
                                            59.6964, 32.6644, 76.6006, 287.879, 13.0894, 51.3237, 625.496, 
                                            35.2258, 33.8145], name="Export Goods"),
              1, 2)

# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+value+name",textinfo='value')

fig.update_layout(
    title_text="Comparison of Goods Exported by Countries in Q2 2019 and Q2 2020(Million US Dollars)",
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="green",
    title_x=0.5,
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='Q2 2019', x=0.16, y=0.5, font_size=20, showarrow=False),
                 dict(text='Q2 2020', x=0.84, y=0.5, font_size=20, showarrow=False)])
fig.show()


# In[10]:


fig = px.scatter_geo(df2, locations="LOCATION", color="LOCATION",
                     hover_name="LOCATION", size="Value",
                     animation_frame="TIME",
                     projection="natural earth")
fig.update_layout(
    title_text="GDP change of world countries between 2017-2020(Million US Dollars)",
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="green",
    title_x=0.5,)
fig.show()


# In[11]:


fig = px.scatter_matrix(df, dimensions=["Import_Value", "Export_Value","TIME"], color="LOCATION")
fig.update_layout(
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="green",
    title_x=0.5,
    title_text="Comparison of Goods Exported and Imported(Million US Dollars)")
fig.show()


# In[12]:


df3.head()


# In[13]:


fig = px.scatter_matrix(df3, dimensions=["Import_Value", "Export_Value","TIME"], color="LOCATION")
fig.update_layout(
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="green",
    title_x=0.5,
    title_text="Comparison of Services Exported and Imported(Million US Dollars)")
fig.show()


# In[ ]:





# In[ ]:




