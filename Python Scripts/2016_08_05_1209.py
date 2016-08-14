# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 12:06:14 2016

@author: levi
"""
import math

Z0 = 76.4
Z00 = 45

Z01 = (Z00*Z0)**0.5
r1 = 12.06
Z1 = Z00 * r1


Z1_0 = Z1 * Z00/(Z1 + Z00)
Z10 = (Z1_0 * Z0) ** 0.5



print('Z1 = ' + str(Z1))
print('Z10 = ' + str(Z10))

print('Z1//Z0 = ' + str(Z1_0))
Z20 = 95.05
print('Z20 = ' + str(Z20))
Z2 = Z20**2 / Z1
print('Z2 = ' + str(Z2))

Z30 =44
print('Z30 = ' + str(Z30))
Z3 = Z30**2 / Z2
print('Z3 = ' + str(Z3))
Z40 =(Z0*Z3)**0.5

print('Z40 = ' + str(Z40))

