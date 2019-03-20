# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:48:45 2017

@author: LY
"""

'''
DuplicateAlongLine(name, direction, NumClones, unit = 'mm')
沿直线复制选中的物体，输入物体名称，复制的方向，复制的个数（包括当前的物体），方向矢量的单位
'''
def DuplicateAlongLine(oEditor, name, direction, NumClones, unit = 'mm', CreateNewObjects = True):
    oEditor.DuplicateAlongLine(
	[
		"NAME:Selections",
		"Selections:="		, name,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToAlongLineParameters",
		"CreateNewObjects:="	, CreateNewObjects,
		"XComponent:="		, [str(direction[0]) + unit  if type(direction[0]) != type('a') else direction[0]][0],
		"YComponent:="		, [str(direction[1]) + unit  if type(direction[1]) != type('a') else direction[1]][0],
		"ZComponent:="		, [str(direction[2]) + unit  if type(direction[2]) != type('a') else direction[2]][0],
		"NumClones:="		, str(NumClones)
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	])

	
	
def DuplicateAroundAxis(oEditor, name, RotateAngle, num, unit = 'deg', WhichAxis='Z', CreateNewObjects=False):
    oEditor.DuplicateAroundAxis(
	[
		"NAME:Selections",
		"Selections:="		, name,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateAroundAxisParameters",
		"CreateNewObjects:="	, CreateNewObjects,
		"WhichAxis:="		, WhichAxis,
		"AngleStr:="		, [str(RotateAngle) + unit if type(RotateAngle) != type('a') else RotateAngle][0],
		"NumClones:="		, str(num)
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	])

	
def DuplicateMirror(oEditor, name_array, Base, Normal, unit = 'mm' ):
    if type(name_array)==type('a'):
        name_array_str = name_array
    else:
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


	
def Intersect(oEditor, name_array, KeepOriginals=False):
    name_array_str = ''
    for s in name_array:
        name_array_str += s
        name_array_str += ','
    name_array_str =name_array_str[0:-1]
    oEditor.Intersect(
	[
		"NAME:Selections",
		"Selections:="		, name_array_str
	], 
	[
		"NAME:IntersectParameters",
		"KeepOriginals:="	, KeepOriginals
	])
	
	
'''
mirror  ,not duplicate

'''    
def Mirror(oEditor, name, Base, Normal, unit = 'mm'):
    oEditor.Mirror(
	[
		"NAME:Selections",
		"Selections:="		, name,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:MirrorParameters",
		"MirrorBaseX:="		,[str(Base[0]) + unit if type(Base[0]) != type('a') else Base[0]][0],
		"MirrorBaseY:="		,[str(Base[1]) + unit if type(Base[1]) != type('a') else Base[1]][0],
		"MirrorBaseZ:="		, [str(Base[2]) + unit if type(Base[2]) != type('a') else Base[2]][0],
		"MirrorNormalX:="	, [str(Normal[0]) + unit if type(Normal[0]) != type('a') else Normal[0]][0],
		"MirrorNormalY:="	, [str(Normal[1]) + unit if type(Normal[1]) != type('a') else Normal[1]][0],
		"MirrorNormalZ:="	, [str(Normal[2]) + unit if type(Normal[2]) != type('a') else Normal[2]][0]
	])

	
def Move(oEditor, name, direction, unit = 'mm'):
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
	
	
def Rotate( oEditor, name, RotateAngle, unit = 'deg', RotateAxis = 'Z'):
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





'''
Roteate around axis
'''

def RotateAroundAxis(oEditor, name, RotateAngle, num, unit = 'deg', WhichAxis='Z', CreateNewObjects=False):
    oEditor.DuplicateAroundAxis(
	[
		"NAME:Selections",
		"Selections:="		, name,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateAroundAxisParameters",
		"CreateNewObjects:="	, CreateNewObjects,
		"WhichAxis:="		, WhichAxis,
		"AngleStr:="		, [str(RotateAngle) + unit if type(RotateAngle) != type('a') else RotateAngle][0],
		"NumClones:="		, str(num)
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	])
###===	
	
'''
set working coordinate system
'''
def SetWCS(oEditor, name = 'Global'):
    oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", name
	])
 
 
 
 
'''
split
'''
def Split(oEditor, name, SplitPlane='ZX',	WhichSide="PositiveOnly" , DeleteInvalidObjects=True):
    oEditor.Split(
	[
		"NAME:Selections",
		"Selections:="		, name,
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:SplitToParameters",
		"SplitPlane:="		, SplitPlane,
		"WhichSide:="		, WhichSide,
		"SplitCrossingObjectsOnly:=", (not DeleteInvalidObjects),
		"DeleteInvalidObjects:=", DeleteInvalidObjects
	])

	
'''
Tool_Parts   "slot1,slot2,slot3,slot4"
'''
def Substract(oEditor, Blank_Parts, Tool_Parts, KeepOriginals=False ):
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

	
def SweepAlongVector(oEditor, name, sweep_vec,unit = 'mm'):
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

	
def Unite(oEditor, name_array):
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
	
