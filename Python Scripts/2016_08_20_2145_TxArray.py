# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:44:41 2016
change numpy
@author: LY
"""


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

###==================================================================
'''create circle
'''
def CreateCircle(name, center, r,unit = 'mm', WhichAxis ='Z'):
    oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, [str(center[0]) + unit if type(center[0]) != type('a') else center[0]][0],
		"YCenter:="		, [str(center[1]) + unit if type(center[1]) != type('a') else center[1]][0],
		"ZCenter:="		, [str(center[2]) + unit if type(center[2]) != type('a') else center[2]][0],
		"Radius:="		, [str(r) + unit if type(r) != type('a') else r][0],
		"WhichAxis:="		, WhichAxis,
		"NumSegments:="		, "0"
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
    
#######============================================================================================================
'''
create arc
'''
def CreateArcSector(name, center, start_point,  angle, unit = 'mm'):
    oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, True,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, [str(start_point[0]) + unit if type(start_point[0]) != type('a') else start_point[0]][0],
				"Y:="			, [str(start_point[1]) + unit if type(start_point[1]) != type('a') else start_point[1]][0],
				"Z:="			, [str(start_point[2]) + unit if type(start_point[2]) != type('a') else start_point[2]][0]
			],
			[
				"NAME:PLPoint",
				"X:="			, "-4.67360850773209mm",
				"Y:="			, "1.77690278756443mm",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-3.7370465934183mm",
				"Y:="			, "3.3218191941496mm",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, [str(center[0]) + unit if type(center[0]) != type('a') else center[0]][0],
				"Y:="			, [str(center[1]) + unit if type(center[1]) != type('a') else center[1]][0],
				"Z:="			, [str(center[2]) + unit if type(center[2]) != type('a') else center[2]][0]
			],
			[
				"NAME:PLPoint",
				"X:="			, [str(start_point[0]) + unit if type(start_point[0]) != type('a') else start_point[0]][0],
				"Y:="			, [str(start_point[1]) + unit if type(start_point[1]) != type('a') else start_point[1]][0],
				"Z:="			, [str(start_point[2]) + unit if type(start_point[2]) != type('a') else start_point[2]][0]
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "AngularArc",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 3,
				"NoOfSegments:="	, "0",
				"ArcAngle:="		, str(angle) + 'deg',
				"ArcCenterX:="		, [str(center[0]) + unit if type(center[0]) != type('a') else center[0]][0],
				"ArcCenterY:="		, [str(center[1]) + unit if type(center[1]) != type('a') else center[1]][0],
				"ArcCenterZ:="		, [str(center[2]) + unit if type(center[2]) != type('a') else center[2]][0],
				"ArcPlane:="		, "XY"
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 2,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 3,
				"NoOfPoints:="		, 2
			]
		],
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
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
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
		"KeepOriginals:="	, KeepOriginals
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
    
    
###====================================================================================================================
    
    
    
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
        

        CreateCircle(name_bo, center, r_out + w)
        CreateCircle(name_bi, center, r_out)
        CreateCircle(name_so, center, r_in + w)
        CreateCircle(name_si, center, r_in)

        Substract(name_bo, name_bi )
        Rename(name_bo, 'Ring_O'+'_'+str(i) +'_'+ str(j))
        Substract(name_so, name_si )
        Rename(name_so, 'Ring_I'+'_'+str(i) +'_'+ str(j))


        pl1 = 'pl1' +'_'+str(i) +'_'+ str(j)
        pl2 = 'pl2' +'_'+str(i) +'_'+ str(j)
        pl3 = 'pl3'+'_'+str(i) +'_'+ str(j)
        pl4 = 'pl4' +'_'+str(i) +'_'+ str(j) 
        
        CreateArcSector(pl1, center,(center[0]+p/2,center[1],center[2]), angle_off/2)
        CreateArcSector(pl2, center,(center[0]+p/2,center[1],center[2]), -angle_off/2)
        CreateArcSector(pl3, center,(center[0]-p/2,center[1],center[2]), angle_off/2)
        CreateArcSector(pl4, center,(center[0]-p/2,center[1],center[2]), -angle_off/2)
        Unite([pl1,pl2,pl3,pl4])
        Substract('Ring_O'+'_'+str(i) +'_'+ str(j), pl1, True )
        Substract('Ring_I'+'_'+str(i) +'_'+ str(j), pl1)
        Unite(['Ring_O'+'_'+str(i) +'_'+ str(j),'Ring_I'+'_'+str(i) +'_'+ str(j) ])
        
        
    
###==============================================================   





  











    
   

    