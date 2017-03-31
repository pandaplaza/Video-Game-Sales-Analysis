# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:11:37 2017

@author: troy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
plt.style.use('ggplot')

#List of videogame sales with games with sales greater than 100,000. 
#Downloaded from Kaggle.com. Treats missing values(set to N/A) as missing.
vgsales = pd.read_csv('C:\\Users\\troy\\Desktop\\Datasets\\vgsales.csv', 
                      na_values = ['N/A'])

#Cleaning data so that first column is rank
vgsales.set_index('Rank', inplace = True)

#Info about each variable
vgsales.info

#Basic summary statistics, excluding year as it doesn't give much information.
#The sales should be read in millions. This doesn't provide too much info.
vgsales_noyr = vgsales.drop(['Year'], axis=1)
vgsales_noyr.describe()

#Prints mean of numerical data, sales are in millions. 
vgsales.mean(axis=0)

na_salesYr = pd.crosstab(vgsales.Year, vgsales.NA_Sales)

#Plotting
#vgsales.plot(x='Year', y='NA_Sales', kind='hist')
na_salesYrTotal = na_salesYr.sum(axis=1)
plt.figure(figsize=(8,6))
sb.barplot(y = na_salesYrTotal.index, x = na_salesYrTotal.values, orient = 'h')
sb.plt.ylabel="Year"
sb.plt.xlabel="Total NA_Sales in Millions"



