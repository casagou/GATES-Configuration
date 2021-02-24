import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 02ContinueTest.py
#******************************************************************************
#*  AUTHOR: John Templin
#*
#*  DESCRIPTION:REFERANCE:CFM56-7B ENGINE MANUAL 72-00-00 TESTING 000
#*  Preparation For Test
#*
#*  DATE: 1/26/2006 2:09:26 PM
#*
#*  MODIFICATIONS:
#*  DATE         WHO  NCR    DESCRIPTION
#*  14Oct09      DP   1.11   Added set_channel for ID to solve problem of no Accel Target for Multi-Derivative configuration
#*  1/26/2006    IF   -----  V1.01 Conversion to proDAS script
#*  3/24/2006    EL          VentPressures channel removed
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
lvPreFuel = None
lvPreHr = None
lvPreMin = None

# Channel Registration
# 3/24/2006  EL   channel "PreRTMin,PreRTHr,PreFuel,VentPressures"
channel("PreRTMin,PreRTHr,PreFuel,ID,ID_N1TOMx")

#*  [lookup]
#*  channel=
#*  [validation]
#*  security=1
#*  modification="3017230253"
#*  [test script]
#*  name=ContinueTest
#/ *
#*  /
#*  Preparation For Test
#*  Modification History
#*  Ver   Date        By  Description
#*  V1.00 11/10/2002  JT  Initial from 263

#show_view "SMES_MGT", "Start.v", "View1",0,0,10,10
# V1.11 added the following set_channel
set_channel("ID", round(getCV("ID_N1TOMx"), 4))


instruction("Zero all Pressure Brick Transducers or press SKIP", SKIP)

if skipgv == False:
	pbs_zero()
	pass
instruction("Record previous test time and fuel burn")

lvPreHr = prompt_num("Enter previous run time: Hours", -1, 101, 0)

set_channel("PreRTHr", lvPreHr)

lvPreMin = prompt_num("Enter previous run time: Minutes", -1, 61, 0)

set_channel("PreRTMin", lvPreMin)

lvPreFuel = prompt_num("Enter the amount of fuel used for previous run in litres", -1, 100000, 0)

set_channel("PreFuel", lvPreFuel)

# 3/24/2006  EL   instruction "Record Wet Transducer tares"
# 3/24/2006  EL   set_channel VentPressures, 1
# 3/24/2006  EL   delay 2
# 3/24/2006  EL   set_channel VentPressures, 0

