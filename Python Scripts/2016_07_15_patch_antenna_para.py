# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:10:13 2016

@author: levi
"""

import math


 
 
#f = 24
#er = 3.66
#H = 0.254
#
#W = 300.0 / 2 /f *(2.0/(er+1))**0.5
#eeff = (er+1)/2+(er-1)/2*(1+12*H/W)**(-0.5)
#delta_L= H * 0.412*(eeff+0.3)*(W/H+0.264)/(eeff-0.258)/(W/H+0.8)
#L = 300/(2*f*eeff**0.5)-2*delta_L
#
#
#W0 =0.254
#Zc = 60.0/eeff**0.5*math.log(8*H/W0+W0/4/H)

''' 
f = 10.05
er = 2.47
H = 1.43
t = 0.035
W =8
eeff = (er+1)/2+(er-1)/2*(1+10*H/W)**(-0.5)-(er-1)/4.6*t/H/(W/H)**0.5
delta_L= H * 0.412*(eeff+0.3)*(W/H+0.264)/(eeff-0.258)/(W/H+0.8)
L = 300/(2*f*eeff**0.5)-2*delta_L


W0 =1
Zc = 60.0/eeff**0.5*math.log(8*H/W0+W0/4/H)
'''
f = 24
er = 3.66
H = 0.254
t = 0.018
W = 300.0 / 2 /f *(2.0/(er+1))**0.5
eeff = (er+1)/2+(er-1)/2*(1+10*H/W)**(-0.5)-(er-1)/4.6*t/H/(W/H)**0.5
delta_L= H * 0.412*(eeff+0.3)*(W/H+0.264)/(eeff-0.258)/(W/H+0.8)
L = 300/(2*f*eeff**0.5)-2*delta_L


W0 =0.254
Zc = 60.0/eeff**0.5*math.log(8*H/W0+W0/4/H)