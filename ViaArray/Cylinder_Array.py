


import math, os



path = r'E:\Data\Antenna  designs\201605' # The file path that you save the vbs script file
file_name = 'Cylinder_Array.vbs'          # The vbs script file name

file_path = path + '\\' + file_name       # The 
fout =open(file_path, 'w')




# cylinder 
center = (1,1,1)
r = 1
h = 2
name = 'via_my'
material = 'pec'

# duplicate along the vector 
line_vector = (1,2,3)
# the number of clones
NumClones = 6
axis = 'Z'


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




	
fout.writelines(Create_Cylinder(center, r, h,name, material,axis ) + '\n')
fout.writelines(Cylinder_Change_Prop(name, material) + '\n')
fout.writelines(DuplicateAlongLine(name, line_vector, NumClones)+ '\n')
#fout.writelines('oDestop.QuitApplication\n')

fout.close()
