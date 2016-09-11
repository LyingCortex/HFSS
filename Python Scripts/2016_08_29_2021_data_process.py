# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 20:17:19 2016

@author: LY
"""

#with open('abc.txt') as input_data:
#    for line in input_data:
#        tmpline = line.split()
#        if tmpline!=[]:
#            try:
#                if float(tmpline[0])==13 or float(tmpline[0])==13.5 or float(tmpline[0])==14:
#                    print [ float(x) for x in tmpline]
#            except ValueError:
#                continue

import numpy as np
import matplotlib.pyplot as plt
import cmath


path = r'D:\Users\LY\Documents\Python Scripts\Data'

file_name1 = r'data_0829_S21_vers_freq.txt'

file_path1 = path + '\\'+ file_name1




col_13 = []


with open(file_path1) as input_data:
    for line in input_data:
        tmpline = line.replace('\n','').replace('\t', ' ').split(' ')  
        
        if tmpline != []:
            
            try:
                if float(tmpline[0])==13.0:                  
                    col_13.append(20*np.log10(np.sqrt(eval(tmpline[1]) ** 2 + eval(tmpline[2]) **2)))
            except ValueError:
                continue



col_x = np.arange(7, 10.7, 0.2)



fig = plt.figure(1)
plt.plot(col_x, col_13,'*')
plt.show()



