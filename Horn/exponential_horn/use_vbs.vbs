' ----------------------------------------------
' Script Recorded by Ansoft HFSS Version 15.0.0
' 4:26:33 下午  4月 11, 2016
' ----------------------------------------------
Dim oAnsoftApp
Dim oDesktop
Dim oProject
Dim oDesign
Dim oEditor
Dim oModule
Set oAnsoftApp = CreateObject("AnsoftHfss.HfssScriptInterface")
Set oDesktop = oAnsoftApp.GetAppDesktop()
oDesktop.RestoreWindow
Set oProject = oDesktop.SetActiveProject("exp")
Set oDesign = oProject.SetActiveDesign("exp_proj")
Set oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=", "1.8mm", "YCenter:=",  _
  "0mm", "ZCenter:=", "0mm", "Radius:=", "0.2mm", "Height:=", "0.4mm", "WhichAxis:=",  _
  "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=", "Cylinder2", "Flags:=",  _
  "", "Color:=", "(132 132 193)", "Transparency:=", 0.400000005960464, "PartCoordinateSystem:=",  _
  "Global", "UDMId:=", "", "MaterialValue:=", "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=",  _
  true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "Cylinder2"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oProject.Save
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=", "-3mm", "YCenter:=",  _
  "0mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=", "3.15mm", "WhichAxis:=",  _
  "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=", "via", "Flags:=", "", "Color:=",  _
  "(132 132 193)", "Transparency:=", 0.400000005960464, "PartCoordinateSystem:=",  _
  "Global", "UDMId:=", "", "MaterialValue:=", "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=",  _
  true)
oEditor.Delete Array("NAME:Selections", "Selections:=", "Cylinder2")
oEditor.Delete Array("NAME:Selections", "Selections:=", "Cylinder1")
oProject.Save
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=", "-3mm", "YCenter:=",  _
  "0mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=", "3.15mm", "WhichAxis:=",  _
  "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=", "via_1", "Flags:=", "", "Color:=",  _
  "(132 132 193)", "Transparency:=", 0.400000005960464, "PartCoordinateSystem:=",  _
  "Global", "UDMId:=", "", "MaterialValue:=", "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=",  _
  true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.DuplicateAlongLine Array("NAME:Selections", "Selections:=", "via_1", "NewPartsModelFlag:=",  _
  "Model"), Array("NAME:DuplicateToAlongLineParameters", "CreateNewObjects:=", true, "XComponent:=",  _
  "1mm", "YComponent:=", "1mm", "ZComponent:=", "0mm", "NumClones:=", "3"), Array("NAME:Options", "DuplicateAssignments:=",  _
  false)
oEditor.Delete Array("NAME:Selections", "Selections:=", "via")
oEditor.Delete Array("NAME:Selections", "Selections:=", "via_1")
oEditor.Delete Array("NAME:Selections", "Selections:=", "via_1_1")
oEditor.Delete Array("NAME:Selections", "Selections:=", "via_1_2")
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=", "-3mm", "YCenter:=",  _
  "0mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=", "3.15mm", "WhichAxis:=",  _
  "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=", "via0", "Flags:=", "", "Color:=",  _
  "(132 132 193)", "Transparency:=", 0.400000005960464, "PartCoordinateSystem:=",  _
  "Global", "UDMId:=", "", "MaterialValue:=", "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=",  _
  true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via0"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-3.07882562659mm", "YCenter:=", "1mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via1", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via1"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-3.1638647326mm", "YCenter:=", "2mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via2", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via2"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-3.25560709941mm", "YCenter:=", "3mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via3", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via3"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-3.35458111578mm", "YCenter:=", "4mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via4", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via4"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-3.46135682101mm", "YCenter:=", "5mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via5", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via5"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-3.5765491881mm", "YCenter:=", "6mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via6", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via6"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-3.70082166571mm", "YCenter:=", "7mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via7", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via7"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-3.83488999923mm", "YCenter:=", "8mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via8", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via8"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-3.97952635315mm", "YCenter:=", "9mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via9", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via9"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-4.1355637583mm", "YCenter:=", "10mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via10", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via10"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-4.30390090968mm", "YCenter:=", "11mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via11", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via11"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-4.4855073425mm", "YCenter:=", "12mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via12", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via12"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-4.68142901617mm", "YCenter:=", "13mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via13", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via13"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-4.89279433854mm", "YCenter:=", "14mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via14", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via14"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-5.12082066489mm", "YCenter:=", "15mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via15", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via15"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-5.36682130928mm", "YCenter:=", "16mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via16", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via16"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-5.63221310862mm", "YCenter:=", "17mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via17", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via17"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-5.91852458283mm", "YCenter:=", "18mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via18", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via18"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-6.2274047384mm", "YCenter:=", "19mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via19", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via19"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-6.56063256577mm", "YCenter:=", "20mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via20", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via20"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-6.92012728543mm", "YCenter:=", "21mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via21", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via21"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-7.30795940163mm", "YCenter:=", "22mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via22", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via22"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-7.7263626274mm", "YCenter:=", "23mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via23", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via23"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-8.17774674961mm", "YCenter:=", "24mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via24", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via24"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-8.66471150809mm", "YCenter:=", "25mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via25", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via25"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=",  _
  "-9.19006156879mm", "YCenter:=", "26mm", "ZCenter:=", "0mm", "Radius:=", "0.4mm", "Height:=",  _
  "3.15mm", "WhichAxis:=", "Z", "NumSides:=", "0"), Array("NAME:Attributes", "Name:=",  _
  "via26", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "via26"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.CreateBox Array("NAME:BoxParameters", "XPosition:=", "-2.6mm", "YPosition:=",  _
  "0mm", "ZPosition:=", "3.15mm", "XSize:=", "12.6mm", "YSize:=", "27mm", "ZSize:=",  _
  "99.85mm"), Array("NAME:Attributes", "Name:=", "Box1", "Flags:=", "", "Color:=",  _
  "(132 132 193)", "Transparency:=", 0.400000005960464, "PartCoordinateSystem:=",  _
  "Global", "UDMId:=", "", "MaterialValue:=", "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=",  _
  true)
oDesign.ChangeProperty Array("NAME:AllTabs", Array("NAME:LocalVariableTab", Array("NAME:PropServers",  _
  "LocalVariables"), Array("NAME:NewProps", Array("NAME:D", "PropType:=", "VariableProp", "UserDef:=",  _
  true, "Value:=", "18.6mm"), Array("NAME:a", "PropType:=", "VariableProp", "UserDef:=",  _
  true, "Value:=", "6mm"), Array("NAME:b", "PropType:=", "VariableProp", "UserDef:=",  _
  true, "Value:=", "3.15mm"))))
oProject.Save
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "Box1:CreateBox:1"), Array("NAME:ChangedProps", Array("NAME:Position", "X:=", "-D/2", "Y:=",  _
  "0mm", "Z:=", "3.15mm"), Array("NAME:XSize", "Value:=", "D"))))
oProject.Save
oDesign.ChangeProperty Array("NAME:AllTabs", Array("NAME:LocalVariableTab", Array("NAME:PropServers",  _
  "LocalVariables"), Array("NAME:NewProps", Array("NAME:Len", "PropType:=", "VariableProp", "UserDef:=",  _
  true, "Value:=", "26.2mm"))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "Box1:CreateBox:1"), Array("NAME:ChangedProps", Array("NAME:YSize", "Value:=", "Len"), Array("NAME:ZSize", "Value:=",  _
  "b"), Array("NAME:Position", "X:=", "-D/2", "Y:=", "0mm", "Z:=", "0"))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "Box1:CreateBox:1"), Array("NAME:ChangedProps", Array("NAME:Position", "X:=", "-D/2", "Y:=",  _
  "-1mm", "Z:=", "0"))))
oDesign.ChangeProperty Array("NAME:AllTabs", Array("NAME:LocalVariableTab", Array("NAME:PropServers",  _
  "LocalVariables"), Array("NAME:ChangedProps", Array("NAME:Len", "Value:=", "27.2mm"))))
oEditor.DuplicateMirror Array("NAME:Selections", "Selections:=",  _
  "via0,via1,via2,via3,via4,via5,via6,via7,via8,via9,via10,via11,via12,via13,via1" & _ 
  "4,via15,via16,via17,via18,via19,via20,via21,via22,via23,via24,via25,via26", "NewPartsModelFlag:=",  _
  "Model"), Array("NAME:DuplicateToMirrorParameters", "DuplicateMirrorBaseX:=", "0mm", "DuplicateMirrorBaseY:=",  _
  "0mm", "DuplicateMirrorBaseZ:=", "0mm", "DuplicateMirrorNormalX:=", "1mm", "DuplicateMirrorNormalY:=",  _
  "0mm", "DuplicateMirrorNormalZ:=", "0mm"), Array("NAME:Options", "DuplicateAssignments:=",  _
  false)
oEditor.DuplicateAlongLine Array("NAME:Selections", "Selections:=", "via0", "NewPartsModelFlag:=",  _
  "Model"), Array("NAME:DuplicateToAlongLineParameters", "CreateNewObjects:=", true, "XComponent:=",  _
  "1mm", "YComponent:=", "0mm", "ZComponent:=", "0mm", "NumClones:=", "6"), Array("NAME:Options", "DuplicateAssignments:=",  _
  false)
oEditor.CreateRectangle Array("NAME:RectangleParameters", "IsCovered:=", true, "XStart:=",  _
  "-9.3mm", "YStart:=", "-1mm", "ZStart:=", "3.15mm", "Width:=", "18.6mm", "Height:=",  _
  "27.2mm", "WhichAxis:=", "Z"), Array("NAME:Attributes", "Name:=", "Rectangle1", "Flags:=",  _
  "", "Color:=", "(132 132 193)", "Transparency:=", 0.400000005960464, "PartCoordinateSystem:=",  _
  "Global", "UDMId:=", "", "MaterialValue:=", "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=",  _
  true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "Rectangle1"), Array("NAME:ChangedProps", Array("NAME:Name", "Value:=", "Top_Patch"), Array("NAME:Color", "R:=",  _
  128, "G:=", 128, "B:=", 0))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "Top_Patch:CreateRectangle:1"), Array("NAME:ChangedProps", Array("NAME:Position", "X:=",  _
  "-D/2", "Y:=", "-1mm", "Z:=", "b"), Array("NAME:XSize", "Value:=", "Len"), Array("NAME:YSize", "Value:=",  _
  "Len"), Array("NAME:XSize", "Value:=", "D"))))
oEditor.CreateRectangle Array("NAME:RectangleParameters", "IsCovered:=", true, "XStart:=",  _
  "-9.3mm", "YStart:=", "-1mm", "ZStart:=", "3.15mm", "Width:=", "18.6mm", "Height:=",  _
  "27.2mm", "WhichAxis:=", "Z"), Array("NAME:Attributes", "Name:=", "Rectangle1", "Flags:=",  _
  "", "Color:=", "(132 132 193)", "Transparency:=", 0.400000005960464, "PartCoordinateSystem:=",  _
  "Global", "UDMId:=", "", "MaterialValue:=", "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=",  _
  true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "Rectangle1"), Array("NAME:ChangedProps", Array("NAME:Name", "Value:=", "GND"), Array("NAME:Color", "R:=",  _
  128, "G:=", 128, "B:=", 0))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "GND:CreateRectangle:1"), Array("NAME:ChangedProps", Array("NAME:Position", "X:=", "-D/2", "Y:=",  _
  "-1mm", "Z:=", "0mm"), Array("NAME:XSize", "Value:=", "D"), Array("NAME:YSize", "Value:=",  _
  "Len"))))
oEditor.DeleteLastOperation Array("NAME:Selections", "Selections:=", "via0", "NewPartsModelFlag:=",  _
  "Model")
oDesign.ChangeProperty Array("NAME:AllTabs", Array("NAME:LocalVariableTab", Array("NAME:PropServers",  _
  "LocalVariables"), Array("NAME:ChangedProps", Array("NAME:Len", "Value:=", "26.2mm"))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "GND:CreateRectangle:1"), Array("NAME:ChangedProps", Array("NAME:Position", "X:=", "-D/2", "Y:=",  _
  "0", "Z:=", "0mm"))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "Top_Patch:CreateRectangle:1"), Array("NAME:ChangedProps", Array("NAME:Position", "X:=",  _
  "-D/2", "Y:=", "0", "Z:=", "b"))))
Set oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.AddMaterial Array("NAME:RF45", "CoordinateSystemType:=",  _
  "Cartesian", Array("NAME:AttachedData"), Array("NAME:ModifierData"), "permittivity:=",  _
  "4.5", "dielectric_loss_tangent:=", "0.0037")
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "Box1"), Array("NAME:ChangedProps", Array("NAME:Name", "Value:=", "Substrate"), Array("NAME:Material", "Value:=",  _
  "" & Chr(34) & "RF45" & Chr(34) & ""))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "Substrate:CreateBox:1"), Array("NAME:ChangedProps", Array("NAME:Position", "X:=", "-D/2", "Y:=",  _
  "0", "Z:=", "0"))))
oEditor.CreateRectangle Array("NAME:RectangleParameters", "IsCovered:=", true, "XStart:=",  _
  "-3mm", "YStart:=", "-0.4mm", "ZStart:=", "3.15mm", "Width:=", "-3.15mm", "Height:=",  _
  "5.85560709941mm", "WhichAxis:=", "Y"), Array("NAME:Attributes", "Name:=",  _
  "Rectangle1", "Flags:=", "", "Color:=", "(132 132 193)", "Transparency:=",  _
  0.400000005960464, "PartCoordinateSystem:=", "Global", "UDMId:=", "", "MaterialValue:=",  _
  "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=", true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "Rectangle1"), Array("NAME:ChangedProps", Array("NAME:Name", "Value:=", "FeedPort"), Array("NAME:Color", "R:=",  _
  128, "G:=", 0, "B:=", 0))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "FeedPort:CreateRectangle:1"), Array("NAME:ChangedProps", Array("NAME:Position", "X:=",  _
  "-D/2", "Y:=", "-0.4mm", "Z:=", "3.15mm"), Array("NAME:XSize", "Value:=", "D"), Array("NAME:ZSize", "Value:=",  _
  "-b"), Array("NAME:Position", "X:=", "-D/2", "Y:=", "0", "Z:=", "b"))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "FeedPort:CreateRectangle:1"), Array("NAME:ChangedProps", Array("NAME:Position", "X:=",  _
  "-D/3", "Y:=", "0", "Z:=", "b"), Array("NAME:Position", "X:=", "-D/3", "Y:=", "0", "Z:=",  _
  "0"), Array("NAME:ZSize", "Value:=", "b*3"))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "FeedPort:CreateRectangle:1"), Array("NAME:ChangedProps", Array("NAME:XSize", "Value:=",  _
  "D/3*2"))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "FeedPort:CreateRectangle:1"), Array("NAME:ChangedProps", Array("NAME:ZSize", "Value:=",  _
  "b*2"), Array("NAME:Position", "X:=", "-D/4", "Y:=", "0", "Z:=", "0"), Array("NAME:XSize", "Value:=",  _
  "D/4*2"))))
oDesign.ChangeProperty Array("NAME:AllTabs", Array("NAME:LocalVariableTab", Array("NAME:PropServers",  _
  "LocalVariables"), Array("NAME:NewProps", Array("NAME:rad", "PropType:=", "VariableProp", "UserDef:=",  _
  true, "Value:=", "0.4mm"), Array("NAME:p", "PropType:=", "VariableProp", "UserDef:=",  _
  true, "Value:=", "1mm"))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "Substrate:CreateBox:1"), Array("NAME:ChangedProps", Array("NAME:YSize", "Value:=",  _
  "Len+rad"), Array("NAME:Position", "X:=", "-D/2", "Y:=", "-rad", "Z:=", "0"))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "Top_Patch:CreateRectangle:1"), Array("NAME:ChangedProps", Array("NAME:Position", "X:=",  _
  "-D/2", "Y:=", "-rad", "Z:=", "b"))))
oDesign.ChangeProperty Array("NAME:AllTabs", Array("NAME:LocalVariableTab", Array("NAME:PropServers",  _
  "LocalVariables"), Array("NAME:ChangedProps", Array("NAME:Len", "Value:=", "26.2+rad"))))
oDesign.ChangeProperty Array("NAME:AllTabs", Array("NAME:LocalVariableTab", Array("NAME:PropServers",  _
  "LocalVariables"), Array("NAME:ChangedProps", Array("NAME:Len", "Value:=", "26.2mm+rad"))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "Substrate:CreateBox:1"), Array("NAME:ChangedProps", Array("NAME:YSize", "Value:=", "Len"))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "GND:CreateRectangle:1"), Array("NAME:ChangedProps", Array("NAME:Position", "X:=", "-D/2", "Y:=",  _
  "-rad", "Z:=", "0mm"))))
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "FeedPort:CreateRectangle:1"), Array("NAME:ChangedProps", Array("NAME:Position", "X:=",  _
  "-D/4", "Y:=", "-rad", "Z:=", "0"))))
oEditor.CreateBox Array("NAME:BoxParameters", "XPosition:=", "-16mm", "YPosition:=",  _
  "0mm", "ZPosition:=", "-26mm", "XSize:=", "26mm", "YSize:=", "40mm", "ZSize:=",  _
  "-6mm"), Array("NAME:Attributes", "Name:=", "Box1", "Flags:=", "", "Color:=",  _
  "(132 132 193)", "Transparency:=", 0.400000005960464, "PartCoordinateSystem:=",  _
  "Global", "UDMId:=", "", "MaterialValue:=", "" & Chr(34) & "vacuum" & Chr(34) & "", "SolveInside:=",  _
  true)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers",  _
  "Box1"), Array("NAME:ChangedProps", Array("NAME:Name", "Value:=", "AirBox"))), Array("NAME:Geometry3DCmdTab", Array("NAME:PropServers",  _
  "Box1:CreateBox:1"), Array("NAME:ChangedProps", Array("NAME:Position", "X:=", "-D/2-4mm", "Y:=",  _
  "0mm", "Z:=", "-26mm"), Array("NAME:XSize", "Value:=", "D+8mm"), Array("NAME:YSize", "Value:=",  _
  "Len+4mm"), Array("NAME:Position", "X:=", "-D/2-4mm", "Y:=", "-rad", "Z:=", "-26mm"), Array("NAME:Position", "X:=",  _
  "-D/2-4mm", "Y:=", "-rad", "Z:=", "-4mm"), Array("NAME:ZSize", "Value:=", "b+8mm"))))
Set oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignRadiation Array("NAME:Rad1", "Objects:=", Array("AirBox"), "IsIncidentField:=",  _
  false, "IsEnforcedField:=", false, "IsFssReference:=", false, "IsForPML:=",  _
  false, "UseAdaptiveIE:=", false, "IncludeInPostproc:=", true)
oModule.AssignPerfectE Array("NAME:PerfE1", "Objects:=", Array("GND", "Top_Patch"), "InfGroundPlane:=",  _
  false)
oModule.AssignWavePort Array("NAME:1", "Objects:=", Array("FeedPort"), "NumModes:=",  _
  1, "RenormalizeAllTerminals:=", true, "UseLineModeAlignment:=", false, "DoDeembed:=",  _
  false, Array("NAME:Modes", Array("NAME:Mode1", "ModeNum:=", 1, "UseIntLine:=", true, Array("NAME:IntLine", "Start:=", Array( _
  "0mm", "-0.4mm", "-8.54191142405279e-016mm"), "End:=", Array( _
  "8.88178419700125e-016mm", "-0.399999999999999mm", "6.3mm")), "CharImp:=", "Zpi", "AlignmentGroup:=",  _
  0)), "ShowReporterFilter:=", false, "ReporterFilter:=", Array(true), "UseAnalyticAlignment:=",  _
  false)
oEditor.Subtract Array("NAME:Selections", "Blank Parts:=", "Substrate", "Tool Parts:=",  _
  "via26,via26_1"), Array("NAME:SubtractParameters", "KeepOriginals:=", true)
Set oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup "HfssDriven", Array("NAME:Setup1", "Frequency:=", "24GHz", "PortsOnly:=",  _
  false, "MaxDeltaS:=", 0.02, "UseMatrixConv:=", false, "MaximumPasses:=", 20, "MinimumPasses:=",  _
  1, "MinimumConvergedPasses:=", 1, "PercentRefinement:=", 30, "IsEnabled:=",  _
  true, "BasisOrder:=", 1, "UseIterativeSolver:=", false, "DoLambdaRefine:=",  _
  true, "DoMaterialLambda:=", true, "SetLambdaTarget:=", false, "Target:=",  _
  0.3333, "UseMaxTetIncrease:=", false, "PortAccuracy:=", 2, "UseABCOnPort:=",  _
  false, "SetPortMinMaxTri:=", false, "EnableSolverDomains:=", false, "SaveRadFieldsOnly:=",  _
  false, "SaveAnyFields:=", true, "NoAdditionalRefinementOnImport:=", false)
oModule.InsertFrequencySweep "Setup1", Array("NAME:Sweep", "IsEnabled:=", true, "SetupType:=",  _
  "LinearStep", "StartValue:=", "15GHz", "StopValue:=", "30GHz", "StepSize:=",  _
  "0.1GHz", "Type:=", "Fast", "SaveFields:=", true, "SaveRadFields:=", false, "GenerateFieldsForAllFreqs:=",  _
  false, "ExtrapToDC:=", false)
oProject.Save
oProject.Save
