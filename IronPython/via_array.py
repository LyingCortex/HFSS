# -*- coding: utf-8 -*-
"""
Created on Fri May 27 10:25:35 2016

@author: LY
"""




oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.SetActiveEditor("3D Modeler")


'''
add_project_varible(varible, value, unit = 'mm')

example: varile = 'a', value =5, 5mm
'''
def add_design_varible(varible, value, unit = 'mm'):
    oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:"+varible,
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, str(value)+unit
				]
			]
		]
	])




def get_design_varibles():
    return oDesign.GetVariables()

def get_project_varibles():
    return oProject.GetVariables()
    
def save():
    oProject.Save()

def delete_design_varibles(varible):
    oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:DeletedProps", 
				varible
			]
		]
	])
# pos (x,y, z)
def pos2pos_str(pos, unit='mm'):
    pos_str = []
    for x in pos:
        pos_str.append(str(x)+unit)
    return pos_str 
def num2numwithunit(var, unit = 'mm'):
    return str(var) + unit
 
def CreateCylinder(center, r, h, name, material, SolveInside = True, Transparency=0.7): 
    if material == 'pec':
        SolveInside = False
    center_str = pos2pos_str(center, unit='mm')
    r_str = num2numwithunit(r, unit = 'mm')
    h_str = num2numwithunit(h, unit = 'mm')
    oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, center_str[0],
		"YCenter:="		, center_str[1],
		"ZCenter:="		, center_str[2],
		"Radius:="		, r_str,
		"Height:="		, h_str,
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, name,
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, Transparency,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"" + material +"\"",
		"SolveInside:="		, SolveInside
	])


#=======================================================================

# get all the design varibles 
local_var_array = get_design_varibles()


# the design varibles used in the design
varible_value = [('a', 5), ('d', 0.4), ('p', 0.6), ('Wsub', 70), ('Lsub', 63.5), ('H', 0.508)]
for vv in varible_value:
    if vv[0] not in local_var_array:
        add_design_varible(vv[0], vv[1])

center = (1,2,4)
r = 1
h =3
material = 'pec'
name = 'via_test1'
#CreateCylinder(center, r, h, name, material, SolveInside = True, Transparency=0.7)
class Cylinder:
    def __init__(self, center, radius, height, name, material):
        self.center = center
        self.radius = radius
        self.height = height
        self.name = name
        self.material = material
    def center2center_str(self, unit='mm'):
        pos_str = []
        for x in self.center:
            pos_str.append(str(x)+unit)
        return pos_str 
    def num2numwithunit(var, unit = 'mm'):
        return str(var) + unit    
    def Create(self, SolveInside = True, Transparency=0.7 ): 
        if self.material == 'pec':
            self.SolveInside = False
        center_str = center2center_str()
        r_str = num2numwithunit(self.radius, unit = 'mm')
        h_str = num2numwithunit(self.height, unit = 'mm')
        oEditor.CreateCylinder([
		"NAME:CylinderParameters",
		"XCenter:="		, center_str[0],
		"YCenter:="		, center_str[1],
		"ZCenter:="		, center_str[2],
		"Radius:="		, r_str,
		"Height:="		, h_str,
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"], [
		"NAME:Attributes",
		"Name:="		, self.name,
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, Transparency,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"" + self.material +"\"",
		"SolveInside:="		, SolveInside])


cylinder1 = Cylinder(center, r, h, name, material)
cylinder1.Create()

save()









