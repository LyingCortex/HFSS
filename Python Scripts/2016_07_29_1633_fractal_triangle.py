# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:33:12 2016

@author: levi
"""

import math

import numpy as np
import matplotlib.pyplot as plt

a1 = (1,0)
a2 = (2,1)
a3 = (1,2)
A = [a1, a2, a3, a1]
x = [a for (a,b) in A]
y = [b for (a,b) in A]

plt.plot(x,y)


N = 2
while(N):
    New = []
    for i in range(len(A)-1):
        New.append(A[i])    
        a11 = A[i][0] + 1/3*abs((A[i+1][0]-A[i][0]))
        b11 = A[i][1] + 1/3*abs((A[i+1][1]-A[i][1]))
        New.append((a11, b11))
    print(New)    
    N= N-1