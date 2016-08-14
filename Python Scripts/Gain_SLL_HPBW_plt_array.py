# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import matplotlib.pyplot as plt

length = np.arange(5.8, 19.8, 2)
rectangle_gain = np.array([10, 10.5, 11.5, 11.7, 12.3, 12, 11.9])
rectangle_bw_e = np.array([83.8, 67.2, 57, 51.2, 44.8, 41, 37.6])
rectangle_bw_h = np.array([43.2, 40.6, 39.8, 35.4, 34, 31.2, 29.8])
rectangle_sll_e = np.array([-12.9, -8.8, -8.1, -7.4, -7.2, -6.5, -5.9])
rectangle_sll_h = np.array([-18.1, -14.3, -17.4, -15.5, -17.6, -17, -15.9])



ellipse_gain = np.array([9.2, 9.8, 10.7, 10.8, 11.5, 11.2, 11.3])
ellipse_bw_e = np.array([78, 62, 57.2, 49.6, 46, 42.2, 38.8])
ellipse_bw_h = np.array([50, 46.2, 44.8, 41.8, 38.8, 37, 34.4])
ellipse_sll_e = np.array([-10.5, -9.1, -9, -8, -8.5, -7.4, -7.3])
ellipse_sll_h = np.array([-16.1, -11.7, -13.4, -13.7, -13.4, -11.4, -10.1])

plt.plot(length, rectangle_gain, label='Rect_Gain', linewidth = 2)
plt.plot(length, ellipse_gain, color = 'red',label = 'Ellipse_Gain', linewidth = 2)
plt.xlabel('Length ($mm$)')
plt.ylabel('Gain ($dB$)')
plt.title('Gain viaries with slab length')
plt.legend()
plt.grid()
plt.show()


plt.plot(length, rectangle_bw_e, label='Rect_Beamwidth_E', linewidth = 2)
plt.plot(length, ellipse_bw_e, label='Ellipse_Beamwidth_E',color = 'red', linewidth = 2)
plt.xlabel('Length ($mm$)')
plt.ylabel('Beamwidth in E plane ($degree$)')
plt.title('E plane beamwidth viaries with slab length')
plt.legend()
plt.grid()
plt.show()


plt.plot(length, rectangle_bw_h, label='Rect_Beamwidth_H', linewidth = 2)
plt.plot(length, ellipse_bw_h, label='Ellipse_Beamwidth_H',color = 'red', linewidth = 2)
plt.xlabel('Length ($mm$)')
plt.ylabel('Beamwidth in H plane ($degree$)')
plt.title('H plane beamwidth viaries with slab length')
plt.legend()
plt.grid()
plt.show()

plt.plot(length, rectangle_sll_e, label='Rect_SLL_E', linewidth = 2)
plt.plot(length, ellipse_sll_e, label='Ellipse_SLL_E', linewidth = 2,color = 'red')
plt.xlabel('Length ($mm$)')
plt.ylabel('SLL in E plane ($dB$)')
plt.title('E plane SLL viaries with slab length')
plt.legend()
plt.grid()
plt.show()

plt.plot(length, rectangle_sll_h, label='Rect_SLL_H', linewidth = 2)
plt.plot(length, ellipse_sll_h, label='Ellipse_SLL_H', linewidth = 2,color = 'red')
plt.xlabel('Length ($mm$)')
plt.ylabel('SLL in H plane ($dB$)')
plt.title('H plane SLL viaries with slab length')
plt.legend()
plt.grid()
plt.show()