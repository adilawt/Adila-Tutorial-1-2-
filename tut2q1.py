# Tutorial1 Question1: Write a python script to make a vector of n evenly spaced numbers between 0 and pi/2 i.e. x[0]=0, x[n-1]= pi/2 
# This is a program for equaly spanced vectors
import numpy as np
n= 100
x = np.linspace(0,np.pi/2,n) 
print 'x gives', n, 'spaced vector'

