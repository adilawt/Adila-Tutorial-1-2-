# Tutorial2 Question3a: Python supports array slicing x[5:10:2] will take points 5,7,9 from x. x[5::2] will take points 5,7,9... 
import numpy as np
x = np.arange(1,20)
for even in x:
    if even%2==0:
       print even + 2, 'is even number'
       if even == len(x)-5:
          break      
