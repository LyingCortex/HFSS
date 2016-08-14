# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:09:19 2016

@author: levi
"""

print('=================================')
O2_ang = 160.32+133.81-159.428
O2_dB = -6.1123-0.4225-0.323

print('O2 ang = ' +str(O2_ang))
print('O2 dB = ' +str(O2_dB))
print('=================================')
O6_ang = -168.44-75.58-161.688
O6_dB = -2.4326-1.0081-0.836
print('O6 ang = ' +str(O6_ang))
print('O6 dB = ' +str(O6_dB))
print('=================================')
O4_ang = -65.03-28.23-132.221
O4_dB = -1.4537-0.6472-0.541

print('O4 ang = ' +str(O4_ang))
print('O4 dB = ' +str(O4_dB))
print('=================================')
O8_ang = 64.88+86.58+165.457
O8_dB = -12.0738-1.3665-1.116
-405.7
print('O8 ang = ' +str(O8_ang))
print('O8 dB = ' +str(O8_dB))
print('=================================')

db_s = [ O4_dB, O6_dB, O2_dB, O8_dB]

real_s = [10**(db/10) for db in db_s]

print ('power ratio = ' + str(1) + ':' + str(round(real_s[1]/real_s[0],2))+ ':' + str(round(real_s[2]/real_s[0], 2))+ ':' + str(round(real_s[3]/real_s[0],2)))
