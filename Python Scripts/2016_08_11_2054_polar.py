# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 20:54:15 2016

@author: LY
"""


import math
import numpy as np
import matplotlib.pyplot  as plt

import os, re










path = r'D:\Users\LY\Documents\Ansoft\MyDesigns\Transmitarray\201608\0808'

file_name1 = r'ang_slot_cross.csv'
file_name2 = r'dB_slot_cross.csv'

file_path1 = path + '\\'+ file_name1
file_path2 = path +  '\\'+file_name2

f1 = open(file_path1, 'r')
col1 = []
for line in f1.readlines():
    line = line.replace('\n',' ').split(',')
    col1.append(line[1])
col1 =[eval(i)/180*np.pi for i in col1[1:-1]]

f2 = open(file_path2, 'r')
col2 = []
for line in f2.readlines():
    line = line.replace('\n',' ').split(',')
    col2.append(line[1])
col2 =[10**(eval(i)/20) for i in  col2[1:-1]]




plt.figure(2)
theta = np.arange(0, 2*np.pi, 0.02)
#plt.subplot(polar= True)
plt.polar(theta, np.ones_like(theta), lw=2)
line2, = plt.polar(theta, np.cos(theta), '--' , lw=2, label = 'theorical')
line3, = plt.polar(col1, col2, 'o', label = 'cross slot')

plt.rgrids(np.arange(0.2,1,0.2),angle =130)
plt.thetagrids(np.linspace(0,330, 12))
plt.legend(handles = [line2, line3],loc =4)
#plt.title('hi')
plt.show()


###########################
#er = 2.5
#gammar = (1-er**0.5)/(1+er**0.5)
#beta_Ld = [0, 45, 90, 135, 180]
#S12 = (1-gammar**2)*


