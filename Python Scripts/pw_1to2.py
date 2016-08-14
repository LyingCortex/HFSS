# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 17:21:45 2016

@author: levi
"""

wl = 12.5
er = 3.66
wl_g = wl /er**0.5


z0 = 76.4
k_2 = 2.5

z1 = 93.6 ** 2 / z0
z2 = z1 / k_2
z2x = (z2*z0)**0.5

z12 = z1 * z2 /(z1+z2)

z0x = (z12 * z0) **0.5
print('===============================')
print('Z1 = ' + str(z1))
print('Z2 = ' + str(z2))
print('Z_2x = ' + str(z2x))
print('Z_0x = ' + str(z0x))
print('===============================')


#p2_db = -1.6016
#p3_db = -6.3331
#
#p2 = 10 **(p2_db/10)
#p3 = 10 **(p3_db/10)
#
#print('p2 = ' + str(p2))
#print('p3 = ' + str(p3))
#print('p2:p3 = 1 : ' + str(p2/p3))