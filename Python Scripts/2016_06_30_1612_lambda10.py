# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:09:27 2016

@author: LY
"""

import math

#er = 2.2
#f = 15  # GHz
#c = 300  ## compared with mm
#a = 12



er = 4.5
f = 22.15  # GHz
c = 300  ## compared with mm
a = 6

wg_10 = math.pi * 2 / math.sqrt(er*(2*math.pi*f/c)**2-(math.pi/a)**2)
wg = 300/f/er**0.5

wg_10_1 = wg/math.sqrt(1-(wg/2/a)**2)