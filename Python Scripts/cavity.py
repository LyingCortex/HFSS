# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:02:15 2016

@author: LY
"""

import math

f = 25
er = 2.2 
lambda_0 = 300.0 / f
lambda_g = lambda_0 / er**0.5

wp1 = 16.8
wp2 = 12
l1 = 3.5
l2 = 2.4

list_1 = [wp1, wp2, l1, l2]
list_2 = [ x/lambda_g for x in list_1]



lambda_g_new = 20 /2.2**0.5

list_3 = [x * lambda_g_new for x in list_2]

list_4 = [ round(x) for x in list_3]

p =1.2

wp1 = list_4[0]
wp2 = list_4[1]
l1 = list_4[2]
l2 = list_4[3]

N1 = round(wp1/p)


#row_bottom = [('wp1/2', 'l1/3*'+str(i), 0)  for i in range(3)]
#row_bottom_1 = [('-wp1/2', 'l1/3*'+str(i), 0)  for i in range(3)]
#column_1 = [('wp1/2 - (wp1-wp2)/4 *'+str(i), 'l1', 0) for i in range(1,3)]
#column_1_1 = [('-wp1/2 + (wp1-wp2)/4 *'+str(i), 'l1', 0) for i in range(1,3)]
#row_second = [('wp2/2', 'l1+l2/3*'+str(i), 0 ) for i in range(1, 3)]
#row_second_1 = [('-wp2/2', 'l1+l2/3*'+str(i), 0 ) for i in range(1, 3)]
#column_2 = [('wp2/2-(wp2-a)/4*'+ str(i), 'l1+l2', 0) for i in range(1, 3)]
#column = [('-wp1/2+ wp1/14*'+str(i), 0,0) for i  in range(1,15)]

list1 = [('wp1/2', 'l1/3*'+str(i), 0)  for i in range(3)]
list8 = [('-wp1/2', 'l1/3*'+str(i), 0)  for i in range(3)]
list2 = [('wp1/2 - (wp1-wp2)/4 *'+str(i), 'l1', 0) for i in range(1,3)]
list7 = [('-wp1/2 + (wp1-wp2)/4 *'+str(i), 'l1', 0) for i in range(1,3)]
list3 = [('wp2/2', 'l1+l2/3*'+str(i), 0 ) for i in range(1, 3)]
list6 = [('-wp2/2', 'l1+l2/3*'+str(i), 0 ) for i in range(1, 3)]
list4 = [('wp2/2-(wp2-a)/4*'+ str(i), 'l1+l2', 0) for i in range(1, 3)]
list5 = [('-wp2/2+(wp2-a)/4*'+ str(i), 'l1+l2', 0) for i in range(1, 3)]
list9 = [('-wp1/2+ wp1/14*'+str(i), 0,0) for i  in range(1,15)]
list_total = []
list_name = []
for i in range(1,10):
    
    #list_total.extend(locals()['list{}'.format(i)])
    list_total.extend(locals()['list'+str(i)])