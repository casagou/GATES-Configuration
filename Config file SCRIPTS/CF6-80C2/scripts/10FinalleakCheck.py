import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 10FinalLeakCHeck.py
#******************************************************************************
#*  AUTHOR: J.Si
#*
#*  DESCRIPTION:
#*  CF6-80 ENGINE MANUAL GEK92451
#*  EM 72-00-00 ENGINE TESTING
#*  CF6-80 Starting Procedure
#*  TESTING 000
#*
#*  MODIFICATIONS:
#*    REV    DATE         WHO  NCR    DESCRIPTION
#*
#*    1.0   01/04/20      JSi   ---    Initial write
#*
#******************************************************************************


# ***** LOCAL VARIABLE DECLARATIONS *****

FuelLk = None
OilLk = None
TestYes = None

# Channel Registration

channel("Eng_On")


#channel("CellRdy,StAirOn,StAirFB,MFPump,MFPumpST,P_Fuel_Fac,OILQTY,IdleCtrlST,IdleCtrl,IGNCtrl_Act,IGNCtrl_ActST,StartControl,StrtCtrlST,AIRSTRT,StrtCtrlST,AIRSTRT,StrtVlvST, FuelOn,TLAFILTR,StartReset,LITF,tToLite,tToLiteMax,POIL,GIFlag,N1,PeakEGT,STCorr,tToIdleLim,POILC,POILCLoLim,POILCHiLim,ECUFltChaA,ECUFltChaB,HPTCDelta,LPTCDelta")


#show_view("rtd2host", "View 0", "Start.v")


if getCV("Eng_On") == 1:
	call_tps("04AutoStart.tps")

	pass


instruction("Perform inspection for leaks, proper drainage and")

note("any abnormal conditions")


FuelLk = prompt_boo("Are there fuel leaks?")

if FuelLk:
	result("There are fuel leaks", REPORT + "LeakCheck")

else:
	result("There are no fuel leaks", REPORT + "LeakCheck")

	pass

OilLk = prompt_boo("Are there oil leaks?")

if OilLk:
	result("There are oil leaks", REPORT + "LeakCheck")

else:
	result("There are no oil leaks", REPORT + "LeakCheck")

	pass

note("NOTE: If adjustment is required, correct all faults. If any")

note("      leaks were corrected, repeat the Start and Leak Check")


TestYes = prompt_boo("Is Test Final leak check completed?")

if TestYes:
	result("Test Final leak check completed and authorized.", REPORT + "Test9")

	pass

