#Assignment 2

#Kittipong Wangnok, D6010218
#School of Physics, Institute of Science, Suranaree University of Technology

#Find the root of the equation f(x) = cosx-x by the method of bisection.
#How many iterate are necessary to determine the root to 8 significant figures?
#The solution of this problem is at below.

import sys
import numpy as np

#Define funtion for finding root
def f(E):
    f = E - e*np.cos(E) - M
    return f

#define parameters
sr = 1*10**(-8)
a = 0.0
b = 2.0
c = (a+b)/2
d = b-a
n = 1
e = 0.5
M = 0.075

while d >= sr:
    c = (a+b)/2.0   
    if (f(b)*f(c)) <= 0:
        a = c
    else:       
        b = c
        c = (a+b)/2.0
    d = (b-a)/b
    n += 1          

print ('1. Bisection metod')
print ('____________________________________________________________________')
print ('The root of the equation f(x)=cos(x)-x is',c)
print ('Approximate Relative Error is equal to',d)
print ('The number of iterateration is',n)
print ('____________________________________________________________________')

