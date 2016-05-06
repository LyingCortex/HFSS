Dim oAnsoftApp
Dim oDesktop
Dim oProject
Dim oDesign
Dim oEditor
Dim oModule
Set oAnsoftApp = CreateObject("AnsoftHfss.HfssScriptInterface")
Set oDesktop = oAnsoftApp.GetAppDesktop()
Set oProject = oDesktop.GetActiveProject ()
Set oDesign = oProject.GetActiveDesign ()
Set oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateCylinder Array("NAME:CylinderParameters", "XCenter:=", "1mm", "YCenter:=","1mm", "ZCenter:=", "1mm", "Radius:=", "1mm", "Height:=", "2mm", "WhichAxis:=", "Z","NumSides:=", "0"), Array("NAME:Attributes", "Name:=", "via_my", "Flags:=","", "Color:=", "(132 132 193)", "Transparency:=", 0.4,"PartCoordinateSystem:=",  "Global", "UDMId:=", "", "MaterialValue:=", "" & Chr(34) & "pec" & Chr(34) & "", "SolveInside:=", false)
oEditor.ChangeProperty Array("NAME:AllTabs", Array("NAME:Geometry3DAttributeTab", Array("NAME:PropServers", "via_my"), Array("NAME:ChangedProps", Array("NAME:Material", "Value:=", "" & Chr(34) & "pec" & Chr(34) & ""))))
oEditor.DuplicateAlongLine Array("NAME:Selections", "Selections:=", "via_my", "NewPartsModelFlag:=", "Model"),Array("NAME:DuplicateToAlongLineParameters", "CreateNewObjects:=", true, "XComponent:=","1mm","YComponent:=", "2mm", "ZComponent:=", "3mm", "NumClones:=", "6"),Array("NAME:Options", "DuplicateAssignments:=", true)
