import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 01TestPreparation.py
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:REFERENCE:CFM56-7B ENGINE MANUAL 72-00-00 Testing 000
#*  Preparation For Test
#*  Modification History
#*
#*  DATE: 12/14/2020
#*
#*  MODIFICATIONS:
#*  DATE         WHO  NCR    DESCRIPTION
#*  
#*
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
lvIDGdisc = None
lvIDGinst = None
lvOilLevel = None
lvPreFuel = None
lvPreHr = None
lvB27AE = None
lvPreMin = None
lvStartleak = None
lvtempvar1 = None
booPreRun = None
lvNoleak = None
lvPreTest = None

# Channel Registration
channel("Eng_On,PreRTMin,PreRTHr,PreFuel,PLA,IDGdisc,ID,ID_N1TOMx,B27A_Model,B27AE_Model")



note("TEST PREPARATION")

instruction("Ensure Facility Air and Fuel spupply are OFF")
wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")
wait("FCS_FuelRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Fuel not OFF")


instruction("Continue with Test Preparation")

booPreRun = prompt_boo("Is this a continuation of a previous test?")

if booPreRun:
	lvPreHr = prompt_num("Enter previous run time: Hours", -1, 101, 0)

	set_channel("PreRTHr", lvPreHr)

	lvPreMin = prompt_num("Enter previous run time: Minutes", -1, 61, 0)

	set_channel("PreRTMin", lvPreMin)

	lvPreFuel = prompt_num("Enter the amount of fuel used for previous run in litres", -1, 100000, 0)

	set_channel("PreFuel", lvPreFuel)

	pass


instruction("Ensure all Pre-Test inspections per ESM 72-00-00 TESTING 000")
note("have been performed prior to this point.")

lvPreTest = prompt_boo("Have all Pre-Test Inspection been completed?")


if lvPreTest:
	result("All Pre-Test Inspections completed{} PreTest ".format(REPORT))

else:
	result("Operator skipped Pre-Test Inspections {} PreTest ".format(REPORT))

	pass



lvtempvar1 = 0
if round(getCV("Eng_On"), 4) == True:
	quit()

	pass

instruction("Zero all Pressure Brick Transducers", SKIP)

if SkipGV == False:
	pbs_zero()
	pass
    
    

#/// --------- Begin V1.04 Changes ------------------

#If cv_ID = 1 and B27A_Model = 1 Then----------------------------ErrorJSi

#if round(getCV("ID"), 4) == 1 and round(getCV("B27A_Model"), 4) == 1:
	#lvB27AE = prompt_boo("Is Engine Model rating -7B27AE?")

#		If lv27AE Then-----------------------------------------ErrorJSi
	
	#if lvB27AE:
		
		#set_channel("B27AE_Model", 1)

		#result("Shunt calculation set at 12 degC for 7B27AE engine rating {} TestPrep ".format(REPORT))

	#else:
		#set_channel("B27AE_Model", 0)

		#result("Shunt calculation set at 0 degC for 7B27A-7B27A3 engine rating {} TestPrep ".format(REPORT))

		#pass
	#pass

#/// --------- End V1.04 Changes --------------------


#lvIDGinst = prompt_boo("Is the IDG installed?")

#* V1.02 if logic modified
#if lvIDGinst:
	#instruction("Check IDG disconnect")

	#set_channel("IDGDisc", 1)

	#lvIDGdisc = prompt_boo("Was IDG disconnect satisfactory?")

#* V1.02 if logic modified
	#if lvIDGdisc:
		#result("IDG disconnect operation OK {} IDGdisc ".format(REPORT))

	#else:
		#result("IDG disconnect operation NOT OK {} IDGdisc ".format(REPORT))

		#pass
	#set_channel("IDGDisc", 0)

	#pass
    
#********************************OIL CHECK***************************************************** 
   
instruction("Do an oil quantity check")

lvOilLevel = prompt_boo("Is oil level satisfactory?")


if lvOilLevel:
	result("Oil level OK {} OilLevel ".format(REPORT))

else:
	result("Oil level NOT OK.  Refill oil tank {} OilLevel ".format(REPORT))

	pass


#********************************AIR LEAK CHECK***********************************************


instruction("Do an Air System leak check")

instruction("Turn Test Cell start air ON")

wait("FCS_AirRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not ON")

note("Check for any air leaks")

instruction("Turn Test Cell start air OFF")

wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")

lvStartleak = prompt_boo("Was air leak check satisfactory?")

if lvStartleak:
	result("Starter air leak check OK {} Startleak ".format(REPORT))

else:
	result("Starter air leak check NOT OK {} Startleak ".format(REPORT))

	pass

#********************************FUEL LEAK CHECK***********************************************

instruction("Do a static fuel leak check as follows")

instruction("Set the Facility fuel to ON")
note("Facility Pumps and Valves will pressurize fuel lines.")

wait("FCS_FuelRdy = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility fuel not ON")


if SkipGV:
	result("Operator skipped Fuel on instruction {} TestPrep ".format(REPORT))

	result("Static fuel leak check not performed {} TestPrep ".format(REPORT))

else:
	lvNoleak = prompt_boo("Were there any leaks?")

	
	if lvNoleak:
		result("leaks were found {} TestPrep ".format(report))

		instruction("Repair leaks before continuing")

	else:
		result("no leaks were found {} TestPrep ".format(report))

		pass
	pass

instruction("Set the Facility fuel to Off")

wait("FCS_FuelRdy = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility fuel not OFF")

