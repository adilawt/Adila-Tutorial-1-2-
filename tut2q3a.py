# Tutorial2 Question3a: Python supports array slicing x[5:10:2] will take points 5,7,9 from x. x[5::2] will take points 5,7,9.... from x. How can I take all odd pints from an array?
import numpy as np
x = np.aragne(1,20)
for odd in x:
    if odd%2==1:
       print odd, 'is odd number'

