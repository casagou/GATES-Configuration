import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 14TestConclusion.py
#******************************************************************************
#*  AUTHOR: J.Si
#*
#*  DESCRIPTION:
#*  CF6-50 ENGINE MANUAL GEK50481 - Rev 87,07/15/2017
#*  EM 72-00-00 ENGINE TESTING
#*
#*  DATE: 04/04/2008 10:54:01 AM
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*    ----------   ---  -----  --------------------------------------------------
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
Conclude = None
lvFuelOil = None
lvBothIGN = None
lvNo1IGN = None
lvNo2IGN = None
lvHPBleed = None
lvHPBldOK = None
lvOilFil = None
lvMCDOK = None
lvOilLevel = None
OilSysInh = None
InhOilLtrs = None
FuelSysInh = None
OLeaks = None
FLeaks = None
In_ExhOK = None

Conclude = prompt_boo("Do you want to conclude this engine testing?")

if Conclude:
	lvFuelOil = prompt_boo("Was Low Oil pressure indication OK during testing?")

	if lvFuelOil:
		result("Low Oil pressure indication OK",REPORT + "LowOilPres")

	else:
		result("Low Oil pressure indication NOT OK",REPORT + "LowOilPres")

		pass
	
	lvNo1IGN = prompt_boo("Was Ignitor 1 operation satisfactory during test?")

	if lvNo1IGN:
		result("Ignitor 1 operation OK",REPORT + "A_IGNIT")

	else:
		result("Ignitor 1 operation NOT OK",REPORT + "A_IGNIT")

		pass
	
	lvNo2IGN = prompt_boo("Was Ignitor 2 operation satisfactory during test?")

	if lvNo2IGN:
		result("Ignitor 2 operation OK",REPORT + "B_IGNIT")

	else:
		result("Ignitor 2 operation NOT OK",REPORT + "B_IGNIT")

		pass
	
	lvOilFil = prompt_boo("Was Oil Filter OK during test?")

	if lvOilFil:
		result("Oil Filter OK",REPORT + "OILFILTER")

	else:
		result("Oil Filter NOT OK",REPORT + "OILFILTER")

		pass
	
	lvMCDOK = prompt_boo("Were all Magnetic Chip Detectors OK during test?")

	if lvMCDOK:
		result("Magnetic Chip Detectors OK",REPORT + "MCDCHECK")

	else:
		result("Magnetic Chip Detectors NOT OK",REPORT + "MCDCHECK")

		pass
	
	lvOilLevel = prompt_boo("Were Oil levels found satisfactory when checked during test?")

	if lvOilLevel:
		result("Oil Levels OK",REPORT + "OILLEVEL")

	else:
		result("Oil Levels NOT OK",REPORT + "OILLEVEL")

		pass
	
	OLeaks = prompt_boo("Was there any oil leaks found?")

	if OLeaks:
		result("Oil leaks were found.",REPORT + "FINLEAKS")

		result("See Snag Sheets for Oil leak detail.",REPORT + "FINLEAKS")

		result("No other oil leaks were found.",REPORT + "FINLEAKS")

	else:
		result("No Oil Leaks were found",REPORT + "FINLEAKS")

		pass
	
	In_ExhOK = prompt_boo("Was inlet and exhaust check satisfactory?")

	if In_ExhOK:
		result("Inlet and exhaust checked OK.",REPORT + "InExCheck")

	else:
		result("A problem was found in the inlet or exhaust.",REPORT + "InExCheck",RED)

		pass
	
	OilSysInh = prompt_boo("Did you inhibit oil system")

	if OilSysInh:
		result("Oil system inhibited",REPORT + "OILINHIB")

	else:
		result("Oil system not inhibited",REPORT + "OILINHIB")

		pass
	
	FuelSysInh = prompt_boo("Did you inhibit fuel system?")

	if FuelSysInh:
		result("Fuel system inhibited",REPORT + "FUELINHIB")

	else:
		result("Fuel system not inhibited",REPORT + "FUELINHIB")

		pass
	
	do_fullset(0,"Test finish","TestConclusion")

	pass
