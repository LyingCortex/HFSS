# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:49:19 2016

@author: levi
"""
import math
###
# redesign 2.63:1
Z0 = 76.4
Z00 = 70

Z01 = (Z00*Z0)**0.5
r1 = 10**(2.688/10)
Z1 = Z00 * r1


Z1_0 = Z1 * Z00/(Z1 + Z00)
Z10 = (Z1_0 * Z0) ** 0.5



print('Z1 = ' + str(Z1))
print('Z01 = ' + str(Z01))
print('Z10 = ' + str(Z10))

print('Z1//Z0 = ' + str(Z1_0))
Z20 = 95.05
print('Z20 = ' + str(Z20))
Z2 = Z20**2 / Z1
print('Z2 = ' + str(Z2))


Z40 =(Z0*Z2)**0.5

print('Z40 = ' + str(Z40))