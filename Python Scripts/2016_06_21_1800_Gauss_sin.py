# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:57:14 2016

@author: LY
"""



Ra = 9.1
L1 = 34.3
N1 = 35
LL = 93.2
N1 = round(LL -L1)

rL = 14.9
q =(LL - L1)/ ((rL/Ra)**2-1)**0.5
z2 = [L1+(LL-L1)/N1*(i+1) for i in range(N1)]
r2 = [Ra*(1+((zi-L1)/q)**2)**0.5  for zi in z2]

pos = []
for i in range(N1):
    pos.append((0,-r2[i],z2[i]))
    
    
    


ri = 12/2
L1 = 34.3
Ra = 9.1
N1 = 35
pp = 0.75
z1 = [34.3/N1*i for i in range(N1+1)]
r1 = [ri+(Ra-ri)*math.sin(math.pi*zi /2/L1) ** pp  for zi in z1]

pos1 = []
for i in range(N1+1):
    pos1.append((0,-r1[i],z1[i]+0.4))