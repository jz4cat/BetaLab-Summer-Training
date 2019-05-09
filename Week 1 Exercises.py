# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:34:07 2019

@author: Jen
"""

#Question 4
import math
d = 9.7
r = d/2
area = math.pi*r**2
print("Area of a circle: " + str(area))

#Question 20
mean_return = float(input("What is the portfolio mean return: "))
risk_free = float(input("What is the mean risk-free rate: "))
standard_deviation = float(input("What is the total risk of the investment: "))
sharpe_ratio = (mean_return-risk_free)/standard_deviation
print(sharpe_ratio)