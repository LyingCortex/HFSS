# ----------------------------------------------
# Script Recorded by Ansoft HFSS Version 15.0.0
# 9:37:02 下午  6月 28, 2016
# ----------------------------------------------
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("WideBeam_SIW_Slot")
oDesign = oProject.SetActiveDesign("wbsiw_Slot")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS1"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "30mm",
		"OriginY:="		, "130mm",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS1"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS1"
	])
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
					"NAME:dc",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "24mm"
				]
			]
		]
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*0",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS1"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "-dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*1",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS2"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*2",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS3"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "-dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*3",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS4"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS2"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS3"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS4"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS1"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*0",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS1"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "-dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*1",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS2"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*2",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS3"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "-dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*3",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS4"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS2"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS3"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS4"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS1"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS2"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS2"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS3"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS3"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS4"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS4"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*0",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS1"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "-dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*1",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS2"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*2",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS3"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "-dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*3",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS4"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS2"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS3"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS4"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
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
					"NAME:slot_w",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.5mm"
				]
			]
		]
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS1"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS2"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS2"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS3"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS3"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS4"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS4"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*0",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS1"
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-slot_w/2",
		"YStart:="		, "-Ls/2",
		"ZStart:="		, "h",
		"Width:="		, "slot_w",
		"Height:="		, "Ls",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "slot1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "-dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*1",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS2"
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-slot_w/2",
		"YStart:="		, "-Ls/2",
		"ZStart:="		, "h",
		"Width:="		, "slot_w",
		"Height:="		, "Ls",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "slot2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*2",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS3"
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-slot_w/2",
		"YStart:="		, "-Ls/2",
		"ZStart:="		, "h",
		"Width:="		, "slot_w",
		"Height:="		, "Ls",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "slot3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "-dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*3",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS4"
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-slot_w/2",
		"YStart:="		, "-Ls/2",
		"ZStart:="		, "h",
		"Width:="		, "slot_w",
		"Height:="		, "Ls",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "slot4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.Rotate(
	[
		"NAME:Selections",
		"Selections:="		, "slot1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:RotateParameters",
		"RotateAxis:="		, "Z",
		"RotateAngle:="		, "5deg"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "slot1,slot2,slot3,slot4"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS1"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS2"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS2"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS3"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS3"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS4"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "RelativeCS4"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*0",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS1"
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-slot_w/2",
		"YStart:="		, "-Ls/2",
		"ZStart:="		, "h",
		"Width:="		, "slot_w",
		"Height:="		, "Ls",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "slot1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.Rotate(
	[
		"NAME:Selections",
		"Selections:="		, "slot1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:RotateParameters",
		"RotateAxis:="		, "Z",
		"RotateAngle:="		, "5deg"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "-dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*1",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS2"
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-slot_w/2",
		"YStart:="		, "-Ls/2",
		"ZStart:="		, "h",
		"Width:="		, "slot_w",
		"Height:="		, "Ls",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "slot2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.Rotate(
	[
		"NAME:Selections",
		"Selections:="		, "slot2",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:RotateParameters",
		"RotateAxis:="		, "Z",
		"RotateAngle:="		, "-5deg"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*2",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS3"
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-slot_w/2",
		"YStart:="		, "-Ls/2",
		"ZStart:="		, "h",
		"Width:="		, "slot_w",
		"Height:="		, "Ls",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "slot3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.Rotate(
	[
		"NAME:Selections",
		"Selections:="		, "slot3",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:RotateParameters",
		"RotateAxis:="		, "Z",
		"RotateAngle:="		, "5deg"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "-dx/2",
		"OriginY:="		, "Lf+Lk+Lp-dc-dy*3",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "1mm",
		"YAxisZvec:="		, "0mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS4"
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-slot_w/2",
		"YStart:="		, "-Ls/2",
		"ZStart:="		, "h",
		"Width:="		, "slot_w",
		"Height:="		, "Ls",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "slot4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.Rotate(
	[
		"NAME:Selections",
		"Selections:="		, "slot4",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:RotateParameters",
		"RotateAxis:="		, "Z",
		"RotateAngle:="		, "-5deg"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Rectangle2"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Rectangle3"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Rectangle4"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS2"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
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
				"NAME:ChangedProps",
				[
					"NAME:dc",
					"Value:="		, "22.1mm"
				]
			]
		]
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS2"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS2"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS3"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS4"
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Patch",
		"Tool Parts:="		, "slot1,slot2,slot3,slot4"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-36mm",
		"YStart:="		, "-59.9mm",
		"ZStart:="		, "0mm",
		"Width:="		, "40mm",
		"Height:="		, "76mm",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.699999988079071,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle2"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Feed"
				],
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 128,
					"B:="			, 0
				],
				[
					"NAME:Color",
					"R:="			, 0,
					"G:="			, 0,
					"B:="			, 255
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Feed:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-10mm",
					"Y:="			, "-59.9mm",
					"Z:="			, "0mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "20mm"
				],
				[
					"NAME:Position",
					"X:="			, "-10mm",
					"Y:="			, "0mm",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Feed:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Coordinate System",
					"Value:="		, "Global"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Feed:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:ZSize",
					"Value:="		, "20mm"
				]
			]
		]
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignWavePort(
	[
		"NAME:1",
		"Objects:="		, ["Feed"],
		"NumModes:="		, 1,
		"RenormalizeAllTerminals:=", True,
		"UseLineModeAlignment:=", False,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, False
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"UseAnalyticAlignment:=", False
	])
oEditor.CreateRegion(
	[
		"NAME:RegionParameters",
		"+XPaddingType:="	, "Percentage Offset",
		"+XPadding:="		, "10",
		"-XPaddingType:="	, "Percentage Offset",
		"-XPadding:="		, "10",
		"+YPaddingType:="	, "Percentage Offset",
		"+YPadding:="		, "10",
		"-YPaddingType:="	, "Percentage Offset",
		"-YPadding:="		, "10",
		"+ZPaddingType:="	, "Percentage Offset",
		"+ZPadding:="		, "10",
		"-ZPaddingType:="	, "Percentage Offset",
		"-ZPadding:="		, "10"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Region",
		"Flags:="		, "Wireframe#",
		"Color:="		, "(255 0 0)",
		"Transparency:="	, 0.699999988079071,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Region:CreateRegion:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:-Y Padding Data",
					"Value:="		, "0"
				],
				[
					"NAME:+Y Padding Data",
					"Value:="		, "30"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Region:CreateRegion:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:+Y Padding Data",
					"Value:="		, "20"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Region:CreateRegion:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:-Z Padding Data",
					"Value:="		, "20"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Region:CreateRegion:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:-Z Padding Data",
					"Value:="		, "40"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Region:CreateRegion:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:-Z Padding Data",
					"Value:="		, "50"
				]
			]
		]
	])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"Frequency:="		, "6GHz",
		"PortsOnly:="		, False,
		"MaxDeltaS:="		, 0.015,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 20,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		"BasisOrder:="		, 1,
		"UseIterativeSolver:="	, False,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"PortAccuracy:="	, 2,
		"UseABCOnPort:="	, False,
		"SetPortMinMaxTri:="	, False,
		"EnableSolverDomains:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"NoAdditionalRefinementOnImport:=", False
	])
oModule.InsertFrequencySweep("Setup1", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"SetupType:="		, "LinearStep",
		"StartValue:="		, "5GHz",
		"StopValue:="		, "7GHz",
		"StepSize:="		, "0.1GHz",
		"Type:="		, "Fast",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"GenerateFieldsForAllFreqs:=", False,
		"ExtrapToDC:="		, False
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["Region"],
		"IsIncidentField:="	, False,
		"IsEnforcedField:="	, False,
		"IsFssReference:="	, False,
		"IsForPML:="		, False,
		"UseAdaptiveIE:="	, False,
		"IncludeInPostproc:="	, True
	])
oProject.Save()
oDesign.AnalyzeAll()
oProject.Save()
