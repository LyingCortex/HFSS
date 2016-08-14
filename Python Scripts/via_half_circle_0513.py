# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:40:31 2016

@author: LY
"""


import math, os
import numpy as np



f = 24.15  # GHz
wave_length = 300.0 / f  # lambda
p = 1 # mm  spacing
opt_n = 0.3    # the varible used to optmize the structure
extend_r  = opt_n * wave_length
theta_v = p * 1.0 / extend_r
num_v =round(math.pi / theta_v)
theta_array = np.linspace(0, math.pi, num_v)
pos = [(extend_r * math.sin(t), -(extend_r - extend_r * math.cos(t)), 0 ) for t in theta_array]




path = r'E:\Data\Antenna  designs\201605\FTB_SLL  - 20160511' # The file path that you save the vbs script file
file_name = 'via_half_circle_0513.vbs'          # The vbs script file name

file_path = path + '\\' + file_name       # The 
fout =open(file_path, 'w')

fout.writelines('Dim oAnsoftApp\n')
fout.writelines('Dim oDesktop\n')
fout.writelines('Dim oProject\n')
fout.writelines('Dim oDesign\n')
fout.writelines('Dim oEditor\n')
fout.writelines('Dim oModule\n')


fout.writelines('Set oAnsoftApp = CreateObject("AnsoftHfss.HfssScriptInterface")\n') # This is the format of HFSS 15.0
fout.writelines('Set oDesktop = oAnsoftApp.GetAppDesktop()\n')
fout.writelines('Set oProject = oDesktop.GetActiveProject ()\n')
fout.writelines('Set oDesign = oProject.GetActiveDesign ()\n')
fout.writelines('Set oEditor = oDesign.SetActiveEditor("3D Modeler")\n')



def Create_Cylinder(center, r, h, name, material,axis = 'Z'):
    return 'oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=", "' + str(center[0])+ 'mm", "YCenter:=","' +\
	str(center[1])+ 'mm", "ZCenter:=", "' + str(center[2]) + 'mm", "Radius:=", "'+ str(r) + 'mm", "Height:=", "' + str(h)+ 'mm", "WhichAxis:=", "'+ \
	axis + '","NumSides:=", "0"), Array("NAME:Attributes", "Name:=", "' + name + '", "Flags:=","", "Color:=", "(132 132 193)", "Transparency:=", 0.4,'+\
	'"PartCoordinateSystem:=",  "Global", "UDMId:=", "", "MaterialValue:=", "" & Chr(34) & "' + material +'" & Chr(34) & "", "SolveInside:=", false)'

def Cylinder_Change_Prop(name, material):
    return 'oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers", "'+ \
	name + '"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "'+ material + '" & Chr(34) & ""))))'



def pos2pos_str(pos, unit='mm'):
    pos_str = []
    for x in pos:
        pos_str.append(str(x)+unit)
    return pos_str
    
    
    

#fout.writelines(Create_Cylinder(center, r, h,name, material,axis ) + '\n')
#fout.writelines(Cylinder_Change_Prop(name, material) + '\n')
#fout.writelines(DuplicateAlongLine(name, line_vector, NumClones)+ '\n')
via_name = 'via_hc'
r=0.4
h = 3.15
material = 'pec'
for i in range(len(pos)):
    via_name_str = via_name +  str(i)
    fout.writelines(Create_Cylinder(pos[i], r, -h, via_name_str, material,axis = 'Z') + '\n')

fout.close()