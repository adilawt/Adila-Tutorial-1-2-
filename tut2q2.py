# Tutorial2 Question2a: Integration of cos(x) for 0 to pi/2 for range # of points using the simple mothod, include 10,30,100,300,1000 points between 0 and pi/2
import numpy as np 
x0 = 0
ul = np.pi/2 # ul is the upper limit 
delta = [(ul-x0)/10,(ul-x0)/30,(ul-x0)/100,(ul-x0)/300,(ul-x0)/1000]   # this is delta 
for dx in delta:
     x = np.arange(x0,ul,dx)
     y = np.cos(x)
     total = y.sum()*dx  
     print 'integral is ' + repr(total) + ' with dx=' + repr(dx) 
# Question2b: How does error scale with of point?
# One can see from the result of the integration for different spacing that the result gets closer to exact value as the number of spacing increases. Therefore, the error scale decreases as the number of points of equally spacing increases.  
