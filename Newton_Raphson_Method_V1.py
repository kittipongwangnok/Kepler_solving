#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:51:53 2020

@author: kittipongwangnok
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:42:05 2020

@author: kittipongwangnok
"""

# Reference website: https://www.geeksforgeeks.org/program-for-newton-raphson-method/
# Python3 code for implementation of Newton 
# Raphson Method for solving equations 
  
import numpy as np

  
# The function is f(E) = E - e*sin(E) - M
def f( E ): 
    return E - e*np.sin(E) - M
  
# Derivative of the above function  
# which is f'(E) = 1 -e*cos(E)
def df( E ): 
    return 1 - e*np.cos(E)

#Assume the initial values 
epsilon = 1*10**(-4) 
e = 0.39
M = 0.0017083707339714137       #deg
#M = 2.981666079679945e-05      #rad
E0 = 0.0005

print ('----------------------------------------------------------------------')
print ('The Eccentric anomaly calculation using the Newton Raphson Method')
#print ('The initial parameters')
print ('----------------------------------------------------------------------')
print ('Mean anomoly (M):', '%.5f'% M)     
print ('Eccentricity (e):', '%.5f'% e)
#print ('The initial value of the eccentric anomaly:', E0)  
#print ('-------------------------------------------------')
#print ('The final parameter')
#print ('-------------------------------------------------')

# Function to find the root: The eccentric anomoly
def NewtonRaphson( E ): 
    h = f(E) / df(E) 
    while abs(h) >= epsilon: 
        h = f(E)/df(E)           
        # x(i+1) = x(i) - f(x) / f'(x) 
        E = E - h 
      
    print('Eccentric anomaly (E):','%.5f'% E) 
  
NewtonRaphson(E0) 
print ('----------------------------------------------------------------------')
print ('Congratulations!!!')
print ('Next, you can calculate the true anomaly.')
print ('----------------------------------------------------------------------')
  
# This code is contributed by "Kittipong Wangnok" 
