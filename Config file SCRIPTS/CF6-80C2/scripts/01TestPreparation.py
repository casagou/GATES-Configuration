import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 01TestPreparation.py
#******************************************************************************
#*  AUTHOR: <J.Si>
#*
#*  DESCRIPTION:
#*  CF6-80 ENGINE MANUAL GEK92451
#*  EM 72-00-00 ENGINE TESTING 000
#*
#*  DATE: 04/04/2017 2:53:58 PM
#*
#*  MODIFICATIONS:
#*    REV    DATE         WHO  NCR    DESCRIPTION
#*    ----  ----------    ---  -----  --------------------------------------------------
#*
#*
#*    1.0   01/04/20      JSi   ---    Initial write
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
TestYes = None
OilTop = None
lvSttop = None
lvStmcd = None
lvCSDtop = None
InEx = None
In_FOD = None
lvAdapt = None
lvCowls = None
lvpad = None
preCK = None
lvFuelOn = None

# Channel Registration
channel("TRAFILTR,FN")



instruction("With the engine coupled to bed,turn electrical power ON (28 V DC and 115 V AC at 400 Hz)")

note("Electrical Power ON (28 V DC and 115 V AC at 400 Hz)")


instruction("Tare Working Thrust Cell ")


do_fullset(10,"Tare Fullset","Tare")

result("Working Cell reads= {} lbs".format(str(getCV("FN"))),REPORT + "IdleLeakCheck")



instruction("Service engine as required")

note("Service per Servicing Substask 72-00-00-610-051")

caution("DO NOT OVERFILL CSD AND THE OIL TANK")


OilTop = prompt_boo("Was Engine oil level checked and topped?")

if OilTop:
	result("Oil level is checked and topped",REPORT + "TestPreparation")

else:
	result("Oil levels not checked and topped",REPORT + "TestPreparation")

	pass

instruction("Service engine starter as required")

lvSttop = prompt_boo("Was starter oil level checked and topped?")

if lvSttop:
	result("Starter oil level checked and topped",REPORT + "TestPreparation")

else:
	result("Starter Oil level not checked and topped",REPORT + "TestPreparation")

	pass

instruction("Check starter MCD as required")

lvStmcd = prompt_boo("Was starter MCD checked ?")

if lvStmcd:
	result("Starter MCD checked OK",REPORT + "TestPreparation")

else:
	result("Starter MCD not OK",REPORT + "TestPreparation")

	pass

instruction("Service engine IDG as required",SKIP)

note("Press PLAY if IDG installed or skip if NOT")

if SkipGV:
	result("No IDG installed",REPORT + "TestPreparation")

else:
	lvCSDtop = prompt_boo("Was IDG oil level checked and topped?")

	if lvCSDtop:
		result("IDG oil level checked and topped",REPORT + "TestPreparation")

	else:
		result("IDG Oil level not checked and topped",REPORT + "TestPreparation")

		pass
	pass

instruction("Ensure plug is intalled on G/B open pad")

lvpad = prompt_boo("Was G/B open pad plugged?")

if lvpad:
	result("G/B pad checked OK",REPORT + "TestPreparation")

else:
	result("G/B pad not OK",REPORT + "TestPreparation")

	pass


instruction("Check inlet and exhaust")

InEx = prompt_boo("Were inlet and exhaust found satisfactory when checked?")

if InEx:
	result("Inlet and exhaust checked OK.",REPORT + REPORT + "TestPreparation")

else:
	result("A problem was found in the inlet or exhaust.",REPORT + "TestPreparation")

	pass

instruction("Check all Adapters services and drain connections for security")

lvAdapt = prompt_boo("Were adapters connections checked?")

if lvAdapt:
	result("Adapters connections checked OK.",REPORT + "TestPreparation")

else:
	result("A problem was found with the connections.",REPORT + "TestPreparation")

	pass

instruction("Check Test cowlings for security and integrity")

lvCowls = prompt_boo("Were cowlings found satisfactory when checked?")

if lvCowls:
	result("Cowling checked OK.",REPORT + "TestPreparation")

else:
	result("A problem was found with the cowlings.",REPORT + "TestPreparation")

	pass

instruction("Make a general inspection of the engine,")

note("Test Cell area for security and integrity.")

preCK = prompt_boo("Is the PRESTART CHECKS has been carried out?")

if preCK:
	result("Engine Installation inspection performed",REPORT + "TestPreparation")

	result("Engine Controls inspection performed",REPORT + "TestPreparation")

else:
	result("Operator skipped the PRESTART CHECKS inspection")

	pass

instruction("Check fuel shutoff lever for security and integrity")

lvFuelOn = prompt_boo("Fuel shutoff open/close found OK when checked?")

if lvFuelOn:
	result("Fuel ON/OFF checked OK.",REPORT + "TestPreparation")

else:
	result("A problem was found with Fuel ON/Off lever.",REPORT + "TestPreparation")

	pass


instruction("Set Power Lever until TRA equals 30 Deg")

note("and set mechanical Stop")

wait("TRAFILTR = 35",30,1.0,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"TRA is not reading 35 degrees.")

if SkipGV:
	result("Operator skipped Power Lever adjustment check",REPORT + "TestPreparation")

else:
	result("Power Lever adjustment is at Idle",REPORT + "TestPreparation")

	pass


instruction("Move Power Lever until TRA equals 88 Deg")

note("and set mechanical Stop")

wait("TRAFILTR = 88",30,0.5,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"TRA is not reading 88 degrees.")

if SkipGV:
	result("Operator skipped Power Lever adjustment check",REPORT + "TestPreparation")

else:
	result("Power Lever adjustment is at Maximum foward mechanical stop",REPORT + "TestPreparation")

	pass


instruction("Return Power Lever to Idle stop")

wait("TRAFILTR = 35",30,1.0,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"TRA is not reading 30 degree after 30 s")


if SkipGV:
	result("Operator skipped Power Lever adjustment check",REPORT + "TestPreparation")

else:
	result("Power Lever adjustment is at Idle",REPORT + "TestPreparation")

	pass

In_FOD = prompt_boo("Has Test cell cleanliness for FOD been performed?")

if In_FOD:
	result("FOD checked OK.",REPORT + "TestPreparation")

else:
	result("Please perform FOD inspection before start.",REPORT + "TestPreparation")

	pass
#*

TestYes = prompt_boo("Is Test Preparation completed?")

if TestYes:
	result("Test Preparation completed and authorized.",REPORT + "Test1")

	pass
