import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 02ContinueTest.tps
#******************************************************************************
#*  AUTHOR: Christian Bourgeois
#*
#*  DESCRIPTION:
#*  Preparation For Test
#*
#*  DATE: 12/18/2012 2:09:26 PM
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
lvPreFuel = None
lvPreHr = None
lvPreMin = None

# Channel Registration
channel("PreRTMin,PreRTHr,PreFuel")


#show_view("GATES-RTD1", "View 0", "Start.v")

instruction("Zero all Pressure Brick Transducers or press SKIP", SKIP)


if not skipgv:
	pbs_zero()
	pass

instruction("Record previous test time and fuel burn")

lvPreHr = prompt_num("Enter previous run time: Hours", -1, 101, 0)

set_channel("PreRTHr", lvPreHr)

lvPreMin = prompt_num("Enter previous run time: Minutes", -1, 61, 0)

set_channel("PreRTMin", lvPreMin)

lvPreFuel = prompt_num("Enter the amount of fuel used for previous run in litres", -1, 100000, 0)

set_channel("PreFuel", lvPreFuel)

