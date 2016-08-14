# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 15:23:14 2016

@author: levi
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 20:54:15 2016

@author: LY
"""


import math
import numpy as np
import matplotlib.pyplot  as plt

import os, re





plt.figure(2)
theta = np.arange(0, 2*np.pi, 0.02)
#plt.subplot(polar= True)
plt.polar(theta, np.ones_like(theta), lw=2)
line2, = plt.polar(theta, np.cos(theta), '--' , lw=2, label = 'theorical')



plt.rgrids(np.arange(0.2,1,0.2),angle =130)
plt.thetagrids(np.linspace(0,330, 12))
plt.legend(handles = [line2],loc =4)
#plt.title('hi')
plt.show()


