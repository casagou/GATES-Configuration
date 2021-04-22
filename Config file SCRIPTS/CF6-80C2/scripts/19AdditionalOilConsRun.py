import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition
#*  18AdditionalOilCons.py
#******************************************************************************
#*  AUTHOR: J.Si
#*
#*  DESCRIPTION:
#*  CF6-80 ENGINE MANUAL GEK92451
#*  EM 72-00-00 ENGINE TESTING
#*  CF6-80 Oil Consumption Check
#*  TESTING 003 72-00-00
#*
#*  MODIFICATIONS:
#*    REV    DATE       WHO  NCR    DESCRIPTION
#*
#*    1.0   04/01/20    JSi   ----   New write
#*
#******************************************************************************

channel("Eng_On,N1_OBS,N185")


if getCV("Eng_On") == 0:
	call_tps("04AutoStart.py")

	pass

call_tps("14StartOilCons.py")



instruction("Accelerate to 86% N1 Power and,")

note("Stabilize engine at this point for 15 minutes.")

wait("N1_OBS="+str(round(getCV("N185"),4)),30,10,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Engine not at 86%N1 in 30 s.")

if SkipGV:
	result("Operator skipped MC power setting")

	pass
delay(300)

delay(300)

delay(300)


instruction("Decelerate to GROUND IDLE. Stabilize the engine for 5 min.")

autostart("15EndOilCons.tps")

