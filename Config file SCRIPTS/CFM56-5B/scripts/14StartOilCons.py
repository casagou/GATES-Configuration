import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 16StartOilCons.py
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:
#*  Start Oil Consumption Check
#*
#*  DATE: 12/10/2020 
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*
#*
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
HighPower = None
OilConYes = None

# Channel Registration

channel("Eng_On,OilCSStr,OilCSEnd,N1K,N1MC")


HighPower = prompt_boo("Was the engine warmed up for five minutes at high power and currently at MIN IDLE?")

if not HighPower:
	instruction("Slowly accelerate (2 min) to Max Cont for 5 min.")

	wait("N1K ="+str(getCV("N1MC")) , 60, 5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Did not reach Max Cont in 60 s ")

	delay(300)

	instruction("Slowly decelerate (30 sec) to GI and stabilize for 5 minutes. ")

	wait("GIFlag = 1", 80, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach GI in 80 s ")

	delay(300)

	pass
    
OilConYes = prompt_boo("Start oil consumption check?")

if not OilConYes:
	result("Proceed with Performance check.")
quit()
pass

set_channel("OilCSEnd",0)
set_channel("OilCSStr", 1)

result("Oil consumption check started.")

delay(5)   
    

