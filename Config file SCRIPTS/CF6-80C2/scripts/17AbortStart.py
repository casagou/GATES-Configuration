import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#*  16AbortStart.tpy
#******************************************************************************
#*  AUTHOR: J.Si
#*
#*  DESCRIPTION:
#*  CF6-80 ENGINE MANUAL GEK92451
#*  EM 72-00-00 ENGINE TESTING
#*  CF6-80 Aborted Start Procedure
#*  TESTING 003
#*
#*  MODIFICATIONS:
#*   REV   DATE      WHO  NCR    DESCRIPTION
#*    1.0   01/04/20      JS1   ---    Initial write
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****

lvtemp = None

# Channel Registration
channel("FuelLvrRunST,FCS_AirRdy,StrtVlvEnST,IGN1Pwr,IGN2Pwr,Ign1On,Ign2On")


note("NOTE: This TP is to be used only as a part of Start TP")


instruction("Set FUEL CONDITION LEVER to CUTOFF position")

wait("FuelLvrRunST = 0",10,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Fuel is not OFF after 10 s")


instruction("Turn ignition power OFF")

set_channel("IGN1Pwr",0)
set_channel("IGN2Pwr",0)

wait("Ign1On=0",3,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Right ignitor is not on")

wait("Ign2On=0",3,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Left ignitor is not ON")

if SkipGV:
	result("Operator skipped ignition OFF check",REPORT + "InitialStart")

else:
	result("Ignition is OFF",REPORT + "InitialStart")

	pass


delay(15)


instruction("Turn starter valve OFF")



wait("StrtVlvEnST=0",10,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Air valve not closed")

if SkipGV:
	result("Operator skipped Starter OFF instruction",REPORT + "AbortStart")

else:
	result("Starter turned OFF",REPORT + "AbortStart")

	pass


instruction("Turn Facility air supply OFF")

wait("FCS_AirRdy = 0",10,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Start Air not responding.  Use PLC")

if SkipGV:
	result("Operator skipped Facility Air OFF instruction",REPORT + "Shutdown")

else:
	result("Facility Air turned OFF",REPORT + "Shutdown")

	pass
