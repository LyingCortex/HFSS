# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:37:24 2016

@author: LY
"""

import numpy as np
import matplotlib.pyplot as plt

theta1 = [1,2,3,4,5,6,7,8,9,10,12,14,16]
gain1 = [ 10.18, 10.04, 10, 9.98, 10.02, 9.89, 10.0, 10.04, 9.9 ,9.95,9.81,7.44, 6.64]

ff = plt.figure(1)
plt.plot(theta1, gain1)
plt.xlabel('theta')
plt.ylabel('Gain')
plt.grid()
ff.savefig('2_4_gain.png', dpi=200)
