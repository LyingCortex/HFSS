# ----------------------------------------------
# Script Recorded by Ansoft HFSS Version 15.0.0
# 9:28:58 上午  9月 06, 2016
# ----------------------------------------------
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Sustrate_change_0905")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-2mm",
		"YCenter:="		, "-1mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "0.5mm",
		"Height:="		, "1mm",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Cylinder1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.699999988079071,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.DuplicateAlongLine(
	[
		"NAME:Selections",
		"Selections:="		, "Cylinder1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToAlongLineParameters",
		"CreateNewObjects:="	, True,
		"XComponent:="		, "1mm",
		"YComponent:="		, "3mm",
		"ZComponent:="		, "2mm",
		"NumClones:="		, "3"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	])
oEditor.DuplicateAlongLine(
	[
		"NAME:Selections",
		"Selections:="		, "Cylinder1,Cylinder1_1,Cylinder1_2",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToAlongLineParameters",
		"CreateNewObjects:="	, True,
		"XComponent:="		, "2mm",
		"YComponent:="		, "3mm",
		"ZComponent:="		, "1mm",
		"NumClones:="		, "2"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	])
oDesign = oProject.SetActiveDesign("Horn")
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
					"NAME:DD",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "8mm"
				]
			]
		]
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
					"NAME:N2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "15"
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_1_1,via_L1_2,via_L1_2_1,via_L1_3,via_L1_3_1,via_L1_4,via_L1_4_1,via_L1_5,via_L1_5_1,via_L1_6,via_L1_6_1,via_L1_7,via_L1_7_1,via_L1_8,via_L1_8_1,via_L1_9,via_L1_9_1,via_L1_10,via_L1_10_1,via_L1_11,via_L1_11_1"
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+0*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+1*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+2*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+3*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+4*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+5*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+6*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+7*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+8*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+9*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+10*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*1",
		"YCenter:="		, "d/2+0*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*2",
		"YCenter:="		, "d/2+1*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*3",
		"YCenter:="		, "d/2+2*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*4",
		"YCenter:="		, "d/2+3*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*5",
		"YCenter:="		, "d/2+4*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*6",
		"YCenter:="		, "d/2+5*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*7",
		"YCenter:="		, "d/2+6*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*8",
		"YCenter:="		, "d/2+7*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*9",
		"YCenter:="		, "d/2+8*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*10",
		"YCenter:="		, "d/2+9*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*11",
		"YCenter:="		, "d/2+10*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*12",
		"YCenter:="		, "d/2+11*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_12",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*13",
		"YCenter:="		, "d/2+12*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_13",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*14",
		"YCenter:="		, "d/2+13*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_14",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*15",
		"YCenter:="		, "d/2+14*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_15",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_2,via_L1_3,via_L1_4,via_L1_5,via_L1_6,via_L1_7,via_L1_8,via_L1_9,via_L1_10,via_L1_11,via_L2_1,via_L2_2,via_L2_3,via_L2_4,via_L2_5,via_L2_6,via_L2_7,via_L2_8,via_L2_9,via_L2_10,via_L2_11,via_L2_12,via_L2_13,via_L2_14,via_L2_15"
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+0*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+1*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+2*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+3*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+4*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+5*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+6*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+7*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+8*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+9*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+10*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*1",
		"YCenter:="		, "d/2+p*11+0*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*2",
		"YCenter:="		, "d/2+p*11+1*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*3",
		"YCenter:="		, "d/2+p*11+2*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*4",
		"YCenter:="		, "d/2+p*11+3*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*5",
		"YCenter:="		, "d/2+p*11+4*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*6",
		"YCenter:="		, "d/2+p*11+5*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*7",
		"YCenter:="		, "d/2+p*11+6*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*8",
		"YCenter:="		, "d/2+p*11+7*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*9",
		"YCenter:="		, "d/2+p*11+8*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*10",
		"YCenter:="		, "d/2+p*11+9*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*11",
		"YCenter:="		, "d/2+p*11+10*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*12",
		"YCenter:="		, "d/2+p*11+11*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_12",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*13",
		"YCenter:="		, "d/2+p*11+12*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_13",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*14",
		"YCenter:="		, "d/2+p*11+13*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_14",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-(DD-a-d/2)/N2*15",
		"YCenter:="		, "d/2+p*11+14*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_15",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
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
					"NAME:DD",
					"Value:="		, "14mm"
				]
			]
		]
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_2,via_L1_3,via_L1_4,via_L1_5,via_L1_6,via_L1_7,via_L1_8,via_L1_9,via_L1_10,via_L1_11,via_L2_1,via_L2_2,via_L2_3,via_L2_4,via_L2_5,via_L2_6,via_L2_7,via_L2_8,via_L2_9,via_L2_10,via_L2_11,via_L2_12,via_L2_13,via_L2_14,via_L2_15"
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+0*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+1*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+2*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+3*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+4*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+5*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+6*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+7*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+8*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+9*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+10*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*1",
		"YCenter:="		, "d/2+p*11+0*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*2",
		"YCenter:="		, "d/2+p*11+1*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*3",
		"YCenter:="		, "d/2+p*11+2*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*4",
		"YCenter:="		, "d/2+p*11+3*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*5",
		"YCenter:="		, "d/2+p*11+4*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*6",
		"YCenter:="		, "d/2+p*11+5*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*7",
		"YCenter:="		, "d/2+p*11+6*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*8",
		"YCenter:="		, "d/2+p*11+7*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*9",
		"YCenter:="		, "d/2+p*11+8*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*10",
		"YCenter:="		, "d/2+p*11+9*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*11",
		"YCenter:="		, "d/2+p*11+10*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*12",
		"YCenter:="		, "d/2+p*11+11*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_12",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*13",
		"YCenter:="		, "d/2+p*11+12*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_13",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*14",
		"YCenter:="		, "d/2+p*11+13*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_14",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*15",
		"YCenter:="		, "d/2+p*11+14*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_15",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
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
					"NAME:N2",
					"Value:="		, "13"
				]
			]
		]
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_2,via_L1_3,via_L1_4,via_L1_5,via_L1_6,via_L1_7,via_L1_8,via_L1_9,via_L1_10,via_L1_11,via_L2_1,via_L2_2,via_L2_3,via_L2_4,via_L2_5,via_L2_6,via_L2_7,via_L2_8,via_L2_9,via_L2_10,via_L2_11,via_L2_12,via_L2_13,via_L2_14,via_L2_15"
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+0*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+1*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+2*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+3*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+4*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+5*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+6*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+7*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+8*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+9*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+10*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*1",
		"YCenter:="		, "d/2+p*11+0*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*2",
		"YCenter:="		, "d/2+p*11+1*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*3",
		"YCenter:="		, "d/2+p*11+2*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*4",
		"YCenter:="		, "d/2+p*11+3*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*5",
		"YCenter:="		, "d/2+p*11+4*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*6",
		"YCenter:="		, "d/2+p*11+5*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*7",
		"YCenter:="		, "d/2+p*11+6*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*8",
		"YCenter:="		, "d/2+p*11+7*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*9",
		"YCenter:="		, "d/2+p*11+8*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*10",
		"YCenter:="		, "d/2+p*11+9*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*11",
		"YCenter:="		, "d/2+p*11+10*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*12",
		"YCenter:="		, "d/2+p*11+11*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_12",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*13",
		"YCenter:="		, "d/2+p*11+12*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_13",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_2,via_L1_3,via_L1_4,via_L1_5,via_L1_6,via_L1_7,via_L1_8,via_L1_9,via_L1_10,via_L1_11,via_L2_1,via_L2_2,via_L2_3,via_L2_4,via_L2_5,via_L2_6,via_L2_7,via_L2_8,via_L2_9,via_L2_10,via_L2_11,via_L2_12,via_L2_13"
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
				"NAME:DeletedProps", 
				"p"
			]
		]
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
					"NAME:p",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"DD"
			]
		]
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
					"NAME:DD",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "14mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L1"
			]
		]
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
					"NAME:L1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L2"
			]
		]
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
					"NAME:L2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"a"
			]
		]
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
					"NAME:a",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "5mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"d"
			]
		]
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
					"NAME:d",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.8mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N2"
			]
		]
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
					"NAME:N2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10"
				]
			]
		]
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
					"NAME:N1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "11"
				]
			]
		]
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+0*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+1*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+2*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+3*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+4*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+5*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+6*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+7*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+8*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+9*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+10*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*1",
		"YCenter:="		, "d/2+p*11+0*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*2",
		"YCenter:="		, "d/2+p*11+1*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*3",
		"YCenter:="		, "d/2+p*11+2*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*4",
		"YCenter:="		, "d/2+p*11+3*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*5",
		"YCenter:="		, "d/2+p*11+4*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*6",
		"YCenter:="		, "d/2+p*11+5*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*7",
		"YCenter:="		, "d/2+p*11+6*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*8",
		"YCenter:="		, "d/2+p*11+7*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*9",
		"YCenter:="		, "d/2+p*11+8*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*10",
		"YCenter:="		, "d/2+p*11+9*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oProject.CopyDesign("Horn")
oProject.Paste()
oProject.DeleteDesign("Horn")
oDesign = oProject.SetActiveDesign("Horn1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_2,via_L1_3,via_L1_4,via_L1_5,via_L1_6,via_L1_7,via_L1_8,via_L1_9,via_L1_10,via_L1_11,via_L2_1,via_L2_2,via_L2_3,via_L2_4,via_L2_5,via_L2_6,via_L2_7,via_L2_8,via_L2_9,via_L2_10"
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
				"NAME:DeletedProps", 
				"p"
			]
		]
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
					"NAME:p",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"DD"
			]
		]
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
					"NAME:DD",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "14mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L1"
			]
		]
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
					"NAME:L1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L2"
			]
		]
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
					"NAME:L2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"a"
			]
		]
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
					"NAME:a",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "5mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"d"
			]
		]
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
					"NAME:d",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.8mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N2"
			]
		]
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
					"NAME:N2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N1"
			]
		]
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
					"NAME:N1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "11"
				]
			]
		]
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+0*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+1*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+2*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+3*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+4*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+5*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+6*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+7*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+8*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+9*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+10*p",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*1",
		"YCenter:="		, "d/2+p*11+0*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*2",
		"YCenter:="		, "d/2+p*11+1*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*3",
		"YCenter:="		, "d/2+p*11+2*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*4",
		"YCenter:="		, "d/2+p*11+3*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*5",
		"YCenter:="		, "d/2+p*11+4*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*6",
		"YCenter:="		, "d/2+p*11+5*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*7",
		"YCenter:="		, "d/2+p*11+6*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*8",
		"YCenter:="		, "d/2+p*11+7*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*9",
		"YCenter:="		, "d/2+p*11+8*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*10",
		"YCenter:="		, "d/2+p*11+9*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.DuplicateMirror(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_2,via_L1_3,via_L1_4,via_L1_5,via_L1_6,via_L1_7,via_L1_8,via_L1_9,via_L1_10,via_L1_11,via_L2_1,via_L2_2,via_L2_3,via_L2_4,via_L2_5,via_L2_6,via_L2_7,via_L2_8,via_L2_9,via_L2_10",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToMirrorParameters",
		"DuplicateMirrorBaseX:=", "0mm",
		"DuplicateMirrorBaseY:=", "0mm",
		"DuplicateMirrorBaseZ:=", "0mm",
		"DuplicateMirrorNormalX:=", "1mm",
		"DuplicateMirrorNormalY:=", "0mm",
		"DuplicateMirrorNormalZ:=", "0mm"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", "true"
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
					"NAME:Width",
					"Value:="		, "DD"
				]
			]
		]
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
					"NAME:Width",
					"Value:="		, "DD+1mm"
				]
			]
		]
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
					"NAME:L3",
					"Value:="		, "8mm"
				]
			]
		]
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
					"NAME:Len",
					"Value:="		, "L1+L2+L3+d/2"
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-8mm",
		"YStart:="		, "-1mm",
		"ZStart:="		, "0mm",
		"Width:="		, "15mm",
		"Height:="		, "27mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.699999988079071,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Rectangle1"
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-7.5mm",
		"YStart:="		, "0mm",
		"ZStart:="		, "2.5mm",
		"Width:="		, "15.5mm",
		"Height:="		, "20mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
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
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Top"
				],
				[
					"NAME:Color",
					"R:="			, 128,
					"G:="			, 128,
					"B:="			, 0
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
				"Top:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-Width/2",
					"Y:="			, "0mm",
					"Z:="			, "b"
				],
				[
					"NAME:XSize",
					"Value:="		, "Width"
				],
				[
					"NAME:YSize",
					"Value:="		, "L1+L2 +d/2"
				]
			]
		]
	])
oEditor.DuplicateAlongLine(
	[
		"NAME:Selections",
		"Selections:="		, "Top",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToAlongLineParameters",
		"CreateNewObjects:="	, True,
		"XComponent:="		, "0mm",
		"YComponent:="		, "0mm",
		"ZComponent:="		, "-2.5mm",
		"NumClones:="		, "2"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Top:DuplicateAlongLine:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Vector",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "-b"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Top_1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "GND"
				]
			]
		]
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignPerfectE(
	[
		"NAME:PerfE1",
		"Objects:="		, ["GND","Top"],
		"InfGroundPlane:="	, False
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-2mm",
		"YStart:="		, "0mm",
		"ZStart:="		, "0mm",
		"Width:="		, "4mm",
		"Height:="		, "1mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
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
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Port"
				],
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 128,
					"B:="			, 0
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
				"Port:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-a/2+d/2",
					"Y:="			, "0mm",
					"Z:="			, "0mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "a-d"
				],
				[
					"NAME:YSize",
					"Value:="		, "b"
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
				"Port:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Axis",
					"Value:="		, "Y"
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
				"Port:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "a-d"
				],
				[
					"NAME:ZSize",
					"Value:="		, "b"
				]
			]
		]
	])
oModule.AssignWavePort(
	[
		"NAME:1",
		"Objects:="		, ["Port"],
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
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"Frequency:="		, "27GHz",
		"PortsOnly:="		, False,
		"MaxDeltaS:="		, 0.02,
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
		"StartValue:="		, "22GHz",
		"StopValue:="		, "32GHz",
		"StepSize:="		, "0.1GHz",
		"Type:="		, "Fast",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"GenerateFieldsForAllFreqs:=", False,
		"ExtrapToDC:="		, False
	])
oProject.Save()
oDesign.AnalyzeAll()
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("XY Plot 1", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"L3:="			, ["Nominal"],
		"b:="			, ["Nominal"],
		"p:="			, ["Nominal"],
		"DD:="			, ["Nominal"],
		"L1:="			, ["Nominal"],
		"L2:="			, ["Nominal"],
		"a:="			, ["Nominal"],
		"d:="			, ["Nominal"],
		"N2:="			, ["Nominal"],
		"N1:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(S(1,1))"]
	], [])
oModule = oDesign.GetModule("Optimetrics")
oModule.InsertSetup("OptiParametric", 
	[
		"NAME:ParametricSetup1",
		"IsEnabled:="		, True,
		[
			"NAME:ProdOptiSetupData",
			"SaveFields:="		, False,
			"CopyMesh:="		, False
		],
		[
			"NAME:StartingPoint"
		],
		"Sim. Setups:="		, ["Setup1"],
		[
			"NAME:Sweeps",
			[
				"NAME:SweepDefinition",
				"Variable:="		, "a",
				"Data:="		, "LIN 4.5mm 5.4mm 0.2mm",
				"OffsetF1:="		, False,
				"Synchronize:="		, 0
			]
		],
		[
			"NAME:Sweep Operations"
		],
		[
			"NAME:Goals"
		]
	])
oModule.RenameSetup("ParametricSetup1", "a")
oProject.Save()
oModule.SolveSetup("a")
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("XY Plot 2", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"L3:="			, ["Nominal"],
		"b:="			, ["Nominal"],
		"p:="			, ["Nominal"],
		"DD:="			, ["Nominal"],
		"L1:="			, ["Nominal"],
		"L2:="			, ["Nominal"],
		"a:="			, ["All"],
		"d:="			, ["Nominal"],
		"N2:="			, ["Nominal"],
		"N1:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(S(1,1))"]
	], [])
oProject.CopyDesign("Horn1")
oProject.Paste()
oDesign = oProject.SetActiveDesign("Horn2")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_1_1,via_L1_2,via_L1_2_1,via_L1_3,via_L1_3_1,via_L1_4,via_L1_4_1,via_L1_5,via_L1_5_1,via_L1_6,via_L1_6_1,via_L1_7,via_L1_7_1,via_L1_8,via_L1_8_1,via_L1_9,via_L1_9_1,via_L1_10,via_L1_10_1,via_L1_11,via_L1_11_1,via_L2_1,via_L2_1_1,via_L2_2,via_L2_2_1,via_L2_3,via_L2_3_1,via_L2_4,via_L2_4_1,via_L2_5,via_L2_5_1,via_L2_6,via_L2_6_1,via_L2_7,via_L2_7_1,via_L2_8,via_L2_8_1,via_L2_9,via_L2_9_1,via_L2_10,via_L2_10_1"
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
				"NAME:DeletedProps", 
				"p"
			]
		]
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
					"NAME:p",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"DD"
			]
		]
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
					"NAME:DD",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "14mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L1"
			]
		]
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
					"NAME:L1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L2"
			]
		]
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
					"NAME:L2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"a"
			]
		]
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
					"NAME:a",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "5mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"d"
			]
		]
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
					"NAME:d",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.8mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N2"
			]
		]
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
					"NAME:N2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N1"
			]
		]
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
					"NAME:N1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "11"
				]
			]
		]
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "0mm",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*1",
		"YCenter:="		, "d/2+p*11+0*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*2",
		"YCenter:="		, "d/2+p*11+1*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*3",
		"YCenter:="		, "d/2+p*11+2*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*4",
		"YCenter:="		, "d/2+p*11+3*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*5",
		"YCenter:="		, "d/2+p*11+4*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*6",
		"YCenter:="		, "d/2+p*11+5*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*7",
		"YCenter:="		, "d/2+p*11+6*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*8",
		"YCenter:="		, "d/2+p*11+7*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*9",
		"YCenter:="		, "d/2+p*11+8*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*10",
		"YCenter:="		, "d/2+p*11+9*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.DuplicateMirror(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_2,via_L1_3,via_L1_4,via_L1_5,via_L1_6,via_L1_7,via_L1_8,via_L1_9,via_L1_10,via_L1_11,via_L2_1,via_L2_2,via_L2_3,via_L2_4,via_L2_5,via_L2_6,via_L2_7,via_L2_8,via_L2_9,via_L2_10",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToMirrorParameters",
		"DuplicateMirrorBaseX:=", "0mm",
		"DuplicateMirrorBaseY:=", "0mm",
		"DuplicateMirrorBaseZ:=", "0mm",
		"DuplicateMirrorNormalX:=", "1mm",
		"DuplicateMirrorNormalY:=", "0mm",
		"DuplicateMirrorNormalZ:=", "0mm"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", "true"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_1_1,via_L1_2,via_L1_2_1,via_L1_3,via_L1_3_1,via_L1_4,via_L1_4_1,via_L1_5,via_L1_5_1,via_L1_6,via_L1_6_1,via_L1_7,via_L1_7_1,via_L1_8,via_L1_8_1,via_L1_9,via_L1_9_1,via_L1_10,via_L1_10_1,via_L1_11,via_L1_11_1,via_L2_1,via_L2_1_1,via_L2_2,via_L2_2_1,via_L2_3,via_L2_3_1,via_L2_4,via_L2_4_1,via_L2_5,via_L2_5_1,via_L2_6,via_L2_6_1,via_L2_7,via_L2_7_1,via_L2_8,via_L2_8_1,via_L2_9,via_L2_9_1,via_L2_10,via_L2_10_1"
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
				"NAME:DeletedProps", 
				"p"
			]
		]
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
					"NAME:p",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"DD"
			]
		]
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
					"NAME:DD",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "14mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L1"
			]
		]
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
					"NAME:L1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L2"
			]
		]
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
					"NAME:L2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"a"
			]
		]
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
					"NAME:a",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "5mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"d"
			]
		]
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
					"NAME:d",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.8mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N2"
			]
		]
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
					"NAME:N2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N1"
			]
		]
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
					"NAME:N1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "11"
				]
			]
		]
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+0*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+1*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+2*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+3*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+4*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+5*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+6*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+7*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+8*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+9*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+10*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*1",
		"YCenter:="		, "d/2+p*11+0*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*2",
		"YCenter:="		, "d/2+p*11+1*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*3",
		"YCenter:="		, "d/2+p*11+2*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*4",
		"YCenter:="		, "d/2+p*11+3*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*5",
		"YCenter:="		, "d/2+p*11+4*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*6",
		"YCenter:="		, "d/2+p*11+5*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*7",
		"YCenter:="		, "d/2+p*11+6*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*8",
		"YCenter:="		, "d/2+p*11+7*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*9",
		"YCenter:="		, "d/2+p*11+8*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*10",
		"YCenter:="		, "d/2+p*11+9*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.DuplicateMirror(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_2,via_L1_3,via_L1_4,via_L1_5,via_L1_6,via_L1_7,via_L1_8,via_L1_9,via_L1_10,via_L1_11,via_L2_1,via_L2_2,via_L2_3,via_L2_4,via_L2_5,via_L2_6,via_L2_7,via_L2_8,via_L2_9,via_L2_10",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToMirrorParameters",
		"DuplicateMirrorBaseX:=", "0mm",
		"DuplicateMirrorBaseY:=", "0mm",
		"DuplicateMirrorBaseZ:=", "0mm",
		"DuplicateMirrorNormalX:=", "1mm",
		"DuplicateMirrorNormalY:=", "0mm",
		"DuplicateMirrorNormalZ:=", "0mm"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", "true"
	])
oProject.CopyDesign("Horn2")
oProject.Paste()
oProject.DeleteDesign("Horn2")
oDesign = oProject.SetActiveDesign("Horn3")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_1_1,via_L1_2,via_L1_2_1,via_L1_3,via_L1_3_1,via_L1_4,via_L1_4_1,via_L1_5,via_L1_5_1,via_L1_6,via_L1_6_1,via_L1_7,via_L1_7_1,via_L1_8,via_L1_8_1,via_L1_9,via_L1_9_1,via_L1_10,via_L1_10_1,via_L1_11,via_L1_11_1,via_L2_1,via_L2_1_1,via_L2_2,via_L2_2_1,via_L2_3,via_L2_3_1,via_L2_4,via_L2_4_1,via_L2_5,via_L2_5_1,via_L2_6,via_L2_6_1,via_L2_7,via_L2_7_1,via_L2_8,via_L2_8_1,via_L2_9,via_L2_9_1,via_L2_10,via_L2_10_1"
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
				"NAME:DeletedProps", 
				"p"
			]
		]
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
					"NAME:p",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"DD"
			]
		]
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
					"NAME:DD",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "14mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L1"
			]
		]
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
					"NAME:L1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L2"
			]
		]
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
					"NAME:L2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"a"
			]
		]
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
					"NAME:a",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "5mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"d"
			]
		]
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
					"NAME:d",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.8mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N2"
			]
		]
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
					"NAME:N2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N1"
			]
		]
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
					"NAME:N1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "11"
				]
			]
		]
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+0*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+1*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+2*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+3*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+4*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+5*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+6*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+7*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+8*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+9*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+10*L1/N1",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*1",
		"YCenter:="		, "d/2+L1+0*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*2",
		"YCenter:="		, "d/2+L1+1*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*3",
		"YCenter:="		, "d/2+L1+2*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*4",
		"YCenter:="		, "d/2+L1+3*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*5",
		"YCenter:="		, "d/2+L1+4*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*6",
		"YCenter:="		, "d/2+L1+5*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*7",
		"YCenter:="		, "d/2+L1+6*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*8",
		"YCenter:="		, "d/2+L1+7*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*9",
		"YCenter:="		, "d/2+L1+8*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*10",
		"YCenter:="		, "d/2+L1+9*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.DuplicateMirror(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_2,via_L1_3,via_L1_4,via_L1_5,via_L1_6,via_L1_7,via_L1_8,via_L1_9,via_L1_10,via_L1_11,via_L2_1,via_L2_2,via_L2_3,via_L2_4,via_L2_5,via_L2_6,via_L2_7,via_L2_8,via_L2_9,via_L2_10",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToMirrorParameters",
		"DuplicateMirrorBaseX:=", "0mm",
		"DuplicateMirrorBaseY:=", "0mm",
		"DuplicateMirrorBaseZ:=", "0mm",
		"DuplicateMirrorNormalX:=", "1mm",
		"DuplicateMirrorNormalY:=", "0mm",
		"DuplicateMirrorNormalZ:=", "0mm"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", "true"
	])
oProject.CopyDesign("Horn3")
oProject.Paste()
oDesign = oProject.SetActiveDesign("Horn4")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "via_L2_10_1,via_L1_1,via_L1_1_1,via_L1_2,via_L1_2_1,via_L1_3,via_L1_3_1,via_L1_4,via_L1_4_1,via_L1_5,via_L1_5_1,via_L1_6,via_L1_6_1,via_L1_7,via_L1_7_1,via_L1_8,via_L1_8_1,via_L1_9,via_L1_9_1,via_L1_10,via_L1_10_1,via_L1_11,via_L1_11_1,via_L2_1,via_L2_1_1,via_L2_2,via_L2_2_1,via_L2_3,via_L2_3_1,via_L2_4,via_L2_4_1,via_L2_5,via_L2_5_1,via_L2_6,via_L2_6_1,via_L2_7,via_L2_7_1,via_L2_8,via_L2_8_1,via_L2_9,via_L2_9_1,via_L2_10"
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
				"NAME:DeletedProps", 
				"p"
			]
		]
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
					"NAME:p",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"DD"
			]
		]
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
					"NAME:DD",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "14mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L1"
			]
		]
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
					"NAME:L1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L2"
			]
		]
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
					"NAME:L2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"a"
			]
		]
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
					"NAME:a",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "5mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"d"
			]
		]
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
					"NAME:d",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.8mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N2"
			]
		]
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
					"NAME:N2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N1"
			]
		]
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
					"NAME:N1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "11"
				]
			]
		]
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+0*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+1*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+2*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+3*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+4*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+5*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+6*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+7*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+8*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+9*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+10*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*1",
		"YCenter:="		, "d/2+L1+0*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*2",
		"YCenter:="		, "d/2+L1+1*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*3",
		"YCenter:="		, "d/2+L1+2*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*4",
		"YCenter:="		, "d/2+L1+3*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*5",
		"YCenter:="		, "d/2+L1+4*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*6",
		"YCenter:="		, "d/2+L1+5*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*7",
		"YCenter:="		, "d/2+L1+6*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*8",
		"YCenter:="		, "d/2+L1+7*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*9",
		"YCenter:="		, "d/2+L1+8*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*10",
		"YCenter:="		, "d/2+L1+9*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.DuplicateMirror(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_2,via_L1_3,via_L1_4,via_L1_5,via_L1_6,via_L1_7,via_L1_8,via_L1_9,via_L1_10,via_L1_11,via_L2_1,via_L2_2,via_L2_3,via_L2_4,via_L2_5,via_L2_6,via_L2_7,via_L2_8,via_L2_9,via_L2_10",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToMirrorParameters",
		"DuplicateMirrorBaseX:=", "0mm",
		"DuplicateMirrorBaseY:=", "0mm",
		"DuplicateMirrorBaseZ:=", "0mm",
		"DuplicateMirrorNormalX:=", "1mm",
		"DuplicateMirrorNormalY:=", "0mm",
		"DuplicateMirrorNormalZ:=", "0mm"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", "true"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_1_1,via_L1_2,via_L1_2_1,via_L1_3,via_L1_3_1,via_L1_4,via_L1_4_1,via_L1_5,via_L1_5_1,via_L1_6,via_L1_6_1,via_L1_7,via_L1_7_1,via_L1_8,via_L1_8_1,via_L1_9,via_L1_9_1,via_L1_10,via_L1_10_1,via_L1_11,via_L1_11_1,via_L2_1,via_L2_1_1,via_L2_2,via_L2_2_1,via_L2_3,via_L2_3_1,via_L2_4,via_L2_4_1,via_L2_5,via_L2_5_1,via_L2_6,via_L2_6_1,via_L2_7,via_L2_7_1,via_L2_8,via_L2_8_1,via_L2_9,via_L2_9_1,via_L2_10,via_L2_10_1"
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
				"NAME:DeletedProps", 
				"p"
			]
		]
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
					"NAME:p",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"DD"
			]
		]
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
					"NAME:DD",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "14mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L1"
			]
		]
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
					"NAME:L1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L2"
			]
		]
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
					"NAME:L2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"a"
			]
		]
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
					"NAME:a",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "5mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"d"
			]
		]
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
					"NAME:d",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.8mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N2"
			]
		]
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
					"NAME:N2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N1"
			]
		]
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
					"NAME:N1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "11"
				]
			]
		]
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+0*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+1*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+2*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+3*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+4*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+5*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+6*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+7*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+8*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+9*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+10*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*1",
		"YCenter:="		, "d/2+L1+1*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*2",
		"YCenter:="		, "d/2+L1+2*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*3",
		"YCenter:="		, "d/2+L1+3*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*4",
		"YCenter:="		, "d/2+L1+4*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*5",
		"YCenter:="		, "d/2+L1+5*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*6",
		"YCenter:="		, "d/2+L1+6*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*7",
		"YCenter:="		, "d/2+L1+7*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*8",
		"YCenter:="		, "d/2+L1+8*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*9",
		"YCenter:="		, "d/2+L1+9*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*10",
		"YCenter:="		, "d/2+L1+10*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.DuplicateMirror(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_2,via_L1_3,via_L1_4,via_L1_5,via_L1_6,via_L1_7,via_L1_8,via_L1_9,via_L1_10,via_L1_11,via_L2_1,via_L2_2,via_L2_3,via_L2_4,via_L2_5,via_L2_6,via_L2_7,via_L2_8,via_L2_9,via_L2_10",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToMirrorParameters",
		"DuplicateMirrorBaseX:=", "0mm",
		"DuplicateMirrorBaseY:=", "0mm",
		"DuplicateMirrorBaseZ:=", "0mm",
		"DuplicateMirrorNormalX:=", "1mm",
		"DuplicateMirrorNormalY:=", "0mm",
		"DuplicateMirrorNormalZ:=", "0mm"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", "true"
	])
oProject.Save()
oDesign = oProject.SetActiveDesign("Horn3")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "via_L2_10"
	])
oModule = oDesign.GetModule("Optimetrics")
oModule.DeleteSetups(["a"])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditFrequencySweep("Setup1", "Sweep", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"SetupType:="		, "LinearStep",
		"StartValue:="		, "20GHz",
		"StopValue:="		, "32GHz",
		"StepSize:="		, "0.1GHz",
		"Type:="		, "Fast",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"GenerateFieldsForAllFreqs:=", False,
		"ExtrapToDC:="		, False
	])
oDesign = oProject.SetActiveDesign("Horn4")
oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditFrequencySweep("Setup1", "Sweep", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"SetupType:="		, "LinearStep",
		"StartValue:="		, "20GHz",
		"StopValue:="		, "32GHz",
		"StepSize:="		, "0.1GHz",
		"Type:="		, "Fast",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"GenerateFieldsForAllFreqs:=", False,
		"ExtrapToDC:="		, False
	])
oModule = oDesign.GetModule("Optimetrics")
oModule.DeleteSetups(["a"])
oModule.InsertSetup("OptiParametric", 
	[
		"NAME:ParametricSetup1",
		"IsEnabled:="		, True,
		[
			"NAME:ProdOptiSetupData",
			"SaveFields:="		, False,
			"CopyMesh:="		, False
		],
		[
			"NAME:StartingPoint"
		],
		"Sim. Setups:="		, ["Setup1"],
		[
			"NAME:Sweeps",
			[
				"NAME:SweepDefinition",
				"Variable:="		, "L1",
				"Data:="		, "LIN 9mm 15mm 1mm",
				"OffsetF1:="		, False,
				"Synchronize:="		, 0
			]
		],
		[
			"NAME:Sweep Operations"
		],
		[
			"NAME:Goals"
		]
	])
oModule.RenameSetup("ParametricSetup1", "L1")
oProject.Save()
oModule.SolveSetup("L1")
oDesign = oProject.SetActiveDesign("Horn1")
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
					"NAME:Lambda",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "300mm/27"
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-12mm",
		"YPosition:="		, "-4mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "22mm",
		"YSize:="		, "42mm",
		"ZSize:="		, "-8mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
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
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Box1:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-Width/2 + Lambda/4",
					"Y:="			, "0mm",
					"Z:="			, "-Lambda/4"
				],
				[
					"NAME:XSize",
					"Value:="		, "Width+Lambda/2"
				],
				[
					"NAME:YSize",
					"Value:="		, "Len + Lambda/2"
				],
				[
					"NAME:ZSize",
					"Value:="		, "Lambda/2 + b"
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
				"Box1:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-Width/2 -Lambda/4",
					"Y:="			, "0mm",
					"Z:="			, "-Lambda/4"
				]
			]
		]
	])
oProject.Save()
oDesign.AnalyzeAll()
oProject.DeleteDesign("Horn4")
oProject.DeleteDesign("Horn3")
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["Box1"],
		"IsIncidentField:="	, False,
		"IsEnforcedField:="	, False,
		"IsFssReference:="	, False,
		"IsForPML:="		, False,
		"UseAdaptiveIE:="	, False,
		"IncludeInPostproc:="	, True
	])
oProject.Save()
oDesign.AnalyzeAll()
oProject.CopyDesign("Horn1")
oProject.Paste()
oDesign = oProject.SetActiveDesign("Horn2")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_1_1,via_L1_2,via_L1_2_1,via_L1_3,via_L1_3_1,via_L1_4,via_L1_4_1,via_L1_5,via_L1_5_1,via_L1_6,via_L1_6_1,via_L1_7,via_L1_7_1,via_L1_8,via_L1_8_1,via_L1_9,via_L1_9_1,via_L1_10,via_L1_10_1,via_L1_11,via_L1_11_1,via_L2_1,via_L2_1_1,via_L2_2,via_L2_2_1,via_L2_3,via_L2_3_1,via_L2_4,via_L2_4_1,via_L2_5,via_L2_5_1,via_L2_6,via_L2_6_1,via_L2_7,via_L2_7_1,via_L2_8,via_L2_8_1,via_L2_9,via_L2_9_1,via_L2_10,via_L2_10_1"
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
				"NAME:DeletedProps", 
				"p"
			]
		]
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
					"NAME:p",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"DD"
			]
		]
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
					"NAME:DD",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "14mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L1"
			]
		]
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
					"NAME:L1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"L2"
			]
		]
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
					"NAME:L2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"a"
			]
		]
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
					"NAME:a",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "5mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"d"
			]
		]
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
					"NAME:d",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.8mm"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N2"
			]
		]
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
					"NAME:N2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10"
				]
			]
		]
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
				"NAME:DeletedProps", 
				"N1"
			]
		]
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
					"NAME:N1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "11"
				]
			]
		]
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+0*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+1*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+2*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+3*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+4*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+5*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+6*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+7*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+8*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+9*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2",
		"YCenter:="		, "d/2+10*L1/(N1-1)",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L1_11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*1",
		"YCenter:="		, "d/2+L1+1*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*2",
		"YCenter:="		, "d/2+L1+2*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*3",
		"YCenter:="		, "d/2+L1+3*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*4",
		"YCenter:="		, "d/2+L1+4*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*5",
		"YCenter:="		, "d/2+L1+5*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*6",
		"YCenter:="		, "d/2+L1+6*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*7",
		"YCenter:="		, "d/2+L1+7*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*8",
		"YCenter:="		, "d/2+L1+8*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*9",
		"YCenter:="		, "d/2+L1+9*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "-a/2-((DD-a)/2-d/2)/N2*10",
		"YCenter:="		, "d/2+L1+10*(L2 -d/2)/N2",
		"ZCenter:="		, "0",
		"Radius:="		, "d/2",
		"Height:="		, "b",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "via_L2_10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"pec\"",
		"SolveInside:="		, False
	])
oEditor.DuplicateMirror(
	[
		"NAME:Selections",
		"Selections:="		, "via_L1_1,via_L1_2,via_L1_3,via_L1_4,via_L1_5,via_L1_6,via_L1_7,via_L1_8,via_L1_9,via_L1_10,via_L1_11,via_L2_1,via_L2_2,via_L2_3,via_L2_4,via_L2_5,via_L2_6,via_L2_7,via_L2_8,via_L2_9,via_L2_10",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToMirrorParameters",
		"DuplicateMirrorBaseX:=", "0mm",
		"DuplicateMirrorBaseY:=", "0mm",
		"DuplicateMirrorBaseZ:=", "0mm",
		"DuplicateMirrorNormalX:=", "1mm",
		"DuplicateMirrorNormalY:=", "0mm",
		"DuplicateMirrorNormalZ:=", "0mm"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", "true"
	])
oProject.CopyDesign("Horn2")
oProject.Save()
oProject.DeleteDesign("Horn2")
oProject.CopyDesign("split_ring0905_D")
oProject.Paste()
oDesign = oProject.SetActiveDesign("split_ring0905_D1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "Top_patch",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "GND",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1,Ring1_3"
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
					"NAME:Len",
					"Value:="		, "L1+L2+rad"
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
				"Via_Box:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "-25mm"
				]
			]
		]
	])
oProject.Save()
oDesign.Analyze("Setup1 : Sweep")
oProject.Save()
oProject.CopyDesign("Horn1")
oProject.Paste()
oDesign = oProject.SetActiveDesign("Horn2")
oModule = oDesign.GetModule("Optimetrics")
oModule.DeleteSetups(["a"])
oModule.InsertSetup("OptiParametric", 
	[
		"NAME:ParametricSetup1",
		"IsEnabled:="		, True,
		[
			"NAME:ProdOptiSetupData",
			"SaveFields:="		, False,
			"CopyMesh:="		, False
		],
		[
			"NAME:StartingPoint"
		],
		"Sim. Setups:="		, ["Setup1"],
		[
			"NAME:Sweeps",
			[
				"NAME:SweepDefinition",
				"Variable:="		, "L3",
				"Data:="		, "LIN 4mm 10mm 1mm",
				"OffsetF1:="		, False,
				"Synchronize:="		, 0
			]
		],
		[
			"NAME:Sweep Operations"
		],
		[
			"NAME:Goals"
		]
	])
oProject.Save()
oModule.SolveSetup("ParametricSetup1")
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("XY Plot 3", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"L3:="			, ["All"],
		"b:="			, ["Nominal"],
		"p:="			, ["Nominal"],
		"DD:="			, ["Nominal"],
		"L1:="			, ["Nominal"],
		"L2:="			, ["Nominal"],
		"a:="			, ["Nominal"],
		"d:="			, ["Nominal"],
		"N2:="			, ["Nominal"],
		"N1:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(S(1,1))"]
	], [])
oModule = oDesign.GetModule("FieldsReporter")
oModule.CreateFieldPlot(
	[
		"NAME:Mag_E1",
		"SolutionName:="	, "Setup1 : LastAdaptive",
		"QuantityName:="	, "Mag_E",
		"PlotFolder:="		, "E Field",
		"UserSpecifyName:="	, 0,
		"UserSpecifyFolder:="	, 0,
		"StreamlinePlot:="	, False,
		"IntrinsicVar:="	, "Freq=\'27GHz\' Phase=\'0deg\'",
		"PlotGeomInfo:="	, [1,"Volume","ObjList",1,"Box1"],
		"FilterBoxes:="		, [0],
		[
			"NAME:PlotOnVolumeSettings",
			"PlotIsoSurface:="	, True,
			"PointSize:="		, 1,
			"Refinement:="		, 0,
			"CloudSpacing:="	, 0.5,
			"CloudMinSpacing:="	, -1,
			"CloudMaxSpacing:="	, -1,
			[
				"NAME:Arrow3DSpacingSettings",
				"ArrowUniform:="	, True,
				"ArrowSpacing:="	, 0,
				"MinArrowSpacing:="	, 0,
				"MaxArrowSpacing:="	, 0
			]
		]
	])
oModule.DeleteFieldPlot(["Mag_E1"])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Substrate"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material",
					"Value:="		, "\"FR4_epoxy\""
				]
			]
		]
	])
oProject.Save()
oDesign.Analyze("Setup1 : Sweep")
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "0mm",
		"OriginY:="		, "0mm",
		"OriginZ:="		, "0mm",
		"XAxisXvec:="		, "1mm",
		"XAxisYvec:="		, "0mm",
		"XAxisZvec:="		, "0mm",
		"YAxisXvec:="		, "0mm",
		"YAxisYvec:="		, "0mm",
		"YAxisZvec:="		, "-1mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RelativeCS1"
	])
oModule = oDesign.GetModule("RadField")
oModule.InsertFarFieldSphereSetup(
	[
		"NAME:EH",
		"UseCustomRadiationSurface:=", False,
		"ThetaStart:="		, "-180deg",
		"ThetaStop:="		, "180deg",
		"ThetaStep:="		, "2deg",
		"PhiStart:="		, "0deg",
		"PhiStop:="		, "90deg",
		"PhiStep:="		, "90deg",
		"UseLocalCS:="		, True,
		"CoordSystem:="		, "RelativeCS1"
	])
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("XY Plot 4", "Far Fields", "Rectangular Plot", "Setup1 : LastAdaptive", 
	[
		"Context:="		, "EH"
	], 
	[
		"Theta:="		, ["All"],
		"Phi:="			, ["All"],
		"Freq:="		, ["27GHz"],
		"L3:="			, ["All"],
		"b:="			, ["Nominal"],
		"p:="			, ["Nominal"],
		"DD:="			, ["Nominal"],
		"L1:="			, ["Nominal"],
		"L2:="			, ["Nominal"],
		"a:="			, ["Nominal"],
		"d:="			, ["Nominal"],
		"N2:="			, ["Nominal"],
		"N1:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Theta",
		"Y Component:="		, ["dB(GainTotal)"]
	], [])
oDesign.RenameDesignInstance("Horn2", "Horn2_FR4")
oProject.Paste()
oDesign = oProject.SetActiveDesign("split_ring0905_2124")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "GND",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "Top_patch",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1_2"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.Rotate(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:RotateParameters",
		"RotateAxis:="		, "Z",
		"RotateAngle:="		, "15deg"
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rectangle2:Rotate:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Angle",
					"Value:="		, "-15deg"
				]
			]
		]
	])
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "0mm",
		"OriginY:="		, "-1.3mm",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCSTab",
			[
				"NAME:PropServers", 
				"RelativeCS3"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Origin",
					"X:="			, "0mm",
					"Y:="			, "-offset",
					"Z:="			, "b"
				]
			]
		]
	])
oEditor.Rotate(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:RotateParameters",
		"RotateAxis:="		, "Z",
		"RotateAngle:="		, "-15deg"
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "0mm",
		"OriginY:="		, "1.3mm",
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
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCSTab",
			[
				"NAME:PropServers", 
				"RelativeCS4"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Origin",
					"X:="			, "0mm",
					"Y:="			, "offset",
					"Z:="			, "b"
				]
			]
		]
	])
oEditor.Rotate(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1_1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:RotateParameters",
		"RotateAxis:="		, "Z",
		"RotateAngle:="		, "15deg"
	])
oEditor.DuplicateAlongLine(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1,Ring1_1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToAlongLineParameters",
		"CreateNewObjects:="	, True,
		"XComponent:="		, "0mm",
		"YComponent:="		, "0mm",
		"ZComponent:="		, "-2.5mm",
		"NumClones:="		, "2"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rectangle2:DuplicateAlongLine:2", 
				"Rectangle2:DuplicateAlongLine:2"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Vector",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "-b"
				]
			]
		]
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "GND,Ring1_1_1,Ring1_2"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Top_patch,Ring1,Ring1_1"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oProject.Save()
oDesign.Analyze("Setup1 : Sweep")
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "GND",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "Top_patch",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, True,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "0mm",
				"Y:="			, "-2.6mm",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-0.724693326287058mm",
				"Y:="			, "-5.30459231360939mm",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "0mm",
				"Y:="			, "-5.3mm",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "0mm",
				"Y:="			, "-2.6mm",
				"Z:="			, "0mm"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 1,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 2,
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
		"Name:="		, "Polyline1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.699999988079071,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS2"
	])
oEditor.DuplicateMirror(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToMirrorParameters",
		"DuplicateMirrorBaseX:=", "0mm",
		"DuplicateMirrorBaseY:=", "0mm",
		"DuplicateMirrorBaseZ:=", "0mm",
		"DuplicateMirrorNormalX:=", "1mm",
		"DuplicateMirrorNormalY:=", "0mm",
		"DuplicateMirrorNormalZ:=", "0mm"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Polyline1:DuplicateMirror:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Coordinate System",
					"Value:="		, "RelativeCS1"
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
				"Polyline1:DuplicateMirror:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Normal Position",
					"X:="			, "0mm",
					"Y:="			, "1mm",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline1,Polyline1_1"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.DuplicateAlongLine(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToAlongLineParameters",
		"CreateNewObjects:="	, True,
		"XComponent:="		, "0mm",
		"YComponent:="		, "0mm",
		"ZComponent:="		, "-2.5mm",
		"NumClones:="		, "2"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Polyline1:DuplicateAlongLine:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Vector",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "-b"
				]
			]
		]
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "GND,Polyline1_2,Ring1_1_1,Ring1_2"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Top_patch,Polyline1,Ring1,Ring1_1"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oProject.Save()
oDesign.AnalyzeAll()
oProject.CopyDesign("split_ring0905_2124")
oProject.Paste()
oDesign = oProject.SetActiveDesign("split_ring0905_2125")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "Top_patch",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "GND",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline1"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline1_2"
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
					"NAME:theta1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "15deg"
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
				"Rectangle2:Rotate:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Angle",
					"Value:="		, "-theta1"
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
				"Rectangle2:Rotate:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Angle",
					"Value:="		, "theta1"
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-0.65mm",
		"YStart:="		, "-1.55mm",
		"ZStart:="		, "0mm",
		"Width:="		, "-0.1mm",
		"Height:="		, "0.15mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle3",
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
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rectangle3:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-offset+ww/2",
					"Y:="			, "-1.55mm",
					"Z:="			, "0mm"
				],
				[
					"NAME:Position",
					"X:="			, "-offset+ww/2",
					"Y:="			, "0",
					"Z:="			, "0mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "-ww"
				],
				[
					"NAME:YSize",
					"Value:="		, "ww"
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
				"Rectangle3:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-offset+ww/2",
					"Y:="			, "0",
					"Z:="			, "b"
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
				"Rectangle3:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "0",
					"Y:="			, "-offset+ww/2",
					"Z:="			, "b"
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
				"Rectangle3:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "0",
					"Y:="			, "-offset",
					"Z:="			, "b"
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
				"Rectangle3:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:YSize",
					"Value:="		, "-ww"
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
				"Rectangle3:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "0",
					"Y:="			, "-offset+ww/2",
					"Z:="			, "b"
				]
			]
		]
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1_1,Ring1_1_1,Ring1_2"
	])
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1,Rectangle3"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.DuplicateMirror(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToMirrorParameters",
		"DuplicateMirrorBaseX:=", "0mm",
		"DuplicateMirrorBaseY:=", "0mm",
		"DuplicateMirrorBaseZ:=", "0mm",
		"DuplicateMirrorNormalX:=", "0mm",
		"DuplicateMirrorNormalY:=", "1mm",
		"DuplicateMirrorNormalZ:=", "0mm"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1,Ring1_1"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.DuplicateAlongLine(
	[
		"NAME:Selections",
		"Selections:="		, "Ring1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateToAlongLineParameters",
		"CreateNewObjects:="	, True,
		"XComponent:="		, "0mm",
		"YComponent:="		, "0mm",
		"ZComponent:="		, "-2.5mm",
		"NumClones:="		, "2"
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rectangle3:DuplicateAlongLine:2"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Vector",
					"X:="			, "0mm",
					"Y:="			, "0mm",
					"Z:="			, "-b"
				]
			]
		]
	])
oModule = oDesign.GetModule("Optimetrics")
oModule.InsertSetup("OptiParametric", 
	[
		"NAME:ParametricSetup1",
		"IsEnabled:="		, True,
		[
			"NAME:ProdOptiSetupData",
			"SaveFields:="		, False,
			"CopyMesh:="		, False
		],
		[
			"NAME:StartingPoint"
		],
		"Sim. Setups:="		, ["Setup1"],
		[
			"NAME:Sweeps",
			[
				"NAME:SweepDefinition",
				"Variable:="		, "theta1",
				"Data:="		, "LIN -20deg 20deg 5deg",
				"OffsetF1:="		, False,
				"Synchronize:="		, 0
			]
		],
		[
			"NAME:Sweep Operations"
		],
		[
			"NAME:Goals"
		]
	])
oModule.RenameSetup("ParametricSetup1", "theta1")
oProject.Save()
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "GND,Ring1_2"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Top_patch,Ring1"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oProject.Save()
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"GND:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "rad",
					"Y:="			, "-Width/2",
					"Z:="			, "0mm"
				]
			]
		]
	])
oProject.Save()
oModule.SolveSetup("theta1")
oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditFrequencySweep("Setup1", "Sweep", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"SetupType:="		, "LinearStep",
		"StartValue:="		, "24GHz",
		"StopValue:="		, "30GHz",
		"StepSize:="		, "0.15GHz",
		"Type:="		, "Fast",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"GenerateFieldsForAllFreqs:=", False,
		"ExtrapToDC:="		, False
	])
oModule.EditSetup("Setup1", 
	[
		"NAME:Setup1",
		"Frequency:="		, "27GHz",
		"PortsOnly:="		, False,
		"MaxDeltaS:="		, 0.02,
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
oProject.Save()
oModule = oDesign.GetModule("Optimetrics")
oModule.SolveSetup("theta1")
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("XY Plot 1", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"L1:="			, ["Nominal"],
		"L2:="			, ["Nominal"],
		"L3:="			, ["Nominal"],
		"D:="			, ["Nominal"],
		"a:="			, ["Nominal"],
		"b:="			, ["Nominal"],
		"w:="			, ["Nominal"],
		"Width:="		, ["Nominal"],
		"ww:="			, ["Nominal"],
		"offset:="		, ["Nominal"],
		"rad:="			, ["Nominal"],
		"r_spacing:="		, ["Nominal"],
		"theta1:="		, ["All"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(S(1,1))"]
	], [])
oProject.CopyDesign("split_ring0905_2125")
oModule.DeleteTraces(
	[
		"XY Plot 1:="		, ["dB(S(1,1))"]
	])
oDesign.Undo()
oModule = oDesign.GetModule("Optimetrics")
oModule.EditSetup("theta1", 
	[
		"NAME:theta1",
		"IsEnabled:="		, True,
		[
			"NAME:ProdOptiSetupData",
			"SaveFields:="		, False,
			"CopyMesh:="		, False
		],
		[
			"NAME:StartingPoint"
		],
		"Sim. Setups:="		, ["Setup1"],
		[
			"NAME:Sweeps",
			[
				"NAME:SweepDefinition",
				"Variable:="		, "theta1",
				"Data:="		, "LIN -10deg 0deg 2deg",
				"OffsetF1:="		, False,
				"Synchronize:="		, 0
			]
		],
		[
			"NAME:Sweep Operations"
		],
		[
			"NAME:Goals"
		]
	])
oProject.Save()
oModule.SolveSetup("theta1")
oProject.CopyDesign("split_ring0905_2125")
oProject.Paste()
oDesign = oProject.SetActiveDesign("split_ring0905_2126")
oDesign.RenameDesignInstance("split_ring0905_2126", "split_ring0905_2126_8")
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
					"NAME:theta1",
					"Value:="		, "8deg"
				]
			]
		]
	])
oModule = oDesign.GetModule("Optimetrics")
oModule.DeleteSetups(["theta1"])
oProject.Save()
oDesign.Analyze("Setup1 : Sweep")
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
					"NAME:theta1",
					"Value:="		, "-8deg"
				]
			]
		]
	])
oDesign.Undo()
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
					"NAME:theta1",
					"Value:="		, "-8deg"
				]
			]
		]
	])
oProject.Save()
oDesign.Analyze("Setup1 : Sweep")
oProject.Save()
