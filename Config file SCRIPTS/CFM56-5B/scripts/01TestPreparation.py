import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 01TestPreparation.tps
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION: CFM56-5B ESM 72-00-00 TESTING 000
#*  Preparation For Test
#*  Modification History
#*
#*  DATE: 12/03/2020
#*
#*  MODIFICATIONS:
#*  DATE         WHO  NCR    DESCRIPTION
#*
#*
#******************************************************************************NK

# ***** LOCAL VARIABLE DECLARATIONS *****
lvIDGdisc = None
lvIDGinst = None
lvOilLevel = None
lvPreFuel = None
lvPreHr = None
lvNo1Fire = None
lvNo2Fire = None
lvNoleak = None
lvPreMin = None
lvStartleak = None
lvtempvar1 = None
booPreRun = None
lvIgntest = None

# Channel Registration
channel("Eng_On,PreRTMin,PreRTHr,PreFuel,D03114,D03115,EngSelectorNRML,EngSelectorIGN,EngSelectorCRNK,FCS_AirRdy,FCS_FuelRdy,ECUpwrAbtn,ECUpwrBbtn,IgnPwrL_ref,IgnPwrR_ref,ManualStartSel")


lvtempvar1 = 0

if getCV("Eng_On") == 1:
	quit()

	pass

note("TEST PREPARATION")

instruction("Ensure Facility Air and Fuel Supply are OFF")
wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")
wait("FCS_FuelRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Fuel not OFF")


booPreRun = prompt_boo("Is this a continuation of a previous test?")


if booPreRun:
	lvPreHr = prompt_num("Enter previous run time: Hours", -1, 101, 0)

	set_channel("PreRTHr", lvPreHr)

	lvPreMin = prompt_num("Enter previous run time: Minutes", -1, 61, 0)

	set_channel("PreRTMin", lvPreMin)

	lvPreFuel = prompt_num("Enter the amount of fuel used for previous run in litres", -1, 100000, 0)

	set_channel("PreFuel", lvPreFuel)

	pass



instruction("Perform an Air System leak check")

instruction("Turn Test Cell start air ON")

wait("FCS_AirRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not ON")

note("Check for any air leaks")

instruction("Turn Test Cell start air OFF")

wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")

lvStartleak = prompt_boo("Was air leak check satisfactory?")


if lvStartleak:
	result("Starter air leak check OK {} TestPrep ".format(REPORT))

else:
	result("Starter air leak check NOT OK {} TestPrep ".format(REPORT))

	pass

instruction("Perform oil quantity check")

lvOilLevel = prompt_boo("Is oil level satisfactory?")


if lvOilLevel:
	result("Oil level OK {} TestPrep ".format(REPORT))

else:
	result("Oil level NOT OK.  Refill oil tank {} TestPrep ".format(REPORT))

	pass

#*************************************************************************

lvIgntest = prompt_boo("Do you want to do an Igniter check?")


if lvIgntest:
	instruction("Do an ignitor check as follows")

	instruction("Ensure MASTER LEVER is set to OFF.")
	note("Engine Fuel is OFF.")
	set_channel("D03114",0)
	set_channel("D03115",1)
    
	wait("D03115 = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "MASTER LEVER not OFF")

    #if SkipGV:
        #result("Operator skipped Fuel OFF instruction {} TestPrep ".format(REPORT))

		#pass

	instruction("Set Throttle to IDLE (0 Deg)")
    #need auto throttle input here

	wait("TLA = 0", 10, 1.0, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Throttle is not at GI after 10 s.")

	#if SkipGV:
		#result("Operator skipped Throttle GI check. {} TestPrep ".format(REPORT))

		#pass
	
	instruction("Set MODE SELECTOR to NORMAL")

	set_channel("EngSelectorNRML", 1)
	set_channel("EngSelectorIGN", 0)
	set_channel("EngSelectorCRNK", 0)
    
	instruction("Turn on ECU 28V power Ch. A & B")
    
	set_channel("ECUpwrAbtn", 1)
	set_channel("ECUpwrBbtn", 1)
    
	
	instruction("Close Test Cell Air supply valve")

	wait("FCAirOn = 0", 10, 1.0, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Air supply is not disabled.")

	
	#if SkipGV:
		#result("Operator skipped Air Supply Disabled {} TestPrep ".format(REPORT))

		#pass
	
	instruction("Turn ON 115VAC ignition No.1 power to ECU Ch.A")
    
	set_channel("IgnPwrL_ref", 1)
    
	instruction("Turn OFF 115VAC ignition No.2 power to ECU Ch.B")
    
	set_channel("IgnPwrR_ref", 0)

	
	instruction("Turn MANUAL START SWITCH to ON")

	set_channel("ManualStartSel", 1)

	
	instruction("Set MODE SELECTOR to IGNITION")
    
	note("Igniter will continuously fire until MANUAL START SWITCH is turned OFF")
    
	set_channel("EngSelectorNRML", 0)
	set_channel("EngSelectorIGN", 1)
	set_channel("EngSelectorCRNK", 0)

	
	instruction("Make sure the No.1 igniter is firing")

	lvNo1Fire = prompt_boo("Was igniter No.1 firing?")

	
	if lvNo1Fire:
		result("Igniter No.1 is firing properly {} TestPrep ".format(REPORT))
       

	else:
		result("Igniter No.1 is not firing properly {} TestPrep ".format(REPORT))

		pass
	
	instruction("Turn MANUAL START SWITCH to OFF")

	set_channel("ManualStartSel", 0)

	
	instruction("Set Mode Selector to NORMAL")

	set_channel("EngSelectorNRML", 1)
	set_channel("EngSelectorIGN", 0)
	set_channel("EngSelectorCRNK", 0)

	
	instruction("Turn ON 115VAC ignition No.2 power to ECU Ch.B")
    
	set_channel("IgnPwrR_ref", 1)
    
	instruction("Turn OFF 115VAC ignition No.1 power to ECU Ch.A")
    
	set_channel("IgnPwrL_ref", 0)
	
	instruction("Turn MANUAL START SWITCH to ON")

	set_channel("ManualStartSel", 1)

	
	instruction("Set MODE SELECTOR to IGNITION")
	note("Igniter will continuously fire until MANUAL START SWITCH is turned OFF")

	set_channel("EngSelectorNRML", 0)
	set_channel("EngSelectorIGN", 1)
	set_channel("EngSelectorCRNK", 0)

	
	instruction("Make sure the No.2 igniter is firing")

	lvNo2Fire = prompt_boo("Was igniter number 2 firing?")

	
	if lvNo2Fire:
		result("Igniter No.2 is firing properly {} TestPrep ".format(REPORT))

	else:
		result("Igniter No.2 is not firing properly {} TestPrep ".format(REPORT))

		pass
	
	instruction("Turn MANUAL START SWITCH to OFF")

	set_channel("ManualStartSel", 0)

	
	instruction("Set MODE SELECTOR to NORMAL")

	set_channel("EngSelectorNRML", 1)

	set_channel("EngSelectorIGN", 0)

	set_channel("EngSelectorCRNK", 0)

	
	instruction("Turn ON 115VAC ignition No.1 power to ECU Ch.A")

	set_channel("IgnPwrL", 1)

else:
	result("Igniter test was not performed {} TestPrep ".format(REPORT))

	pass

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
		result("leaks were found {} TestPrep ".format(REPORT))

		instruction("Repair leaks before continuing")

	else:
		result("no leaks were found {} TestPrep ".format(REPORT))

		pass
	pass

instruction("Set the Facility fuel to Off")

wait("FCS_FuelRdy = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility fuel not OFF")


