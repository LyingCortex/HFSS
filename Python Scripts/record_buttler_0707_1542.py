# ----------------------------------------------
# Script Recorded by Ansoft HFSS Version 15.0.0
# 3:42:07 下午  七月 07, 2016
# ----------------------------------------------
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("My_buttler_0707")
oDesign = oProject.SetActiveDesign("butler_1458")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "arm1,arm2,arm3,arm4,arm5,arm6,arm7,arm8"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "arm1"
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
				"L_u"
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
					"NAME:L_u",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.8568mm"
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
				"W_u"
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
					"NAME:W_u",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.4948mm"
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
				"L_l"
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
					"NAME:L_l",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.9146mm"
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
				"W_l"
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
					"NAME:W_l",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.254mm"
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
				"W_ul"
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
					"NAME:W_ul",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.254mm"
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
				"L_ul"
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
					"NAME:L_ul",
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
				"h0"
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
					"NAME:h0",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.018mm"
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
				"H"
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
					"NAME:H",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.254mm"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2-W_u/2",
		"YPosition:="		, "-L_u/2",
		"ZPosition:="		, "H",
		"XSize:="		, "W_u",
		"YSize:="		, "L_u",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "L_l/2+W_u/2",
		"YPosition:="		, "-L_u/2",
		"ZPosition:="		, "H",
		"XSize:="		, "-W_u",
		"YSize:="		, "L_u",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2",
		"YPosition:="		, "-L_u/2-W_l/2",
		"ZPosition:="		, "H",
		"XSize:="		, "L_l",
		"YSize:="		, "W_l",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2",
		"YPosition:="		, "L_u/2+W_l/2",
		"ZPosition:="		, "H",
		"XSize:="		, "L_l",
		"YSize:="		, "-W_l",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2-W_ul/2",
		"YPosition:="		, "-L_u/2-L_ul",
		"ZPosition:="		, "H",
		"XSize:="		, "W_ul",
		"YSize:="		, "L_ul",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "L_l/2+W_ul/2",
		"YPosition:="		, "-L_u/2-L_ul",
		"ZPosition:="		, "H",
		"XSize:="		, "-W_ul",
		"YSize:="		, "L_ul",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2-W_ul/2",
		"YPosition:="		, "L_u/2+L_ul",
		"ZPosition:="		, "H",
		"XSize:="		, "W_ul",
		"YSize:="		, "-L_ul",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "L_l/2+W_ul/2",
		"YPosition:="		, "L_u/2+L_ul",
		"ZPosition:="		, "H",
		"XSize:="		, "-W_ul",
		"YSize:="		, "-L_ul",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "arm1,arm2,arm3,arm4,arm5,arm6,arm7,arm8"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"arm1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "arm"
				]
			]
		]
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "arm"
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
				"L_u"
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
					"NAME:L_u",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.8568mm"
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
				"W_u"
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
					"NAME:W_u",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.4948mm"
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
				"L_l"
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
					"NAME:L_l",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.9146mm"
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
				"W_l"
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
					"NAME:W_l",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.254mm"
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
				"W_ul"
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
					"NAME:W_ul",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.254mm"
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
				"L_ul"
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
					"NAME:L_ul",
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
				"h0"
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
					"NAME:h0",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.018mm"
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
				"H"
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
					"NAME:H",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.254mm"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2-W_u/2",
		"YPosition:="		, "-L_u/2",
		"ZPosition:="		, "H",
		"XSize:="		, "W_u",
		"YSize:="		, "L_u",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "L_l/2+W_u/2",
		"YPosition:="		, "-L_u/2",
		"ZPosition:="		, "H",
		"XSize:="		, "-W_u",
		"YSize:="		, "L_u",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2",
		"YPosition:="		, "-L_u/2-W_l/2",
		"ZPosition:="		, "H",
		"XSize:="		, "L_l",
		"YSize:="		, "W_l",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2",
		"YPosition:="		, "L_u/2+W_l/2",
		"ZPosition:="		, "H",
		"XSize:="		, "L_l",
		"YSize:="		, "-W_l",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2-W_ul/2",
		"YPosition:="		, "-L_u/2-L_ul",
		"ZPosition:="		, "H",
		"XSize:="		, "W_ul",
		"YSize:="		, "L_ul",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "L_l/2+W_ul/2",
		"YPosition:="		, "-L_u/2-L_ul",
		"ZPosition:="		, "H",
		"XSize:="		, "-W_ul",
		"YSize:="		, "L_ul",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2-W_ul/2",
		"YPosition:="		, "L_u/2+L_ul",
		"ZPosition:="		, "H",
		"XSize:="		, "W_ul",
		"YSize:="		, "-L_ul",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "L_l/2+W_ul/2",
		"YPosition:="		, "L_u/2+L_ul",
		"ZPosition:="		, "H",
		"XSize:="		, "-W_ul",
		"YSize:="		, "-L_ul",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "arm1,arm2,arm3,arm4,arm5,arm6,arm7,arm8"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"arm1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "coupler"
				]
			]
		]
	])
oProject.Save()
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"coupler"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 128,
					"B:="			, 64
				]
			]
		]
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "coupler"
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
				"L_u"
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
					"NAME:L_u",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.8568mm"
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
				"W_u"
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
					"NAME:W_u",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.4948mm"
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
				"L_l"
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
					"NAME:L_l",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.9146mm"
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
				"W_l"
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
					"NAME:W_l",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.254mm"
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
				"W_ul"
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
					"NAME:W_ul",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.254mm"
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
				"L_ul"
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
					"NAME:L_ul",
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
				"h0"
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
					"NAME:h0",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.018mm"
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
				"H"
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
					"NAME:H",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.254mm"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2-W_u/2",
		"YPosition:="		, "-L_u/2",
		"ZPosition:="		, "H",
		"XSize:="		, "W_u",
		"YSize:="		, "L_u",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "L_l/2+W_u/2",
		"YPosition:="		, "-L_u/2",
		"ZPosition:="		, "H",
		"XSize:="		, "-W_u",
		"YSize:="		, "L_u",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2",
		"YPosition:="		, "-L_u/2-W_l/2",
		"ZPosition:="		, "H",
		"XSize:="		, "L_l",
		"YSize:="		, "W_l",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2",
		"YPosition:="		, "L_u/2+W_l/2",
		"ZPosition:="		, "H",
		"XSize:="		, "L_l",
		"YSize:="		, "-W_l",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2-W_ul/2",
		"YPosition:="		, "-L_u/2-L_ul",
		"ZPosition:="		, "H",
		"XSize:="		, "W_ul",
		"YSize:="		, "L_ul",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "L_l/2+W_ul/2",
		"YPosition:="		, "-L_u/2-L_ul",
		"ZPosition:="		, "H",
		"XSize:="		, "-W_ul",
		"YSize:="		, "L_ul",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-L_l/2-W_ul/2",
		"YPosition:="		, "L_u/2+L_ul",
		"ZPosition:="		, "H",
		"XSize:="		, "W_ul",
		"YSize:="		, "-L_ul",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "L_l/2+W_ul/2",
		"YPosition:="		, "L_u/2+L_ul",
		"ZPosition:="		, "H",
		"XSize:="		, "-W_ul",
		"YSize:="		, "-L_ul",
		"ZSize:="		, "h0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "arm8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.7,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "arm1,arm2,arm3,arm4,arm5,arm6,arm7,arm8"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"arm1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "coupler"
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
				"coupler"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 128,
					"B:="			, 64
				]
			]
		]
	])
oProject.Save()
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
					"NAME:Sub_W",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				],
				[
					"NAME:Sub_L",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10mm"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-2mm",
		"YPosition:="		, "-2.4mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "3.6mm",
		"YSize:="		, "4.8mm",
		"ZSize:="		, "-0.6mm"
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
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Substrate"
				],
				[
					"NAME:Material",
					"Value:="		, "\"Rogers RO4350 (tm)\""
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
				"Substrate:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-Sub_W/2",
					"Y:="			, "-Sub_L/2",
					"Z:="			, "0mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "Sub_W"
				],
				[
					"NAME:YSize",
					"Value:="		, "Sub_L"
				],
				[
					"NAME:ZSize",
					"Value:="		, "H"
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
					"NAME:Sub_W",
					"Value:="		, "6mm"
				],
				[
					"NAME:Sub_L",
					"Value:="		, "6mm"
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "0.2mm",
		"YStart:="		, "0mm",
		"ZStart:="		, "-1.7mm",
		"Width:="		, "0.5mm",
		"Height:="		, "0.4mm",
		"WhichAxis:="		, "Y"
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
					"Value:="		, "Port1"
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
				"Port1:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "L_l/2+W_ul/2",
					"Y:="			, "-L_u/2-L_ul",
					"Z:="			, "0mm"
				],
				[
					"NAME:ZSize",
					"Value:="		, "H"
				],
				[
					"NAME:XSize",
					"Value:="		, "-W_ul"
				]
			]
		]
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "27mm",
		"YStart:="		, "0mm",
		"ZStart:="		, "20.7mm",
		"Width:="		, "2.8mm",
		"Height:="		, "3.9mm",
		"WhichAxis:="		, "Y"
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
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "24.1mm",
		"YStart:="		, "0mm",
		"ZStart:="		, "18.1mm",
		"Width:="		, "-1mm",
		"Height:="		, "-1.1mm",
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
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "7.4mm",
		"YStart:="		, "0mm",
		"ZStart:="		, "5.9mm",
		"Width:="		, "-1.9mm",
		"Height:="		, "-2.3mm",
		"WhichAxis:="		, "Y"
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
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Port2"
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
				"Port2:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "L_l/2+W_ul/2",
					"Y:="			, "-L_u/2-L_ul",
					"Z:="			, "0mm"
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
				"Port1:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-(L_l/2+W_ul/2)",
					"Y:="			, "-L_u/2-L_ul",
					"Z:="			, "0mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "W_ul"
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
				"Port2:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "-W_ul"
				],
				[
					"NAME:ZSize",
					"Value:="		, "H"
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
				"Rectangle2"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Port3"
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
				"Port3:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-(L_l/2+W_ul/2)",
					"Y:="			, "L_u/2+L_ul",
					"Z:="			, "0mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "W_ul"
				],
				[
					"NAME:ZSize",
					"Value:="		, "H"
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
				"Rectangle3"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Port4"
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
				"Port4:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "(L_l/2+W_ul/2)",
					"Y:="			, "L_u/2+L_ul",
					"Z:="			, "0mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "-W_ul"
				],
				[
					"NAME:ZSize",
					"Value:="		, "H"
				]
			]
		]
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignLumpedPort(
	[
		"NAME:1",
		"Objects:="		, ["Port1"],
		"RenormalizeAllTerminals:=", True,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, True,
				[
					"NAME:IntLine",
					"Start:="		, ["-0.9573mm","-1.9284mm","-2.33295215237571e-017mm"],
					"End:="			, ["-0.9573mm","-1.9284mm","0.254mm"]
				],
				"CharImp:="		, "Zpi",
				"AlignmentGroup:="	, 0
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"FullResistance:="	, "74.6865ohm",
		"FullReactance:="	, "0ohm"
	])
oModule.AssignLumpedPort(
	[
		"NAME:2",
		"Objects:="		, ["Port2"],
		"RenormalizeAllTerminals:=", True,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, True,
				[
					"NAME:IntLine",
					"Start:="		, ["0.9573mm","-1.9284mm","2.33295215237571e-017mm"],
					"End:="			, ["0.9573mm","-1.9284mm","0.254mm"]
				],
				"CharImp:="		, "Zpi",
				"AlignmentGroup:="	, 0
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"FullResistance:="	, "74.6865ohm",
		"FullReactance:="	, "0ohm"
	])
oModule.AssignLumpedPort(
	[
		"NAME:3",
		"Objects:="		, ["Port3"],
		"RenormalizeAllTerminals:=", True,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, True,
				[
					"NAME:IntLine",
					"Start:="		, ["-0.9573mm","1.9284mm","-2.33295215237571e-017mm"],
					"End:="			, ["-0.9573mm","1.9284mm","0.254mm"]
				],
				"CharImp:="		, "Zpi",
				"AlignmentGroup:="	, 0
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"FullResistance:="	, "74.6865ohm",
		"FullReactance:="	, "0ohm"
	])
oModule.AssignLumpedPort(
	[
		"NAME:4",
		"Objects:="		, ["Port4"],
		"RenormalizeAllTerminals:=", True,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, True,
				[
					"NAME:IntLine",
					"Start:="		, ["0.9573mm","1.9284mm","2.33295215237571e-017mm"],
					"End:="			, ["0.9573mm","1.9284mm","0.254mm"]
				],
				"CharImp:="		, "Zpi",
				"AlignmentGroup:="	, 0
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"FullResistance:="	, "74.6865ohm",
		"FullReactance:="	, "0ohm"
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
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Region"
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-6mm",
		"YPosition:="		, "-3.5mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "9mm",
		"YSize:="		, "8mm",
		"ZSize:="		, "1.5mm"
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
					"Value:="		, "12.5mm"
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
					"X:="			, "-Sub_W/2-Lambda/4",
					"Y:="			, "-Sub_L/2-Lambda/4",
					"Z:="			, "-Lambda/4"
				],
				[
					"NAME:XSize",
					"Value:="		, "Sub_W+Lambda/2"
				],
				[
					"NAME:YSize",
					"Value:="		, "Sub_L+Lambda/2"
				],
				[
					"NAME:ZSize",
					"Value:="		, "Lambda/2+H+h0*2"
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
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Air"
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
				"Air"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material",
					"Value:="		, "\"air\""
				]
			]
		]
	])
oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["Air"],
		"IsIncidentField:="	, False,
		"IsEnforcedField:="	, False,
		"IsFssReference:="	, False,
		"IsForPML:="		, False,
		"UseAdaptiveIE:="	, False,
		"IncludeInPostproc:="	, True
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-3mm",
		"YPosition:="		, "-3mm",
		"ZPosition:="		, "0.254mm",
		"XSize:="		, "6mm",
		"YSize:="		, "6mm",
		"ZSize:="		, "-4.254mm"
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
					"X:="			, "-Sub_W/2",
					"Y:="			, "-Sub_L/2",
					"Z:="			, "0mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "Sub_W"
				],
				[
					"NAME:YSize",
					"Value:="		, "Sub_L"
				],
				[
					"NAME:ZSize",
					"Value:="		, "-h0"
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
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "GND"
				],
				[
					"NAME:Material",
					"Value:="		, "\"copper\""
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
				"Air:CreateBox:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "-Sub_W/2-Lambda/4",
					"Y:="			, "-Sub_L/2-Lambda/4",
					"Z:="			, "-Lambda/4-h0"
				]
			]
		]
	])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"Frequency:="		, "24GHz",
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
		"StartValue:="		, "23GHz",
		"StopValue:="		, "25GHz",
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
		"L_u:="			, ["Nominal"],
		"W_u:="			, ["Nominal"],
		"L_l:="			, ["Nominal"],
		"W_l:="			, ["Nominal"],
		"W_ul:="		, ["Nominal"],
		"L_ul:="		, ["Nominal"],
		"h0:="			, ["Nominal"],
		"H:="			, ["Nominal"],
		"Sub_W:="		, ["Nominal"],
		"Sub_L:="		, ["Nominal"],
		"Lambda:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(S(1,1))","dB(S(2,1))","dB(S(3,1))","dB(S(4,1))"]
	], [])
oModule.AddTraces("XY Plot 1", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"L_u:="			, ["Nominal"],
		"W_u:="			, ["Nominal"],
		"L_l:="			, ["Nominal"],
		"W_l:="			, ["Nominal"],
		"W_ul:="		, ["Nominal"],
		"L_ul:="		, ["Nominal"],
		"h0:="			, ["Nominal"],
		"H:="			, ["Nominal"],
		"Sub_W:="		, ["Nominal"],
		"Sub_L:="		, ["Nominal"],
		"Lambda:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(S(4,3))"]
	], [])
oModule.CreateReport("XY Plot 2", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"L_u:="			, ["Nominal"],
		"W_u:="			, ["Nominal"],
		"L_l:="			, ["Nominal"],
		"W_l:="			, ["Nominal"],
		"W_ul:="		, ["Nominal"],
		"L_ul:="		, ["Nominal"],
		"h0:="			, ["Nominal"],
		"H:="			, ["Nominal"],
		"Sub_W:="		, ["Nominal"],
		"Sub_L:="		, ["Nominal"],
		"Lambda:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["cang_deg(S(4,3))"]
	], [])
oModule.AddMarker("XY Plot 2", "m1", "cang_deg(S(4 3)) : Setup1 : Sweep : Cartesian", "24GHz")
oModule.RenameReport("XY Plot 1", "S_Para")
oModule.RenameReport("XY Plot 2", "Phase")
oModule.AddTraces("Phase", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"L_u:="			, ["Nominal"],
		"W_u:="			, ["Nominal"],
		"L_l:="			, ["Nominal"],
		"W_l:="			, ["Nominal"],
		"W_ul:="		, ["Nominal"],
		"L_ul:="		, ["Nominal"],
		"h0:="			, ["Nominal"],
		"H:="			, ["Nominal"],
		"Sub_W:="		, ["Nominal"],
		"Sub_L:="		, ["Nominal"],
		"Lambda:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["cang_deg(S(3,1))","cang_deg(S(4,1))"]
	], [])
oModule.AddDeltaMarker("Phase", "m1", "cang_deg(S(4 3)) : Setup1 : Sweep : Cartesian", "24GHz", "m2", "cang_deg(S(4 1)) : Setup1 : Sweep : Cartesian", "24GHz")
oModule.AddDeltaMarker("Phase", "m2", "cang_deg(S(4 1)) : Setup1 : Sweep : Cartesian", "24GHz", "m3", "cang_deg(S(3 1)) : Setup1 : Sweep : Cartesian", "24GHz")
oModule.AddDeltaMarker("S_Para", "m1", "dB(S(4 1)) : Setup1 : Sweep : Cartesian", "24GHz", "m2", "dB(S(3 1)) : Setup1 : Sweep : Cartesian", "24GHz")
oProject.Save()
oProject.Save()
oDesign = oProject.SetActiveDesign("Butler3")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "L10",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "L10",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:L11",
				"OperationIndices:="	, [3]
			]
		]
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:L12",
				"OperationIndices:="	, [3]
			]
		]
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:L11",
				"OperationIndices:="	, [1]
			]
		]
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:L10",
				"OperationIndices:="	, [1]
			]
		]
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:Polyline2",
				"OperationIndices:="	, [3]
			]
		]
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:Polyline3",
				"OperationIndices:="	, [3]
			]
		]
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "L4"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "L6"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "L7"
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:L13",
				"OperationIndices:="	, [4]
			]
		]
	])
oProject.Save()
oProject.Paste()
oDesign = oProject.SetActiveDesign("array6")
oDesign.RenameDesignInstance("array6", "array d=7.2mm h_array=0.508mm")
oProject.Save()
oProject.Paste()
oDesign = oProject.SetActiveDesign("Butler4")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "L1"
	])
oDesign = oProject.SetActiveDesign("array d=7.2mm h_array=0.508mm")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ImportFromClipboard()
oDesign.Undo()
oProject.DeleteDesign("array d=7.2mm h_array=0.508mm")
oProject.Paste()
oDesign = oProject.SetActiveDesign("Butler3")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "L3"
	])
oDesign = oProject.SetActiveDesign("Butler4")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Paste()
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "L37"
	])
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "L1"
	])
oDesign = oProject.SetActiveDesign("Butler3")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Paste()
oDesign.Undo()
oProject.Save()
oDesign.RenameDesignInstance("Butler3", "Butler_all_parts")
oProject.CopyDesign("Butler_all_parts")
oProject.Paste()
oDesign = oProject.SetActiveDesign("Butler_all_parts1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "L1,L2,L3,L5,L8,L9,L10,L11,L12,Polyline2,Polyline3,L13"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "P1,P2,P3,P4"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "P6,P7"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "P8"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "P5"
	])
oProject.Save()
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
				"H", 
				"h0", 
				"Sub_W", 
				"Sub_L", 
				"Lambda", 
				"L18", 
				"L21", 
				"B1_L", 
				"L15", 
				"Cut", 
				"L12"
			]
		]
	])
oModule = oDesign.GetModule("ReportSetup")
oModule.DeleteReports(["XY Plot 1"])
oModule.DeleteReports(["XY Plot 2"])
oModule.DeleteReports(["XY Plot 3"])
oModule.DeleteReports(["XY Plot 4"])
oProject.Save()
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
				"L3", 
				"L0", 
				"L1", 
				"L10", 
				"L11", 
				"L16", 
				"L17", 
				"L20", 
				"L19", 
				"W2", 
				"L2", 
				"space_x"
			]
		]
	])
oProject.Save()
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
				"space_y", 
				"W1", 
				"L14"
			]
		]
	])
oDesign = oProject.SetActiveDesign("Butler4")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "L1"
	])
oDesign = oProject.SetActiveDesign("Butler_all_parts1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Paste()
oDesign = oProject.SetActiveDesign("array6")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "10mm",
		"OriginY:="		, "-40mm",
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
oEditor.Paste()
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCSTab",
			[
				"NAME:PropServers", 
				"RelativeCS1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Origin",
					"X:="			, "17mm",
					"Y:="			, "-50mm",
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
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "RelativeCS1"
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCSTab",
			[
				"NAME:PropServers", 
				"RelativeCS1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Origin",
					"X:="			, "17mm",
					"Y:="			, "-space_y*4",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCSTab",
			[
				"NAME:PropServers", 
				"RelativeCS1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Origin",
					"X:="			, "17mm",
					"Y:="			, "-space_y*2",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCSTab",
			[
				"NAME:PropServers", 
				"RelativeCS1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Origin",
					"X:="			, "17mm",
					"Y:="			, "-space_y*3",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCSTab",
			[
				"NAME:PropServers", 
				"RelativeCS1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Origin",
					"X:="			, "space_x*2",
					"Y:="			, "-space_y*3",
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
oProject.Save()
oDesign.RenameDesignInstance("array6", "total_2layer_0707_1730")
oDesign = oProject.SetActiveDesign("Butler4")
oDesign.RenameDesignInstance("Butler4", "Butler")
oDesign = oProject.SetActiveDesign("butler_1458")
oDesign.RenameDesignInstance("butler_1458", "my_butler_1458")
oProject.Paste()
oDesign = oProject.SetActiveDesign("array6")
oDesign.RenameDesignInstance("array6", "Array")
oProject.Save()
oProject.CopyDesign("Array")
oProject.Paste()
oDesign = oProject.SetActiveDesign("Array1")
oDesign.RenameDesignInstance("Array1", "Array_depart")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Patch4,Patch3,Patch2"
	])
oDesign.Undo()
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Patch3,Patch4"
	])
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "Patch1",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.CreateRelativeCS(
	[
		"NAME:RelativeCSParameters",
		"OriginX:="		, "0mm",
		"OriginY:="		, "-30mm",
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
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:divider1_2",
				"OperationIndices:="	, [8]
			]
		]
	])
oDesign.Undo()
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:divider1_2",
				"OperationIndices:="	, [11]
			]
		]
	])
oDesign.Undo()
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:divider1_2",
				"OperationIndices:="	, [11]
			]
		]
	])
oDesign.Undo()
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:divider1_2",
				"OperationIndices:="	, [11]
			]
		]
	])
oDesign.Undo()
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCSTab",
			[
				"NAME:PropServers", 
				"RelativeCS1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Origin",
					"X:="			, "3.5mm",
					"Y:="			, "-30mm",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:divider1_2",
				"OperationIndices:="	, [9]
			]
		]
	])
oDesign.Undo()
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:divider1_2",
				"OperationIndices:="	, [11]
			]
		]
	])
oDesign.Undo()
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global"
	])
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "Patch1",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Patch1_4"
	])
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "Patch1",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:Patch1",
				"OperationIndices:="	, [4]
			]
		]
	])
oEditor.DeleteLastOperation(
	[
		"NAME:Selections",
		"Selections:="		, "Patch1",
		"NewPartsModelFlag:="	, "Model"
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:divider1_2",
				"OperationIndices:="	, [11]
			]
		]
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:divider1_2",
				"OperationIndices:="	, [10]
			]
		]
	])
oDesign.Undo()
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:divider1_2",
				"OperationIndices:="	, [9]
			]
		]
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:divider1_2",
				"OperationIndices:="	, [8]
			]
		]
	])
oEditor.Delete(
	[
		"NAME:Selections",
		"Selections:="		, "Rectangle59"
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:divider1_2",
				"OperationIndices:="	, [7]
			]
		]
	])
oEditor.DeleteOperation(
	[
		"NAME:Parameters",
		[
			"NAME:PartOperations",
			[
				"NAME:divider1_2",
				"OperationIndices:="	, [6]
			]
		]
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
			"NAME:Geometry3DCSTab",
			[
				"NAME:PropServers", 
				"RelativeCS1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Origin",
					"X:="			, "(3.5 +1.1425) mm",
					"Y:="			, "-30mm",
					"Z:="			, "0mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCSTab",
			[
				"NAME:PropServers", 
				"RelativeCS1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Origin",
					"X:="			, "(3.5 +1.1425+7.2) mm",
					"Y:="			, "-30mm",
					"Z:="			, "0mm"
				]
			]
		]
	])
oDesign.Undo()
oDesign.Undo()
oDesign.Undo()
oDesign.Undo()
oDesign.Undo()
oDesign.Undo()
oDesign.Undo()
oDesign.Undo()
oDesign.Undo()
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCSTab",
			[
				"NAME:PropServers", 
				"RelativeCS1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Origin",
					"X:="			, "(3.5+1) mm",
					"Y:="			, "-30mm",
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
oProject.Save()
