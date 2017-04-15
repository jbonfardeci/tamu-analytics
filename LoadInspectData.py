# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 13:23:39 2017

@author: horvitz-a

Here is the code to load the Hall of Fame data and visually inspect it.
The file path is under fileLocation. Therefore it can be substituted for any CSV data set. 
It gives you the first five rows, last five rows and a brief description of the data in in each column.


"""

import pandas as pd  #import pandas module

fileLocation = ('C:/Data/hof_data.csv')         #Link the file location to 'fileLocation'

df = pd.read_csv(fileLocation)                  #Read the file into a dataframe

print()
print('------------------------------------')
print('The first five rows in the data are: ')
print('------------------------------------')
print()
print(df.head())                                #Inspect the first five rows
print()
print('----------------------------------')
print('The last five rows in the data are: ')
print('----------------------------------')
print()
print(df.tail())                                   #Inspect the last five rows
print()
print('-------------------------------------------------')
print('Here is a description of the data in each column:')
print('-------------------------------------------------')
print()
print(df.describe())                              #Describe each column in the data
print()
print('-----------------------------------')
print('Here is a list of the column names:')
print('-----------------------------------')
print()
print(df.columns)                               #List the column names
print()
print('----------------------------------')
print('Here is a shape of the data frame:')
print('(Rows, Columns)')
print(df.shape)                                 #List the shape of the data
print('----------------------------------')
print()
