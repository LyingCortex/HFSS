# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 22:15:06 2016

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
    if material == 'pec':
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
'''
create the box boject
name: the box name you want to named 
position: the first point of the box
box_size: a 3-elements list representing the size of the box
material: the material of the box
'''
def CreateBox(name, position, box_size, material, unit = 'mm'):
    
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
    		"SolveInside:="		, True
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




local_var_array = get_design_varibles()
################### the design varibles used in the design
varible_value = [('yy', 0.6),('height', 2),('LL', 0.1)]

for vv in varible_value:
    if vv[0] not in local_var_array:
        add_design_varible(vv[0], vv[1])
    else:
        delete_design_varibles(vv[0])
        add_design_varible(vv[0], vv[1])
        
local_var_array = get_design_varibles()
################# the design varibles used in the design

######### 进行两次的原因是在第二次使用时用变量名称来表示其他变量,变量都是用字符表达式来表示的。
## Using the method twice is to express a new varible by other named varibles' name. The value of the new varible is expressed by character expression
varible_value = [('xx', '(DD-yy)/6')]

for vv in varible_value:
    if vv[0] not in local_var_array:
        add_design_varible(vv[0], vv[1])
    else:
        delete_design_varibles(vv[0])
        add_design_varible(vv[0], vv[1]) 
 
'''
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
		"SweepVectorX:="	, str(sweep_vec[0]) + unit,
		"SweepVectorY:="	, str(sweep_vec[1]) + unit,
		"SweepVectorZ:="	, str(sweep_vec[2]) + unit
	])




##=============
def GetObjectIDByName(name):
    objID = oEditor.GetSelections   # to be continued

    AddErrorMessage(str(objID))


##==========
def Delete(name):
    oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, name
	])



##========================

def Add_varible_list(varible_value):
    for vv in varible_value:
        if vv[0] not in local_var_array:
            add_design_varible(vv[0], vv[1])
        else:
            delete_design_varibles(vv[0])
            add_design_varible(vv[0], vv[1])
    
##========================

def Add_varible_list_without_unit(varible_value):
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



###==========================================
def Add_error_message(message):
    AddErrorMessage(message)
    
    
###========================================
f = 25
er = 2.2 
lambda_0 = 300.0 / f
lambda_g = lambda_0 / er**0.5



wp1 = 16.8
wp2 = 12
l1 = 3.5
l2 = 2.4

list_1 = [wp1, wp2, l1, l2]
list_2 = [ x/lambda_g for x in list_1]



lambda_g_new = 20 /2.2**0.5

list_3 = [x * lambda_g_new for x in list_2]
#wp1 =8
#wp2 = 7
#l1 = lambda_g_new /4
#l2 = list_3[3]
#########################
####  11:27
#wp1 =18
#wp2 = 12
#l1 = lambda_g_new /4
#l2 = list_3[3]

########################
###  14:13
#wp1 =18
#wp2 = 12
#l1 = lambda_g_new /4
#l2 = 2
#########################
####  14:51
#wp1 =20
#wp2 = 14
#l1 = lambda_g_new /4
#l2 = 3


#######
###  06-23  10:00
#wp1 =25
#wp2 = 16
#l1 = 4
#l2 = 3.4
#######
####  06-23  10:23
#wp1 =25
#wp2 = 18
#l1 = 4
#l2 = 3.4
##############
####  06-23  10:35
#wp1 =26
#wp2 = 16
#l1 = 4
#l2 = 3.4
###############
####  06-23  10:35
#wp1 =23
#wp2 = 16
#l1 = 4
#l2 = 3.4
###############
###  06-23  11：35
wp1 = 22
wp2 = 17
ll1 = 4.2
ll2 = 3.6
##############
a = 12
p = 1

lsiw = 14.4
w = 1.2
N6 = math.ceil(lsiw/w)

#list_4 = [ math.ceil(x/p) for x in list_3]
N1 = math.ceil(ll1/p)
N2 = math.ceil((wp1-wp2)/2/p)
N3 = math.ceil(ll2/p)
N4 = math.ceil((wp2-a)/2/p)
N5 = math.ceil(wp1/p)








####===============================================================



################### the design varibles used in the design
local_var_array = get_design_varibles()
varible_value = [('wp1',wp1),('wp2',wp2),('ll1',ll1),('ll2',ll2),('p',p),('a',a)]
Add_varible_list(varible_value)

varible_value_without_unit = [('N1', N1), ('N2', N2), ('N3', N3), ('N4', N4), ('N5',N5),('N6',N6)]
Add_varible_list_without_unit(varible_value_without_unit) 

list1 = [('wp1/2', 'll1/N1*'+str(i), '0')  for i in range(N1+1)]
list8 = [('-wp1/2', 'll1/N1*'+str(i), '0')  for i in range(N1+1)]
list2 = [('wp1/2 - (wp1-wp2)/2/N2*'+str(i), 'll1', '0') for i in range(1,N2+1)]
list7 = [('-wp1/2 + (wp1-wp2)/2/N2*'+str(i), 'll1', '0') for i in range(1,N2+1)]
list3 = [('wp2/2', 'll1+ll2/N3*'+str(i),' 0' ) for i in range(1, N3+1)]
list6 = [('-wp2/2', 'll1+ll2/N3*'+str(i),' 0' ) for i in range(1, N3+1)]
list4 = [('wp2/2-(wp2-a)/2/N4*'+ str(i), 'll1+ll2',' 0') for i in range(1, N4+1)]
list5 = [('-wp2/2+(wp2-a)/2/N4*'+ str(i), 'll1+ll2',' 0') for i in range(1, N4+1)]
list9 = [('-wp1/2+ wp1/N5*'+str(i), '0', '0') for i  in range(1,N5)]

list_siw = [(0,'-a/2', '-lsiw-d/2+w*'+str(i))  for i in range(1, N6+1)]

list_total = []
length_via = 0
for i in range(1,10):     
    #list_total.extend(locals()['list{}'.format(i)])
    list_total.extend(locals()['list'+str(i)])
    length_via += len(locals()['list'+str(i)])

list_via_name = ['via_f_'+ str(i+1) for i in range(length_via)]    
list_sum = [(z, x, y+'-ll1-ll2-lsiw-d/2') for (x, y, z) in list_total]

h= 'h'
material = 'pec'
r= 'd/2'
for i in range(length_via):
    CreateCylinder(list_sum[i], r, h, list_via_name[i], material, WhichAxis = 'X', SolveInside = True, Transparency=0.7)



name_siw = ['siw_via'+str(i+1) for i in range(len(list_siw))]
for i in range(len(list_siw)):
    CreateCylinder(list_siw[i], r, h, name_siw[i], material, WhichAxis = 'X', SolveInside = True, Transparency=0.7)

Base = (0, 0, 0)
Normal = (0, 1, 0)
DuplicateMirror(name_siw, Base, Normal, unit = 'mm' )