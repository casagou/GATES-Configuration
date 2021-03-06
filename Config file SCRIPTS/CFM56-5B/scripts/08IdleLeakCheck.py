import sys
import os
import time
from math import *
from nxtps import *


# Global variable definition

#* 08IdleLeakCheck.tps
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:REFERANCE CFM56-5B ENGINE MANUAL 72-00-00 TESTING 002
#*  Idle Leak Check
#*
#*  DATE: 12/04/2020
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
FuelLk = None
In_ExhOK = None
OilLk = None

#Channel Registration
channel("Eng_On")

if getCV("Eng_On") == 0:
	call_tps("06AutoStart.py")
	pass

note("NOTE: Make sure that all lines, blanking plugs and harnesses")
note("      are properly secured for Idle leak check.")
delay(300)

if SkipGV:
	result("Operator skipped 5 min stabilization at IDLE {} IdleLeakCheck ".format(REPORT))
	pass

FuelLk = prompt_boo("Are there fuel leaks?")


if FuelLk:
	result("There are fuel leaks {} IdleLeakCheck ".format(REPORT))

else:
	result("There are no fuel leaks {} IdleLeakCheck ".format(REPORT))
	pass

OilLk = prompt_boo("Are there oil leaks?")


if OilLk:
	result("There are oil leaks {} IdleLeakCheck ".format(REPORT))

else:
	result("There are no oil leaks {} IdleLeakCheck ".format(REPORT))

	pass

call_tps("16Shutdown.py")


instruction("Check inlet and exhaust")

In_ExhOK = prompt_boo("Was inlet and exhaust check satisfactory?")


if In_ExhOK:
	result("Inlet and exhaust checked OK. {} InExCheck ".format(REPORT))

else:
	result("A problem was found in the inlet or exhaust. {} InExCheck ".format(REPORT))

	pass

instruction("Close and secure cowlings")

