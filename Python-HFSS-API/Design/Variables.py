# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:31:47 2017

@author: LY

Functions:
    GetDesignVaribles
    GetProjectVaribles
    AddDesignVarible
    AddDesignVaribleWithoutUnit
    DeleteDesignVaribles
    AddVaribleList  
    


"""

def GetDesignVaribles(oDesign):
    return oDesign.GetVariables()


def GetProjectVaribles(oProject):
    return oProject.GetVariables()

def AddDesignVariable(oDesign, variable, value,  unit = 'mm'):
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
					"NAME:"+variable,
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, [str(value)+unit if type(value) != type('d') else value][0]  ## 在一句话中完成了判断，未验证
				]
			]
		]
	]) 


def AddDesignVariableWithoutUnit(oDesign, variable, value):
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
					"NAME:"+variable,
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, [str(value) if type(value) != type('d') else value][0]  #
				]
			]
		]
	]) 


def DeleteDesignVaribles(oDesign, variable):
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
				variable
			]
		]
	])  

    
    
def AddVariableList(oDesign, variable_value):
    local_var_array = GetDesignVaribles(oDesign)
    for vv in variable_value:
        Leng=len(vv)
        if vv[0] not in local_var_array:
            if Leng == 3:   # the unit is assigned
                AddDesignVariable(oDesign, vv[0], vv[1], unit=vv[2])
            else:
                AddDesignVariable(oDesign, vv[0], vv[1])
        else:
            DeleteDesignVaribles(oDesign, vv[0])
            if Leng== 3:
                AddDesignVariable(oDesign, vv[0], vv[1], unit=vv[2])
            else:
                AddDesignVariable(oDesign, vv[0], vv[1])


