# -*- coding: utf-8 -*-
#Solution for Question 3
"""
Question 1:
The random variable X and Y have the following joint probability density 
𝑓𝑋𝑌(𝑥,𝑦)={𝑒^(−𝑥−𝑦) 0<𝑥<∞,0<𝑦<∞0 
          0 𝑒𝑙𝑠𝑒𝑤ℎ𝑒𝑟𝑒
What is 𝑃(𝑋<𝑌) ?
"""

import scipy as sp
import numpy as np
from scipy import integrate

f = lambda y, x: np.exp(-x-y)

"""
Here we need to do double integration of the joint probability density function given.
Since we want P(X<Y) then we have to integrate from the point where y>x 
which is the straight line y=x. 
The inner integral must go from x to infinity as range of x is from 0 to infinity.
The outer integral is from 0 to infinity as the range of y is from 0 to infinity.
"""

result = integrate.dblquad(f, 0, np.inf, lambda x:x, lambda x:np.inf)

print(result)

print('P(X<Y) is %.2f'%(result[0]))




