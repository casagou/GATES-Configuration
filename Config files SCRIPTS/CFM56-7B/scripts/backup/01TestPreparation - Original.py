import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 01TestPreparation.tps
#******************************************************************************
#*  AUTHOR: John Tamplin
#*
#*  DESCRIPTION:REFERENCE:CFM56-7B ENGINE MANUAL 72-00-00 Testing 000
#*  Preparation For Test
#*  Modification History
#*
#*  DATE: 1/26/2006 8:40:48 AM
#*
#*  MODIFICATIONS:
#*  DATE         WHO  NCR    DESCRIPTION
#*  07Jul16    JOA/JSi----   V1.04 Added prompt for B27AE, fixed missing variables and synthax errors
#*  14Oct09      DP   1.11   Added set_channel for ID to solve problem of no Accel Target for Multi-Derivative configuration
#*  05Sep09      DP          V1.03 Added call to CopyStaticCheck
#*  09/06/2006   TS   -----  V1.02 if logic modified
#*  24/06/2006   JT   -----  V1.01 Initial: Taken from 263
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

# Channel Registration
channel("Eng_On,PreRTMin,PreRTHr,PreFuel,PLA,IDGdisc,FuelEnable,ID,ID_N1TOMx,BVlvUp,BVlvEnable,BVlv_Pos,B27A_Model,B27AE_Model")


# V1.11 added the following set_channel


#set_channel("ID", round(getCV("ID_N1TOMx"), 4))


# --------- Begin V1.03 Changes ------------------
#call_tps("CopyStaticCheck")

#instruction("Copy of Static Check file complete - Perform Static Check. Press NEXT when done.")

# --------- End V1.03 Changes --------------------

note("TEST PREPARATION")

instruction("Ensure Facility Air and Fuel spupply are OFF")
wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")
wait("FCS_FuelRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Fuel not OFF")

#tempvar1gv = 0
lvtempvar1 = 0
if round(getCV("Eng_On"), 4) == True:
	quit()

	pass

instruction("Zero all Pressure Brick Transducers", SKIP)

if skipgv == False:
	pbs_zero()
	pass
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


lvIDGinst = prompt_boo("Is the IDG installed?")

#* V1.02 if logic modified
if lvIDGinst:
	instruction("Check IDG disconnect")

	set_channel("IDGDisc", 1)

	lvIDGdisc = prompt_boo("Was IDG disconnect satisfactory?")

#* V1.02 if logic modified
	if lvIDGdisc:
		result("IDG disconnect operation OK {} IDGdisc ".format(REPORT))

	else:
		result("IDG disconnect operation NOT OK {} IDGdisc ".format(REPORT))

		pass
	set_channel("IDGDisc", 0)

	pass


instruction("Do an Air System leak check")

instruction("Turn Test Cell start air ON")

wait("FCS_AirRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not ON")

note("Check for any air leaks")

instruction("Turn Test Cell start air OFF")

wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")

lvStartleak = prompt_boo("Was air leak check satisfactory?")

if lvStartleak:
	result("Start air leak check OK {} Startleak ".format(REPORT))

else:
	result("Start air leak check NOT OK {} Startleak ".format(REPORT))

	pass

instruction("Do an oil quantity check")

lvOilLevel = prompt_boo("Is oil level satisfactory?")

#* V1.02 if logic modified
if lvOilLevel:
	result("Oil level OK {} OilLevel ".format(REPORT))

else:
	result("Oil level NOT OK.  Refill oil tank {} OilLevel ".format(REPORT))

	pass

