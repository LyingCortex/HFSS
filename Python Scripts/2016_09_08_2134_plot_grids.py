# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:32:15 2016

@author: LY
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:20:02 2016

@author: LY
"""



import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os, re


####################################################################################   
####################################################################################
####################################################################################   
####################################################################################
####################################################################################   
####################################################################################
####################################################################################   
####################################################################################
f0 = 13.5
D = 321.9
f = D * 0.95   # 
Lambda = 300 / f0
k0 = 2*math.pi/Lambda
theta0 = 0/180*math.pi  # deg
phi0 = 0/180*math.pi    

p = 11.1

###=================================================================================
path = r'D:\Users\LY\Documents\Ansoft\MyDesigns\Transmitarray\201608\0828'

file_name1 = r'TxA_0829_phase.csv'
file_name2 = r'TxA_0829_dB.csv'

file_path1 = path + '\\'+ file_name1
file_path2 = path +  '\\'+file_name2

f1 = open(file_path1, 'r')
col1 = []        # store the phase 
colr = []        #
col1_deg = []    # change the radian angle to degree
dict_r_ang = {}  # r and angle pairs
for line in f1.readlines():
    line = line.replace('\n',' ').split(',')
    col1.append(line[1])
    colr.append(line[0])

f1.close()
    
colr = [eval(i) for i in colr[1:-1]]
col1 = [eval(i)/180*math.pi for i in col1[1:-1]]
col1_deg = [i%(2*math.pi) /math.pi *180   for i in col1]

for i in range(len(col1)):
    dict_r_ang[col1_deg[i]] = colr[i]
    
########################################################################################
###============================================================
'''
find the key of the dictionary that nearest the real value

input:
output:  index present the position of the value in the list of angle_list

'''
def find_the_most_similar_angle(v_real, angle):
    
    dist = 361
    index = 0
    for i in range(len(angle)):
        disti = abs(angle[i] - v_real)
        if disti < dist:
            dist = disti
            index = i
    return index
            
###================================================================  

####=====================================================================================
####============================================
x0 = 0
y0 = 0
z0 = 0

xf=0
yf=0
zf= f
pf = (xf, yf, zf)
p0 = (x0, y0, z0)
# N = D/p
N=29  # N is odd
N1 = (N+1)//2
N2 = (N-1)//2

v_part = {}  # point and value

P1_angle = [[0 for j in range(N)] for i in range(N)]  # angle
P2 = [[0 for j in range(N)] for i in range(N)]     #  r
P3 = [[] for i in range(N)]    #  real position



for m in range(0,N1):
    for n in range(m+1):
        p_i = (p0[0]+m*p, p0[1]+n*p, p0[2])
        d_i = ( (p0[0] + m*p-pf[0])**2 + (p0[1]+ n*p -pf[1])**2 + (p0[2] - pf[2])**2)**0.5
        phi_i = k0 * (d_i - math.sin(theta0)*(p_i[0]*math.cos(phi0) + p_i[1]*math.sin(phi0)))
        phi_i_360 =  (phi_i % (2*math.pi))/math.pi*180
        v_part[m**2 + n **2] = phi_i_360     # it's handable if the dictionary is used
        
for i in range(N):
    for j in range(N):
        P1_angle[i][j] = v_part[(N2-i)**2 +(N2-j)**2] if ((N2-i)**2 + (N2-j)**2) in v_part.keys() else 180
        index1 = find_the_most_similar_angle(P1_angle[i][j], col1_deg)
        P2[i][j] = dict_r_ang[col1_deg[index1]]    # store the radius
        P3[i].append(((i-N2)*p, (j-N2)*p, 0))      # real position

XX = P1_angle

fig, ax = plt.subplots()
i = ax.imshow(XX, cmap=cm.jet, interpolation='nearest')
fig.colorbar(i)
plt.show()
fig.savefig('ta_4.png',dpi=500)
##################################################################################

'''    
## plot image of the phase distribution   
XX = P1_angle

fig, ax = plt.subplots()
i = ax.imshow(XX, cmap=cm.jet, interpolation='nearest')
fig.colorbar(i)

plt.show()
'''
#########################################################################################
#w  = 0.4
#T = 0.5 
#for i in range(N):
#    for j in range(N):
#        center=P3[i][j]
#        L1 = P2[i][j]
#        S = 0.22 * L1
#        L2= L1 - S *2 - w*2
#        L11 = L1 -w *2
#        L22 = L2 - w*2
#        
#        
        
      
        
        
#        # add some judge
#        xmax = abs(center[0]) + L1/2
#        ymax = abs(center[1]) + L1/2
#        if (xmax ** 2 + ymax ** 2 )**0.5 <= D/2:
            

















