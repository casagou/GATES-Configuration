import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#*  18TestConclustion.tps
#******************************************************************************
#*  AUTHOR: John Tamplin
#*
#*  DESCRIPTION:REFERANCE:CFM56-7B ENGINE MANUAL 72-00-00
#*  Test Conclusion
#*
#*  DATE: 1/27/2006 10:32:24 AM
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*    06/09/2006   TS          V1.05 instruction
#*    06/09/2006   TS          V1.03 iflogic modified
#*    26/01/2006   JT          Initial-Taken from 263
#*    27/01/2006   IF          Conversion to porDAS script
#*    03/25/2006   EL          "do_fullset 0" changed to "do_fullset 1"
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
Conclude = None
CSDFilOK = None
EngFilInst = None
EngFilOK = None
EngFuelFilOK = None
FuelLk = None
IDGReEng = None
In_ExhOK = None
lvMCDOK = None
OilLevelOK = None
OilLk = None
RotorRot = None
TestEqRem = None

# Channel Registration
channel("Eng_On")

#*  [lookup]
#*  channel=
#*  [validation]
#*  security=1
#*  modification="3017230253"
#*  [test script]
#*  name=TestConclusion
#/ *
#*  /
#*  Test Conclusion
#*  Ver    Date        By   Description
#*  V1.01  26 01 2006  JT   Initial-Taken from 263
# V1.03 iflogic modified
if round(getCV("Eng_On"), 4) == True:
	quit()

	pass

Conclude = prompt_boo("Do you want to conclude this engine test?")

if Conclude == False:
	quit()

	pass

instruction("Check engine for leaks")

FuelLk = prompt_boo("Are there fuel leaks?")

if FuelLk:
	result("There are fuel leaks {} LeaksCheck ".format(REPORT))

else:
	result("There are no fuel leaks {} LeaksCheck ".format(REPORT))

	pass

OilLk = prompt_boo("Are there oil leaks?")

if OilLk:
	result("There are oil leaks {} LeaksCheck ".format(REPORT))

else:
	result("There are no oil leaks {} LeaksCheck ".format(REPORT))

	pass

instruction("Check magnetic chip detectors")

lvMCDOK = prompt_boo("Were all Magnetic Chip Detectors OK during test?")

if lvMCDOK:
	result("Magnetic Chip Detectors OK {} MCDCheck ".format(REPORT))

else:
	result("Magnetic Chip Detectors NOT OK {} MCDCheck ".format(REPORT))

	pass

instruction("Check engine fuel filter")

EngFuelFilOK = prompt_boo("Is engine fuel filter OK?")

if EngFuelFilOK:
	result("Engine fuel filter is OK {} FuelFilterChk ".format(REPORT))

else:
	result("Engine fuel filter is not OK {} FuelFilterChk ".format(REPORT))

	pass

instruction("Check engine oil filter")

EngFilOK = prompt_boo("Is engine filter OK?")

if EngFilOK:
	result("Engine filter is OK {} OilFilterChk ".format(REPORT))

else:
	result("Engine filter is not OK {} OilFilterChk ".format(REPORT))

	pass

instruction("Install new engine oil filter if necessary")

EngFilInst = prompt_boo("Is engine filter installed?")

if EngFilInst:
	result("New engine filter is installed {} NewOilFilter ".format(REPORT))

else:
	result("New engine filter is not installed {} NewOilFilter ".format(REPORT))

	pass

#If cv_IDG = 1 Then
#	instruction "Check IDG oil filter"
#	prompt_boo "Is IDG filter OK?", CSDFilOK
#	If CSDFilOK  Then
#		result "IDG filter is OK", REPORT & "OilFilterChk"
#	Else
#		result "IDG filter is not OK", REPORT & "OilFilterChk"
#	End If
#
#	instruction "Re-Engage IDG if applicable."
#	prompt_boo "Did you Re-Engange IDG?.", IDGReEng
#	If IDGReEng Then
#		result "The IDG was Re-Engaged.", REPORT & Shutdown_Check
#	Else
#		result "The IDG was not Re-Engaged.", REPORT & Shutdown_Check
#	End If
#End If

instruction(" Check all oil levels")

OilLevelOK = prompt_boo("Were oil levels checked and topped up as required?")

if OilLevelOK:
	result("Oil levels were checked and retopped {} OilLevelCheck ".format(REPORT))

else:
	result("Oil levels are not satisfactory {} OilLevelCheck ".format(REPORT))

	pass

instruction("Check intake and exhaust.")

In_ExhOK = prompt_boo("Was intake and exhaust check satisfactory?")

if In_ExhOK:
	result("Intake and exhaust checked OK. {} IntakeExhaustCheck ".format(REPORT))

else:
	result("A problem was found in the intake or exhaust. {} IntakeExhaustCheck ".format(REPORT))

	pass

instruction("Check rotors for freedom of rotation.")

RotorRot = prompt_boo("Were rotors rotation found satisfactory when checked?")

if RotorRot:
	result("Rotors rotation found satisfactory. {} RotorRotation ".format(REPORT))

else:
	result("Rotors rotation were not satisfactory {} RotorRotation ".format(REPORT))

	pass

instruction("Remove all test equipment")

TestEqRem = prompt_boo("Is test equipment removed?")

if TestEqRem:
	result("Test equipment is removed {} TestEquipment ".format(REPORT))

else:
	result("Test equipment is not removed {} TestEquipment ".format(REPORT))

	pass

#V1.05 following instruction added
instruction("Record fullset")

do_fullset(1, "Test finish", "TestConclusion")

