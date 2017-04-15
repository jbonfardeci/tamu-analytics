# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:59:38 2017

@author: horvitz-a
"""
import pylab
import random

#Randomly generate a normal distribution with mean = 0 and SD = 30.  
#Use 10000 values.

dist = []
for i in range (10000):
    dist.append(random.gauss(0,30))
    
#Plot the histogram in 30 bins

pylab.hist(dist,30)


