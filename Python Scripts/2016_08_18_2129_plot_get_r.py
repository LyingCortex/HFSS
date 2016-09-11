# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 21:29:11 2016

@author: LY
"""



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#import os, re

########
path = r'D:\Users\LY\Documents\Ansoft\MyDesigns\Transmitarray\201608\0817'

file_name1 = r'r_and_phase-819.csv'
file_name2 = r'r_and_dB-819.csv'

file_path1 = path + '\\'+ file_name1
file_path2 = path +  '\\'+file_name2

f1 = open(file_path1, 'r')
col1 = []
colr = []
col1_deg = []
dict_r_ang = {}
for line in f1.readlines():
    line = line.replace('\n',' ').split(',')
    col1.append(line[1])
    colr.append(line[0])
colr = [eval(i) for i in colr[1:-1]]
col1 =[eval(i)/180*np.pi for i in col1[1:-1]]
col1_deg = [i%(2*np.pi) /np.pi *180   for i in col1]

for i in range(len(col1)):
    dict_r_ang[col1_deg[i]]=colr[i]


f2 = open(file_path2, 'r')
col2 = []
for line in f2.readlines():
    line = line.replace('\n',' ').split(',')
    col2.append(line[1])
col2 =[10**(eval(i)/20) for i in  col2[1:-1]]

f1.close()
f2.close()


###########################

theta = np.linspace(0, 2*np.pi,0.02)
plt.polar(theta, np.ones_like(theta), lw = 2)
plt.polar(col1, col2, 'ro')



plt.rgrids(np.arange(0.2,1,0.2),angle =130)
plt.thetagrids(np.linspace(0,330, 12))

plt.show()

########################################




D = 149.3
f = D *0.8

x0 = 0
y0 = 0
z0 = 0

xf=0
yf=0
zf= f
pf = (xf, yf, zf)
p0 = (x0, y0, z0)



theta0 = 0/180*np.pi  # deg
phi0 = 0/180*np.pi
f0  = 13.58
lambda0 = 300/f0
k0 = 2*np.pi/lambda0

d0 =  ( (p0[0] -pf[0])**2 + (p0[1] -pf[1])**2 + (p0[2] - pf[2])**2)**0.5

p = 11.5  #mm

p_part = []
p_part.append(p0)
v_part = {}  # point and value


N=13
Points = np.zeros((N,N))

#mp = [[(x0+m*p, y0+ n*p, z0),((x0+m*p-xf)**2 + (y0+ n*p -yf)**2 + (z0 -zf)**2)**0.5]  for m in range(1, 7) for n in range(m+1)]
for m in range(0,7):
    for n in range(m+1):
        p_i = (p0[0]+m*p, p0[1]+n*p, p0[2])
        d_i = ( (p0[0] + m*p-pf[0])**2 + (p0[1]+ n*p -pf[1])**2 + (p0[2] - pf[2])**2)**0.5
        phi_i = k0 * (d_i - np.sin(theta0)*(p_i[0]*np.cos(phi0) + p_i[1]*np.sin(phi0)))
        phi_i_360 =  (phi_i % (2*np.pi))/np.pi*180
        p_part.append(p_i)
        #print(m**2 + n**2)
        v_part[m**2 + n **2]= phi_i_360     # it's handable if the dictionary is used
        
for i in range(N):
    for j in range(N):
        Points[i][j] = v_part[(6-i)**2 +(6-j)**2] if ((6-i)**2 + (6-j)**2) in v_part.keys() else 180
        

XX = Points

fig, ax = plt.subplots()
i = ax.imshow(XX, cmap=cm.jet, interpolation='nearest')
fig.colorbar(i)

plt.show()


dict_real_r_angle = {}

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
'''
P2 = np.zeros((N,N))    
for i in range(N):
    for j in range(N):
       index1 = find_the_most_similar_angle(Points[i][j], col1_deg)
       P2[i][j]= dict_r_ang[col1_deg[index1]] 
    
    

    
'''

N=13
P1_angle = np.zeros((N,N))  # angle
P2 = np.zeros((N,N))     #  r
P3 = [[] for i in range(N)]    #  real position

for m in range(0,7):
    for n in range(m+1):
        p_i = (p0[0]+m*p, p0[1]+n*p, p0[2])
        d_i = ( (p0[0] + m*p-pf[0])**2 + (p0[1]+ n*p -pf[1])**2 + (p0[2] - pf[2])**2)**0.5
        phi_i = k0 * (d_i - np.sin(theta0)*(p_i[0]*np.cos(phi0) + p_i[1]*np.sin(phi0)))
        phi_i_360 =  (phi_i % (2*np.pi))/np.pi*180
        v_part[m**2 + n **2]= phi_i_360     # it's handable if the dictionary is used
        
for i in range(N):
    for j in range(N):
        P1_angle[i][j] = v_part[(6-i)**2 +(6-j)**2] if ((6-i)**2 + (6-j)**2) in v_part.keys() else 180
        index1 = find_the_most_similar_angle(P1_angle[i][j], col1_deg)
        P2[i][j] = dict_r_ang[col1_deg[index1]]    # store the radius
        P3[i].append(((i-6)*p, (j-6)*p, 0))