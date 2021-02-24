import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 05AbortStart.py
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:REFERANCE CFM56-7B ENGINE MANUAL 72-00-00 TESTING 000
#*  Abort Start
#*
#*  DATE: 1/6/2021
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*  
#*
#******************************************************************************

# Channel Registration
channel("EngStrtLvr,StrtSwitch")


note("NOTE: This TP is to be used only as a part of Start TP")


instruction("Set ENGINE START LEVER to CUTOFF")

wait("EngStrtLvr = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel is not OFF after 10 seconds")

if skipgv:
	result("Operator skipped Fuel OFF check {} AbortStart ".format(REPORT))

	pass

instruction("SET ENGINE START SWITCH to OFF")

wait("StrtSwitch = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "START SWITCH is not OFF ")



delay(3)



instruction("Close Facility Air supply valve")

wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")
