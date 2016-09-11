# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:37:56 2016

@author: LY
"""
#import math
#import os
import numpy as np
import matplotlib.pyplot as plt
import cmath


path = r'D:\Users\LY\Documents\Python Scripts\Data'

file_name1 = r'data_0829_S21_vers_freq_4_layers_H+T.txt'

file_path1 = path + '\\'+ file_name1


f1 = open(file_path1, 'r')
col_13_5 = []
col_13 = []
col_14 = []
phase_col_13_5 = []
phase_col_13 = []
phase_col_14 = []

for line in f1.readlines():
    if '\t' in line:
        line = line.replace('\n','').replace('\t', ' ').split(' ')    
    
        #print(line[0])
    
        if eval(line[0]) == 13:
            col_13.append(20*np.log10(np.sqrt(eval(line[1]) ** 2 + eval(line[2]) **2)))
            phase_col_13.append(cmath.phase(complex(eval(line[1]),eval(line[2])))/np.pi*180  % 360)
        elif eval(line[0]) == 13.5:
            col_13_5.append(20*np.log10(np.sqrt(eval(line[1]) ** 2 + eval(line[2]) **2)))
            phase_col_13_5.append(cmath.phase(complex(eval(line[1]),eval(line[2])))/np.pi*180 % 360)
        elif eval(line[0]) == 14:
            col_14.append(20*np.log10(np.sqrt(eval(line[1]) ** 2 + eval(line[2]) **2)))
            phase_col_14.append(cmath.phase(complex(eval(line[1]),eval(line[2])))/np.pi*180 % 360)


col_x = np.arange(7, 10.7, 0.2)


f1.close()

fig = plt.figure(1)
plt.axis([7, 11,-30, 5 ])
plt.plot(col_x, col_13,'*')
plt.plot(col_x, col_13_5,'ro')
plt.plot(col_x, col_14,'k+')

plt.show()
fig.set_size_inches(8, 6)
fig.savefig('S21_vers_L1.png', dpi=200)


fig_phase = plt.figure(2)
plt.plot(col_x, phase_col_13,'b')
plt.plot(col_x, phase_col_13_5,'r')
plt.plot(col_x, phase_col_14,'k')
plt.show()
fig_phase.savefig('S21_Phase_vers_L1.png', dpi=200)