# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:10:13 2016

@author: LY
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 13:55:26 2016

@author: LY
"""




'''
All the antenna parameters.

SIW Part:
width  : a
height : H
length : L1

via parameters:
diameter: d
spacing: p

horn flaring angle: horn_theta
horn length : L2



length


'''

import math


oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.SetActiveEditor("3D Modeler")
##============================================================================
# Rename the design name 
def RenameDesignInstance(new_design_name):
    old_design_name = oDesign.GetName()
    oDesign.RenameDesignInstance(old_design_name, new_design_name)
    
##============================================================================  
def get_design_varibles():
    return oDesign.GetVariables()
##============================================================================
def get_project_varibles():
    return oProject.GetVariables()
##============================================================================    
def save():
    oProject.Save()
##============================================================================   
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
					"Value:="		, [str(value)+unit if type(value) != type('d') else value][0]  ## 在一句话中完成了判断，未验证
				]
			]
		]
	]) 
       
    
##============================================================================   
def add_design_varible_without_unit(varible, value):
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
					"Value:="		, [str(value) if type(value) != type('d') else value][0]  ## 在一句话中完成了判断，未验证
				]
			]
		]
	]) 
         
##============================================================================
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
##============================================================================      
'''
CreatePolyline(Points, name, material , unit = 'mm', IsPolylineClosed = False, SolveInside = True, Transparency = 0.7)

'''       
def CreatePolyline(Points, name, material , IsPolylineClosed = False, SolveInside = True, Transparency = 0.7):
    if (Points[0] == Points[-1]):
        IsPolylineClosed = True
    if material == 'pec' or material =='copper':
        SolveInside = False
        
    NumofPoints = len(Points)
    oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, IsPolylineClosed,
		["NAME:PolylinePoints"] + [["NAME:PLPoint","X:=", point[0],	"Y:=", point[1],"Z:=", point[2]] for point in Points],
		["NAME:PolylineSegments"] + [["NAME:PLSegment","SegmentType:="	, "Line","StartIndex:=", k,	"NoOfPoints:=", 2] for k in range(NumofPoints-1)],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, name,
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	,Transparency,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"" + material + "\"",
		"SolveInside:="		, SolveInside
	])


##========================================================================================

def SweepAlongVector(name, sweep_vec,unit = 'mm'):
    oEditor.SweepAlongVector(
	[
		"NAME:Selections",
		"Selections:="		, name,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:VectorSweepParameters",
		"DraftAngle:="		, "0deg",
		"DraftType:="		, "Extended",
		"CheckFaceFaceIntersection:=", False,
		"SweepVectorX:="	, [str(sweep_vec[0])+unit if type(sweep_vec[0]) != type('d') else sweep_vec[0]][0],
		"SweepVectorY:="	, [str(sweep_vec[1])+unit if type(sweep_vec[1]) != type('d') else sweep_vec[1]][0],
		"SweepVectorZ:="	, [str(sweep_vec[2])+unit if type(sweep_vec[2]) != type('d') else sweep_vec[2]][0]
	])


##============================================================================
'''
DuplicateAlongLine(name, direction, NumClones, unit = 'mm')
沿直线复制选中的物体，输入物体名称，复制的方向，复制的个数（包括当前的物体），方向矢量的单位
'''
def DuplicateAlongLine(name, direction, NumClones, unit = 'mm'):
    oEditor.DuplicateAlongLine(
	[
		"NAME:Selections",
		"Selections:="		, name,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToAlongLineParameters",
		"CreateNewObjects:="	, True,
		"XComponent:="		, [str(direction[0]) + unit  if type(direction[0]) != type('a') else direction[0]][0],
		"YComponent:="		, [str(direction[1]) + unit  if type(direction[1]) != type('a') else direction[1]][0],
		"ZComponent:="		, [str(direction[2]) + unit  if type(direction[2]) != type('a') else direction[2]][0],
		"NumClones:="		, str(NumClones)
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	])
##====================================================================================
def Move(name, direction, unit = 'mm'):
    oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, name,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, [str(direction[0]) + unit  if type(direction[0]) != type('a') else direction[0]][0],
		"TranslateVectorY:="	, [str(direction[1]) + unit  if type(direction[1]) != type('a') else direction[1]][0],
		"TranslateVectorZ:="	, [str(direction[2]) + unit  if type(direction[2]) != type('a') else direction[2]][0]
	])
##====================================================================================
'''
create the box boject
name: the box name you want to named 
position: the first point of the box
box_size: a 3-elements list representing the size of the box
material: the material of the box
'''
def CreateBox(name, position, box_size, material, unit = 'mm', SolveInside = True):
    if material == 'pec' or material == 'copper':
        SolveInside = False
    oEditor.CreateBox(
        [
    		"NAME:BoxParameters",
    		"XPosition:="		, [str(position[0]) + unit if type(position[0]) != type('a') else position[0]][0],
    		"YPosition:="		, [str(position[1]) + unit if type(position[1]) != type('a') else position[1]][0],
    		"ZPosition:="		, [str(position[2]) + unit if type(position[2]) != type('a') else position[2]][0],
    		"XSize:="		      , [str(box_size[0]) + unit if type(box_size[0]) != type('a') else box_size[0]][0] ,
    		"YSize:="		      , [str(box_size[1]) + unit if type(box_size[1]) != type('a') else box_size[1]][0],
    		"ZSize:="		      , [str(box_size[2]) + unit if type(box_size[2]) != type('a') else box_size[2]][0]
        ], 
    	  [
    		"NAME:Attributes",
    		"Name:="		, name,
    		"Flags:="		, "",
    		"Color:="		, "(132 132 193)",
    		"Transparency:="	, 0.7,
    		"PartCoordinateSystem:=", "Global",
    		"UDMId:="		, "",
    		"MaterialValue:="	, "\"" + material + "\"",
    		"SolveInside:="		, SolveInside
    	  ])
       
##========================================================================================
'''
create the cylinder 

center: the bottom face
'''
def CreateCylinder(center, r, h, name, material, unit = 'mm', WhichAxis = 'Z', SolveInside = True, Transparency=0.7): 
    if material == 'pec':
        SolveInside = False
    
    oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, [str(center[0]) + unit if type(center[0]) != type('a') else center[0]][0],
		"YCenter:="		, [str(center[1]) + unit if type(center[1]) != type('a') else center[1]][0],
		"ZCenter:="		, [str(center[2]) + unit if type(center[2]) != type('a') else center[2]][0],
		"Radius:="		, [str(r) + unit if type(r) != type('a') else r][0],
		"Height:="		, [str(h) + unit if type(h) != type('a') else h][0],
		"WhichAxis:="		, WhichAxis,
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
 
##=========================================================================================
'''
create rectangle
'''
def CreateRectangle(name, start_pos, Width, Height, unit = 'mm', WhichAxis = 'Z'):
    oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="	, True,
		"XStart:="		, [str(start_pos[0]) + unit if type(start_pos[0]) != type('a') else start_pos[0]][0],
		"YStart:="		, [str(start_pos[1]) + unit if type(start_pos[1]) != type('a') else start_pos[1]][0],
		"ZStart:="		, [str(start_pos[2]) + unit if type(start_pos[2]) != type('a') else start_pos[2]][0],
		"Width:="		, [str(Width) + unit if type(Width) != type('a') else Width][0],
		"Height:="		, [str(Height) + unit if type(Height) != type('a') else Height][0],
		"WhichAxis:="	, WhichAxis
	], 
	[
		"NAME:Attributes",
		"Name:="		, name,
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])




##=======================================================
'''
thers's sth wrong with this function

def GetObjectIDByName(name):
    objID = oEditor.GetSelections   # to be continued

    #AddErrorMessage(str(objID))

'''
##===================================================================
def Delete(name):
    oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, name
	])



##===================================================================

def Add_varible_list(varible_value):
    local_var_array = get_design_varibles()
    for vv in varible_value:
        if vv[0] not in local_var_array:
            add_design_varible(vv[0], vv[1])
        else:
            delete_design_varibles(vv[0])
            add_design_varible(vv[0], vv[1])
    
##==================================================================

def Add_varible_list_without_unit(varible_value):
    local_var_array = get_design_varibles()
    for vv in varible_value:
        if vv[0] not in local_var_array:
            add_design_varible_without_unit(vv[0], vv[1])
        else:
            delete_design_varibles(vv[0])
            add_design_varible_without_unit(vv[0], vv[1])    
    
##================================================================
def DuplicateMirror(name_array, Base, Normal, unit = 'mm' ):
    name_array_str = ''
    for s in name_array:
        name_array_str += s
        name_array_str += ','
    name_array_str =name_array_str[0:-1]
        
    oEditor.DuplicateMirror(
	[
		"NAME:Selections",
		"Selections:="		, name_array_str,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToMirrorParameters",
		"DuplicateMirrorBaseX:=", [str(Base[0]) + unit if type(Base[0]) != type('a') else Base[0]][0],
		"DuplicateMirrorBaseY:=", [str(Base[1]) + unit if type(Base[1]) != type('a') else Base[1]][0],
		"DuplicateMirrorBaseZ:=", [str(Base[2]) + unit if type(Base[2]) != type('a') else Base[2]][0],
		"DuplicateMirrorNormalX:=", [str(Normal[0]) + unit if type(Normal[0]) != type('a') else Normal[0]][0],
		"DuplicateMirrorNormalY:=", [str(Normal[1]) + unit if type(Normal[1]) != type('a') else Normal[1]][0],
		"DuplicateMirrorNormalZ:=", [str(Normal[2]) + unit if type(Normal[2]) != type('a') else Normal[2]][0]
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	])
###================================================================================================================
'''
create relative coordinate system
'''
def CreateRelativeCS( name, Origin_pos, X_vec, Y_vec, unit = 'mm'):
    oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, [str(Origin_pos[0]) + unit if type(Origin_pos[0]) != type('a') else Origin_pos[0]][0],
		"OriginY:="		, [str(Origin_pos[1]) + unit if type(Origin_pos[1]) != type('a') else Origin_pos[1]][0],
		"OriginZ:="		, [str(Origin_pos[2]) + unit if type(Origin_pos[2]) != type('a') else Origin_pos[2]][0],
		"XAxisXvec:="		, [str(X_vec[0]) + unit if type(X_vec[0]) != type('a') else X_vec[0]][0],
		"XAxisYvec:="		, [str(X_vec[1]) + unit if type(X_vec[1]) != type('a') else X_vec[1]][0],
		"XAxisZvec:="		, [str(X_vec[2]) + unit if type(X_vec[2]) != type('a') else X_vec[2]][0],
		"YAxisXvec:="		, [str(Y_vec[0]) + unit if type(Y_vec[0]) != type('a') else Y_vec[0]][0],
		"YAxisYvec:="		, [str(Y_vec[1]) + unit if type(Y_vec[1]) != type('a') else Y_vec[1]][0],
		"YAxisZvec:="		, [str(Y_vec[2]) + unit if type(Y_vec[2]) != type('a') else Y_vec[2]][0]
	], 
	[
		"NAME:Attributes",
		"Name:="		, name
	])
    

##=================================================================================================================
'''
set working coordinate system
'''
def SetWCS(name = 'Global'):
    oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", name
	])
 
###================================================================================================================
def Rotate( name, RotateAngle, unit = 'deg', RotateAxis = 'Z'):
    oEditor.Rotate(
	[
		"NAME:Selections",
		"Selections:="		, name,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:RotateParameters",
		"RotateAxis:="		, "Z",
		"RotateAngle:="		, [str(RotateAngle) + unit if type(RotateAngle) != type('a') else RotateAngle][0]
	])


###================================================================================================================
'''
Tool_Parts   "slot1,slot2,slot3,slot4"
'''
def Substract(Blank_Parts, Tool_Parts, KeepOriginals=False ):
    oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, Blank_Parts,
		"Tool Parts:="		, Tool_Parts
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])

###=================================================================================
def Unite(name_array):
    name_array_str = ''
    for s in name_array:
        name_array_str += s
        name_array_str += ','
    name_array_str =name_array_str[0:-1]
    oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, name_array_str
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])


###=======================================
def Rename(select_name, changed_name1):
    oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				select_name
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, changed_name1
				]
			]
		]
	])

###==============================================================================
def ChangeColor(RGB, select_name):
    oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				select_name
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, RGB[0],
					"G:="			, RGB[1],
					"B:="			, RGB[2]
				]
			]
		]
	])

###================================================================================================================
def Add_error_message(message):
    AddErrorMessage(message)
    
    



####===============================================================
    
a = 6

################### the design varibles used in the design


ri = a/2
L1 = 10
Ra = 5.6
N1 = 10
z1 = [L1/N1*i for i in range(N1+1)]
r1 = [ri+(Ra-ri)*math.sin(math.pi*zi /2/L1) ** 0.75  for zi in z1]

pos = []
for i in range(1,N1+1):
    pos.append((0,-r1[i],z1[i]))

    
name = ['avia_curve' + str(i+1) + 'sin' for i in range(N1+1)]


###=================================================================




p  = 1 
LL = 20
N2 = math.ceil((LL -L1)/p)
#Add_error_message('what..........' + str(N2))
rL = 17.8/2
q =(LL - L1)/ ((rL/Ra)**2-1)**0.5

z2 = [L1+(LL-L1)/N2*(i+1) for i in range(N2)]

r2 = [Ra*(1+((zi-L1)/q)**2)**0.5  for zi in z2]




pos2 = []
for i in range(N2):
    pos2.append((0,-r2[i],z2[i]))

name2 = ['agauss' + str(i+1) + 'sin' for i in range(N2)]
###==================================================================================


 

h= 'b'
material = 'pec'
r= 'd/2'
for i in range(N1):
    CreateCylinder(pos[i], r, h, name[i], material, WhichAxis = 'X', SolveInside = True, Transparency=0.7)
for i in range(N2):
    CreateCylinder(pos2[i], r, h, name2[i], material, WhichAxis = 'X', SolveInside = True, Transparency=0.7)

Base =(0, 0 ,0)
Normal = (0, 1, 0)
DuplicateMirror(name, Base, Normal, unit = 'mm' )
DuplicateMirror(name2, Base, Normal, unit = 'mm' )
