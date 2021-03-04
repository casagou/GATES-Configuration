import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 03Motoring.tps
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION: CFM56-5B ESM 72-00-00 TESTING 002
#*  Motoring Test Procedure
#*
#*  DATE: 12/03/2020
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
AutoStrt = None
InExOK = None
MotorLeaks = None
OilReTop = None
RunDwnOK = None
StartYES = None

# Channel Registration
channel("POIL,N2,WFK,AVSVSel,BVSVSel,AVBVSel,BVBVSel,D03114,D03115,FCS_AirRdy,FCS_FuelRdy,EngSelectorNRML,EngSelectorCRNK,EngSelectorIGN,ECUpwrAbtn,ECUpwrBbtn,ManualStartSel,WetFlag")


#show_view "GATES-RTD1","View 0","Start.v"

caution("DO NOT OPERATE THE STARTER FOR MORE THAN THE STARTER")

caution("LIMIT, IT CAN CAUSE DAMAGE TO THE STARTER")

note("NOTE: Maximum operation time for the starter is 2 min")

caution("Do not motor the engine unless you have positive fuel inlet pressure.")

caution("The fuel pump and HMU are lubricated by fuel and")

caution("damage to these components can occur.")

note("NOTE: If necessary, open the cowling doors.")

instruction("Open Test Cell Start Air supply valve")

wait("FCS_AirRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not ON")

instruction("Set the Facility fuel to ON")

wait("FCS_FuelRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility fuel not ON")

instruction("DRY MOTORING PROCEDURE")

instruction("Set Throttle to GI (0 Deg)")

wait("TLA = 0", 10, 1.0, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Throttle is not at GI after 10 s.")

if skipgv:
    result("Operator skipped Throttle GI check. {} Motoring ".format(REPORT))

    pass

instruction("Set Mode Selector to NORMAL")

set_channel("EngSelectorNRML", 1)

set_channel("EngSelectorIGN", 0)

set_channel("EngSelectorCRNK", 0)


instruction("Set MASTER LEVER to OFF.")
note("Turns Engine Fuel OFF.")
set_channel("D03114", 0)
set_channel("D03115", 1)

wait("D03115 = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "MASTER LEVER not OFF")


if skipgv:
    result("Operator skipped Fuel OFF instruction {} Motoring ".format(REPORT))
    pass

instruction("Turn on ECU Ch.A Power")

set_channel("ECUpwrAbtn", 1)


instruction("Turn on ECU Ch.B Power")

set_channel("ECUpwrBbtn", 1)


instruction("Turn MANUAL START SWITCH to ON")

set_channel("ManualStartSel", 1)


instruction("Set the MODE SELECTOR to CRANK")

wait("EngSelectorCRNK = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Select CRANK Mode")


instruction("Check oil pressure rise and check engine for leaks")

wait("POIL = 5", 15, 0.5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "POIL did not reach 5 psi.")


if skipgv:
    result("Operator skipped oil pressure check {} Motoring ".format(REPORT))
    pass

wait("N2 > 300", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "No positive N2 indication in 30 s. Press SKIP to abort Motoring")

if skipgv:
	quit()
	pass

wait("N2 >= 3900", 30, 100, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "N2 did not reach 4000 rpm N2 in 30s")

if getCV("AVSVSel") > 39.7 or getCV("AVSVSel") < 37.7 or getCV("BVSVSel") > 39.7 or getCV("BVSVSel") < 37.7:
	result("FAULT: VSV are not closed! {} Motoring ".format(REPORT))

else:
	result("VSV closed {} Motoring ".format(REPORT))
	pass

if getCV("AVBVSel") <= 36 or getCV("BVBVSel") <= 36:
	result("FAULT: VBV are not open! {} Motoring ".format(REPORT))

else:
	result("VBV are open {} Motoring ".format(REPORT))
	pass

lvMotorLeaks = prompt_boo("Are there any leaks while motoring?")

if lvMotorLeaks:
	result("THERE ARE LEAKS WHILE MOTORING {} Motoring ".format(REPORT))

else:
	result("There are no leaks during engine motoring {} Motoring ".format(REPORT))
	pass

do_fullset(1, "Dry Motoring Fullset", "Motoring")


#note("WET MOTORING PROCEDURE")

instruction("WET MOTORING PROCEDURE - Fuel will be introduced in engine.", SKIP)
note("Press SKIP for Dry Motoring")

caution("When MASTER LEVER IS ON, fuel will start flowing fuel into the engine.")

note("NOTE: Set the MASTER LEVER - ON for a maximum of 15 seconds.")


if not skipgv:
	set_channel("WetFlag", 1)

instruction("Set MASTER LEVER to ON")
set_channel("D03115", 0) 
set_channel("D03114", 1)

wait("D03114 = 1", 2, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "MASTER LEVER not ON")
if skipgv:
    result("Operator skipped Fuel ON instruction {} Motoring ".format(REPORT))
    pass

delay(5)

if getCV("WFK") > 0:
	result("Working Fuel Flow = {} PPH - Positive Indication {} Motoring ".format(getCV("WFK") , REPORT))

else:
    result("Working Fuel Flow = {} PPH - FAULTY {} Motoring ".format(getCV("WFK") , REPORT))
    pass

do_fullset(1, "Wet Motoring", "WetMotoring")

delay(5)

result("Working Fuel flow {} PPH. It should be 680 PPH max. {} Motoring ".format(getFV("WFK") , REPORT))


if getCV("WFK") > 680:
    result("Working Fuel flow is over 680 PPH limit. {} Motoring ".format(REPORT))
    instruction("Immediately set the MASTER LEVER to Off")
    set_channel("D03114", 0)
    set_channel("D03115", 1)
    pass

note("NOTE: If no vapours are seen in the exhaust within 30 seconds of")

note("      MASTER LEVER movement, return MASTER LEVER to the OFF position ")

note("      and troubleshoot fuel system for possible blockage.")

	
instruction("Wet motor the engine for a maximum of 15 seconds.")

instruction("Set MASTER LEVER to OFF and dry motor the engine for 60 seconds.")

set_channel("D03114", 0)

set_channel("D03115", 1)

wait("D03115 = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel is not OFF")

if skipgv:
    result("Operator skipped Fuel Cutoff instruction {} Motoring ".format(REPORT))
    pass

if getCV("WFK") > 0:
    result("There is still fuel flow indication {} Motoring ".format(REPORT))
    pass

delay(60)

pass

instruction("Set Mode Selector to NORMAL and listen to engine rundown")

note("Both N1 and N2 rotors must come to a full stop")

set_channel("EngSelectorNRML", 1)

set_channel("EngSelectorIGN", 0)

set_channel("EngSelectorCRNK", 0)


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

#instruction("Five minutes after rotors stop, record Wet Transducer tares")


#show_view "SMES_RTD1","View 0","Pressures.0"

StartYES = prompt_boo("Do you want to Start the engine?")

if StartYES:
	AutoStrt = prompt_boo("Enter YES for AUTO Start or NO for MANUAL Start.")


if AutoStrt:
	autostart("06AutoStart")

else:
	autostart("04ManualStart")
	pass

pass

