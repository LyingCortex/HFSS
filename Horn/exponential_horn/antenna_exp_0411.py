# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import math, os
g = 1
r = 0.4
L = 26.2
a= 10 ** (math.log10(7.3)/L)
b = 3.15

name = 'via'
material = 'vacuum'
pos = []     #the position of the via
for x in range (27):
#    print x,
#    print ',',
#    print -a**x -2,
#    print ',',
#    print 0
#    print '\n'
    pos.append((-a**x -2,x,0))

print pos     #   [ (x, y, z), () ,()]





path = r'D:\Users\LY\Documents\Ansoft\MyDesign\SIW\201604\0411\Exp'
file_name = 'my_hfss.vbs'

file_path = path + '\\' + file_name
fout =file(file_path, 'w')
fout.writelines('Dim oAnsoftApp\n')
fout.writelines('Dim oDesktop\n')
fout.writelines('Dim oProject\n')
fout.writelines('Dim oDesign\n')
fout.writelines('Dim oEditor\n')
fout.writelines('Dim oModule\n')


fout.writelines('Set oAnsoftApp = CreateObject("AnsoftHfss.HfssScriptInterface")\n')
fout.writelines('Set oDesktop = oAnsoftApp.GetAppDesktop()\n')
fout.writelines('Set oProject = oDesktop.GetActiveProject ()\n')
fout.writelines('Set oDesign = oProject.GetActiveDesign ()\n')
fout.writelines('Set oEditor = oDesign.SetActiveEditor("3D Modeler")\n')



# Create Cylinder

def cylinder_array_pos(center, r, h):
    return 'Array(' + '"NAME:CylinderParameters", "XCenter:=", "'+ str(center[0])+'mm", "YCenter:=", "'  \
    + str(center[1])+ 'mm", "ZCenter:=", "' + str(center[2])  + 'mm", "Radius:=", "' + \
    str(r)+ 'mm", "Height:=", "' + str(h) + 'mm", "WhichAxis:=", "Z", "NumSides:=", "0"' + ')'


def cylinder_array_attr(name, material):
    return 'Array(' + '"NAME:Attributes", "Name:=", "'  + name + \
    '", "Flags:=", "",   "Color:=", "(132 132 193)", "Transparency:=", 0.400000005960464, "PartCoordinateSystem:=",  "Global", "UDMId:=", "", "MaterialValue:=", "" & Chr(34) & "' \
    + material + '" & Chr(34) & "", "SolveInside:=", true' + ')'
    
    


def cylinder_change_prop(name, material):
    return 'Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers","'+ \
    name + '"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "' + \
    material + '" & Chr(34) & ""))))'
    

for i in range(len(pos)):
    # Create Cylinder
    fout.writelines('oEditor.CreateCylinder ' + cylinder_array_pos(pos[i], r, b) + ', ' + cylinder_array_attr(name + str(i), material) + '\n' )
    # Change the material of cylinder
    fout.writelines('oEditor.ChangeProperty ' + cylinder_change_prop(name+str(i), 'pec') + '\n' )


fout.writelines('oDestop.QuitApplication\n')

   


fout.close()

 

