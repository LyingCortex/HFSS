# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:48:45 2017

@author: LY
"""

def ChangeColor(oEditor, RGB, select_name):
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

	
'''
change material
'''

def ChangeMaterial(oEditor, name, material):
    oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				name
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material",
					"Value:="		, "\"" + material + "\""
				]
			]
		]
	])


def Rename(oEditor, select_name, changed_name1):
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
	

def RenameDesignInstance(new_design_name, oDesign):
    
    old_design_name = oDesign.GetName()
    oDesign.RenameDesignInstance(old_design_name, new_design_name)
	
