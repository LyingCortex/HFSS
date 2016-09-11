# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:44:41 2016
change numpy
@author: LY
"""
   
import math   
    
###############
##################
###############
##################
###############
##################
##################
###############
##################
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
w = 1
g = 1.5
Rs =1.5
Rb = Rs + g + w
f0 = 13.58
Lambda = 300/f0
P = 0.52*Lambda
angle_off = 30 
p=P

D = 149.3
f = D *0.8

theta0 = 0/180*math.pi  # deg
phi0 = 0/180*math.pi

k0 = 2*math.pi/Lambda

###=================================================================================
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
col1 =[eval(i)/180*math.pi for i in col1[1:-1]]
col1_deg = [i%(2*math.pi) /math.pi *180   for i in col1]

for i in range(len(col1)):
    dict_r_ang[col1_deg[i]]=colr[i]

f1.close()





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


v_part = {}  # point and value
N=13
P1_angle = [[0 for j in range(N)] for i in range(N)]  # angle
P2 = [[0 for j in range(N)] for i in range(N)]     #  r
P3 = [[] for i in range(N)]    #  real position



for m in range(0,7):
    for n in range(m+1):
        p_i = (p0[0]+m*p, p0[1]+n*p, p0[2])
        d_i = ( (p0[0] + m*p-pf[0])**2 + (p0[1]+ n*p -pf[1])**2 + (p0[2] - pf[2])**2)**0.5
        phi_i = k0 * (d_i - math.sin(theta0)*(p_i[0]*math.cos(phi0) + p_i[1]*math.sin(phi0)))
        phi_i_360 =  (phi_i % (2*math.pi))/math.pi*180
        v_part[m**2 + n **2]= phi_i_360     # it's handable if the dictionary is used
        
for i in range(N):
    for j in range(N):
        P1_angle[i][j] = v_part[(6-i)**2 +(6-j)**2] if ((6-i)**2 + (6-j)**2) in v_part.keys() else 180
        index1 = find_the_most_similar_angle(P1_angle[i][j], col1_deg)
        P2[i][j] = dict_r_ang[col1_deg[index1]]    # store the radius
        P3[i].append(((i-6)*p, (j-6)*p, 0))


##################################################################################



for i in range(N):
    for j in range(N):
        center=P3[i][j]
        r_in = P2[i][j]
        r_out = r_in + g + w
        name_bo = 'Circle_Big_o' +'_'+str(i) +'_'+ str(j)
        name_bi = 'Circle_Big_i' +'_'+str(i) +'_'+ str(j)
        name_so = 'Circle_Small_o' +'_'+str(i) +'_'+ str(j)
        name_si = 'Circle_Small_i' +'_'+str(i) +'_'+ str(j)
        print('center = ' + str(center))
        print('r = ' + str(r_in))

        pl1 = 'pl1' +'_'+str(i) +'_'+ str(j)
        pl2 = 'pl2' +'_'+str(i) +'_'+ str(j)
        pl3 = 'pl3'+'_'+str(i) +'_'+ str(j)
        pl4 = 'pl4' +'_'+str(i) +'_'+ str(j) 
        

        
    
###==============================================================   





  











    
   

    