# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:45:05 2016

@author: LY
"""

'''
Set the values of the basic parameters when start.
cener position
the vbs file path you want to store, recommanding put it in the HFSS design file folder.
radius
the thickness of the substrate
the period of the vias
the material
the number of duplicating
the vector which describe the direction of the duplicate
'''


import math, os



path = r'E:\Data\Antenna  designs\201512' # The file path that you save the vbs script file
file_name = 'Cylinder_Array_2016_05_11.vbs'          # The vbs script file name

W2 = 7.2 #mm

# cylinder 
center = (-W2/2, 0, 0)
r = 0.25   #mm
h = 1.524 #mm
p = 0.9   #mm
name = 'via'
material = 'pec'
# the number of clones
NumClones = 9
axis = 'Z'


# duplicate along the vector 
line_vector = (p, 0, 0)


file_path = path + '\\' + file_name       # The 
fout =open(file_path, 'w')

# HFSS Initilization

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

	
# create the cylinder object 
'''
center : turple  (x, y, z)
r      : radius
h      : height
name   : the name of the cylinder
material : the material of  cylinder 
Axis   : 'Z'
'''	
def Create_Cylinder(center, r, h, name, material,axis = 'Z'):
    return 'oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=", "' + str(center[0])+ 'mm", "YCenter:=","' +\
	str(center[1])+ 'mm", "ZCenter:=", "' + str(center[2]) + 'mm", "Radius:=", "'+ str(r) + 'mm", "Height:=", "' + str(h)+ 'mm", "WhichAxis:=", "'+ \
	axis + '","NumSides:=", "0"), Array("NAME:Attributes", "Name:=", "' + name + '", "Flags:=","", "Color:=", "(132 132 193)", "Transparency:=", 0.4,'+\
	'"PartCoordinateSystem:=",  "Global", "UDMId:=", "", "MaterialValue:=", "" & Chr(34) & "' + material +'" & Chr(34) & "", "SolveInside:=", false)'

def Cylinder_Change_Prop(name, material):
    return 'oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers", "'+ \
	name + '"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "'+ material + '" & Chr(34) & ""))))'

  

def DuplicateAlongLine(name, line_vector, NumClones):
    return 'oEditor.DuplicateAlongLine Array("NAME:Selections", "Selections:=", "' + name + '", "NewPartsModelFlag:=", "Model"),' +\
	'Array("NAME:DuplicateToAlongLineParameters", "CreateNewObjects:=", true, "XComponent:=","' + str(line_vector[0]) + 'mm",' +\
	'"YComponent:=", "' + str(line_vector[1]) + 'mm", "ZComponent:=", "' + str(line_vector[2]) +'mm", "NumClones:=", "'   + str(NumClones) + '"),'   +\
	'Array("NAME:Options", "DuplicateAssignments:=", true)'


'''
# Convert the position without unit to the position string with unit so that it can
#  be easily used in the following operations.	
'''
def pos2pos_str(pos, unit='mm'):
    pos_str = []
    for x in pos:
        pos_str.append(str(x)+unit)
    return pos_str




'''
# Duplicate the chosen object with the specific axis
----name_array : the name array of the object you want to duplicate
----base_pos   : the first point of the normal vector of the symmetry plane
----normal_pos : the second point of the normal vector of the symmetry plane
# return a piece of  VB script that can perform the duplicate function
'''	
def DuplicateMirror(name_array, base_pos, normal_pos):
    name_str = ''
    for name in name_array:
        name_str = name_str + name + ','
    name_str = name_str[0:-1]
    base_pos_str = pos2pos_str(base_pos, unit='mm')
    normal_pos_str = pos2pos_str(normal_pos, unit='mm')
    return 'oEditor.DuplicateMirror Array("NAME:Selections", "Selections:=", "' + name_str + '", "NewPartsModelFlag:=", "Model"), ' + \
	'Array("NAME:DuplicateToMirrorParameters", "DuplicateMirrorBaseX:=",  "' + base_pos_str[0] + '", "DuplicateMirrorBaseY:=", "' + base_pos_str[1] +\
	'", "DuplicateMirrorBaseZ:=", "' + base_pos_str[2] + '", "DuplicateMirrorNormalX:=",  "' + normal_pos_str[0] + '", "DuplicateMirrorNormalY:=", "'+\
	normal_pos_str[1] + '", "DuplicateMirrorNormalZ:=", "'+ normal_pos_str[2] + '"), Array("NAME:Options", "DuplicateAssignments:=",  true)'


    

	
fout.writelines(Create_Cylinder(center, r, h,name, material,axis ) + '\n')
fout.writelines(Cylinder_Change_Prop(name, material) + '\n')
fout.writelines(DuplicateAlongLine(name, line_vector, NumClones)+ '\n')

# Another duplicate
L2 = 4.8
r1 = 0.2
p1 = 0.6   # L2 / 8
NumClones1 = 9
line_vector1 = (0, p1, 0)


fout.writelines(DuplicateAlongLine(name, line_vector1, NumClones1)+ '\n')


#fout.writelines('oDestop.QuitApplication\n')

fout.close()
