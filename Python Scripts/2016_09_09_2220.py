# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 22:19:44 2016

@author: LY
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0., np.e, 0.01)
y1 = np.exp(-x)
y2 = np.log(x)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x, y1,'r',label="right");
ax1.legend(loc=1)
ax1.set_ylabel('Y values for exp(-x)');
ax2 = ax1.twinx() # this is the important function
ax2.plot(x, y2, 'g',label = "left")
ax2.legend(loc=2)
ax2.set_xlim([0, np.e]);
ax2.set_ylabel('Y values for ln(x)');
ax2.set_xlabel('Same X for both exp(-x) and ln(x)');
plt.show()
