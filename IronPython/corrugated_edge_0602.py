# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 21:52:52 2016

@author: LY
"""

x = 3
y = 0.6


pp = []
N = 12

L1 = 9
L2 = 17.2
L3 = 13
DD = 18.6
LL = 4
height = 2   # the length of the step

for i in range(N):
    if(i % 2 == 0):
        pp.append(((i // 2)*(x + y), 0))
        pp.append(((i // 2)*(x + y), height))
    else:
        k = i + 1
        pp.append(((k //2) * (x + y) - x, height))
        pp.append(((k //2) * (x + y) - x, 0))
        



pos = []
pos.append((0, DD/2, L1+L2))


for point in pp:
    pos.append((0, DD/2-point[0], L1+L2+LL+point[1]))
    

pos.append((0, -DD/2, L1+L2))
pos.append((0, DD/2, L1+L2))

print(pos)

oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.SetActiveEditor("3D Modeler")

def CreatePolyline(Points, name, material , unit = 'mm', IsPolylineClosed = False, SolveInside = True, Transparency = 0.7):
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
		["NAME:PolylinePoints"] + [["NAME:PLPoint","X:=", str(point[0]) + unit,	"Y:=", str(point[1]) + unit,"Z:=", str(point[2]) + unit] for point in Points],
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
 


material = 'vacuum'
name = 'Line111'
CreatePolyline(pos, name, material , unit = 'mm', IsPolylineClosed = False, SolveInside = True, Transparency = 0.7)