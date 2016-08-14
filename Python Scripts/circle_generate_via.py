# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:49:15 2016

@author: LY
"""

import math
import numpy as np



f = 24.15  # GHz
wave_length = 300.0 / f  # lambda
p = 1 # mm  spacing
opt_n = 0.3    # the varible used to optmize the structure
extend_r  = opt_n * wave_length
print('==========================================')
print ('r: ', extend_r)

print('==========================================')

num_v =round(math.pi / theta_v)

print('numbers of circular vias : ' + str(num_v))

print('==========================================')
theta_array = np.linspace(0, math.pi, num_v)
print ('theta_array:\n' , theta_array)

print('==========================================')
pos = [(extend_r * math.sin(t), -(extend_r - extend_r * math.cos(t)) ) for t in theta_array]

print('pos:\n', pos)

print('==========================================')
