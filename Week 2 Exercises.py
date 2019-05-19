# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Question 8
from scipy.stats import skew
print(skew([1,2,3,4,1000]))


#Question 10
import scipy as sp
ret = sp.array([0.05,0.11,-0.03])
print(pow(sp.prod(ret+1),1/len(ret))-1)


#Question 11
import scipy as sp
ret = sp.array([0.05,0.11,-0.03])
#Arithmetric mean of returns
arith_mean = sp.mean(ret)
#geometric mean
geo_mean = pow(sp.prod(ret+1),1/len(ret))-1
print(arith_mean)
print(geo_mean)