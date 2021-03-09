import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 03Motoring.py
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:REFERANCE CFM56-7B ENGINE MANUAL 72-00-00 TESTING 002
#*  Motoring Check Procedure
#*
#*  DATE: 01/04/2021 
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*
#*
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
AutoStrt = None
InExOK = None
MotorLeaks = None
OilReTop = None
RunDwnOK = None
StartYES = None
RTD1 = None
RTD1 = "SMESRTD1"


# Channel Registration
channel("FCS_AirRdy,FCS_FuelRdy,ECUpwrA,ECUpwrB,IgnPwrL,IgnPwrR,EngStrtLvr,StrtSwitch,FIFB,APOilLoc,N2,AVSVSel,BVSVSel,AVBVSel,BVBVSel,TLA,WFK")



caution("DO NOT OPERATE THE STARTER FOR MORE THAN THE STARTER")

caution("LIMIT, IT CAN CAUSE DAMAGE TO THE STARTER")


note("NOTE: Allowable limit - 2 consective extended motoring times of 15 min each for the starter is permited")
note("A wait time of 2 minutes between attempts is required.")


caution("Do not motor the engine unless you have positive fuel inlet")

caution("pressure.  The fuel pump and HMU are lubricated by fuel and")

caution("damage to these components can occur.")


instruction("Dry Motor the engine as follows:")

note("If necessary, open the cowling doors")


#caution("Do no try to control the fuel flow with the Fuel On switch.")

#caution("High fuel flows will put too much fuel into the engine.")


instruction("Open Test Cell Start Air supply valve")

wait("FCS_AirRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not ON")

instruction("Set the Facility fuel to ON")

wait("FCS_FuelRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility fuel not ON")


if getCV("ECUpwrA") == 0 or getCV("ECUpwrB") == 0:
	   
	   instruction("Power ON ECU Ch. A & Ch. B")
	   
	   set_channel("ECUpwrA",1)
	   set_channel("ECUpwrB",1)
	   
	   pass



instruction("Manually Set Throttle to IDLE position (0 Deg TLA)")

set_channel("FIFB", 0)

wait("TLA = 0", 10, 1.0, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Throttle is not at GI after 10 s.")


if SkipGV:
	result("Operator skipped Throttle GI check. {} Motoring ".format(REPORT))

	pass



instruction("Set ENGINE START LEVER to CUTOFF position")

wait("EngStrtLvr = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "START LEVER not in CUTOFF position")



instruction("Set ENGINE START SWITCH to GRD")


wait("StrtSwitch = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "GRD not selected by START SWITCH")


instruction("Check oil pressure rise and check engine for leaks")

wait("APOilLoc = 5", 15, 0.5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "POIL did not reach 5 psi.")


if SkipGV:
	result("Operator skipped oil pressure check {} Motoring ".format(REPORT))

	pass

wait("N2 > 300", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "No positive N2 indication in 30 s. Press SKIP to abort Motoring")


if SkipGV:

	instruction("Set ENGINE START SWITCH to OFF.Do troubleshooting")

	pass


wait("N2 > 3900", 30, 100, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "N2 did not reach 3900 rpm N2 in 30s")


if getCV("AVSVSel") < 37.7 or getCV("BVSVSel") < 37.7:
	result("FAULT: VSV are not closed! {} Motoring ".format(REPORT))

else:
	result("VSV closed {} Motoring ".format(REPORT))

	pass


if getCV("AVBVSel") < 37 or getCV("BVBVSel") < 37:
	
	result("FAULT: VBV are not open! {} Motoring ".format(REPORT))

else:
	result("VBV open {} Motoring ".format(REPORT))

	pass

MotorLeaks = prompt_boo("Are there any leaks while motoring?")


if MotorLeaks:
	result("THERE ARE LEAKS WHILE MOTORING {} Motoring ".format(REPORT))

else:
	result("There are no leaks during engine motoring {} Motoring ".format(REPORT))

	pass

instruction("Record full_set")

do_fullset(1, "Dry Motoring Fullset", "Motoring")


instruction("WET MOTORING PROCEDURE - Fuel will be introduced in engine.", SKIP)
note("Press SKIP for Dry Motoring")

caution("When ENGINE START LEVER is at IDLE, fuel will start flowing fuel into the engine.")

note("NOTE: Set ENGINE START LEVER at IDLE for a maximum of 15 seconds.")


if not SkipGV:
	set_channel("WetFlag", 1)
	instruction("Turn OFF ignition power")
	set_channel("IgnPwrL", 0)
	set_channel("IgnPwrR", 0)
	instruction("Set ENGINE START LEVER to IDLE")
	wait("EngStrtLvr = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel not ON")

	if SkipGV:
		result("Operator skipped Fuel ON instruction {} Motoring ".format(REPORT))
		pass
	
	delay(5)

	if getCV("WFK")> 0:
		result("Working Fuel Flow = {} PPH - Positive Indication {} Motoring ".format(getCV("WFK"), REPORT))

	else:
		result("Working Fuel Flow = {} PPH - FAULTY {} Motoring ".format(getCV("WFK"), REPORT))

		pass
	
	do_fullset(1, "Wet Motoring", "WetMotoring")

	delay(5)

	result("Working Fuel flow {} PPH. It should be 680 PPH max. {} Motoring ".format(getFV("WFK"), REPORT))

	
	if getCV("WFK") > 680:
		result("Working Fuel flow is over 680 PPH limit. {} Motoring ".format(REPORT))

		instruction("Immediately set the fuel to Off")

		pass
	
	note("NOTE: If no vapours are seen in the exhaust within 30 seconds of")

	note("      selecting the IDLE, return ENGINE START LEVER to CUTOFF position ")

	note("      and troubleshoot fuel system for possible blockage.")

	
	instruction("Wet motor the engine for a maximum of 15 seconds.")

	
	instruction("Set ENGINE START LEVER to CUTOFF and dry motor the engine for 60 seconds.")
	
	set_channel("EngStrtLvr", 0)

	wait("EngStrtLvr = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel is not OFF")

	if SkipGV:
		result("Operator skipped Fuel Cutoff instruction {} Motoring ".format(REPORT))

		pass
	
	if getCV("WFK") > 0:
		result("There is still fuel flow indication {} Motoring ".format(REPORT))

		pass
	
	delay(60)

	
	pass

instruction("Set ENGINE START SWITCH to OFF and listen to engine rundown")

note("until both N1 and N2 rotors have come to a full stop")


wait("StrtSwitch = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Set ENGINE START SWITCH to OFF.")


note("NOTE: Any unusual noises during rundown should be")

note("      reported to Engineering")


RunDwnOK = prompt_boo("Was rundown satisfactory?")

if RunDwnOK:
	result("Rundown was satisfactory {} Motoring ".format(REPORT))

else:
	result("There were problems during rundown {} Motoring ".format(REPORT))

	pass

instruction("Service engine as required")


caution("DO NOT OVERFILL IDG AND THE OIL TANK")


OilReTop = prompt_boo("Were oil levels checked and retopped as required?")

if OilReTop:
	result("Oil levels are checked and retopped {} Motoring ".format(REPORT))

else:
	result("Oil levels are not checked and retopped {} Motoring ".format(REPORT))

	pass

instruction("Check inlet and exhaust")

InExOK = prompt_boo("Were inlet and exhaust found satisfactory when checked?")

if InExOK:
	result("Inlet and exhaust checked OK. {} Motoring ".format(REPORT))

else:
	result("A problem was found in the inlet or exhaust. {} Motoring ".format(REPORT))

	pass

instruction("Five minutes after rotors stop, record Wet Transducer tares")


#*  V1.05 added the following show_view
#* show_view "SMES-RTD1", "View1" , "Pressures.0", 0,0,10,10

StartYES = prompt_boo("Do you want to Start the engine?")

if StartYES:
	
	autostart("04Start.py")

else:
	quit()

	pass
pass