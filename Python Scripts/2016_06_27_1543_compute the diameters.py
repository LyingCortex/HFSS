# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:42:49 2016

@author: LY
"""



import math
er = 4.5
er_air = 1
N = 4
delta_1 = (er - er_air)/(N+1)
er_array = [er-delta_1*(i+1) for i in range(N)]


Lr = 3
r = [((er-i)/(er-1)/math.pi)**0.5 * Lr  for i in er_array]

d = [ rr * 2 for rr in r]
circle_area = [math.pi * rr ** 2 for rr in r]