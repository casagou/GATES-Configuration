import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* <04ManualStart.tps>
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:
#*  10.A CFM56-5B Manual Starting Procedure
#*
#*  DATE: 12/04/2020
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*
#******************************************************************************

# Channel Registration
channel("tToLite,tToLiteMax,WFK,EndStartL,tToIdle,EndLite,N2PCT,POIL,FuelEnable")

channel("ECUpwrAbtn,ECUpwrBbtn,EngSelectorNRML,EngSelectorIGN,EngSelectorCRNK,D03114,D03115,FCS_AirRdy,FCS_FuelRdy,ManualStartSel")


In_ExhOK = None
lvFuelPress = None

instruction("Ensure Facility fuel and air are OFF")

wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")

wait("FCS_FuelRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Fuel not OFF")

if skipgv:
	result("Operator skipped Facility OFF instruction {} ManStart ".format(REPORT))

	pass
    

instruction("Before performing start check inlet and exhaust")

In_ExhOK = prompt_boo("Was inlet and exhaust check satisfactory?")


if In_ExhOK:
	result("Inlet and exhaust checked OK. {} InExCheck ".format(REPORT))

else:
	result("A problem was found in the inlet or exhaust. {} InExCheck ".format(REPORT))
	pass

    

instruction("Turn on ECU 28V power Ch. A & B")
set_channel("ECUpwrAbtn", 1)
set_channel("ECUpwrBbtn", 1)


instruction("Set MASTER LEVER to OFF")
set_channel("D03114",0)
set_channel("D03115",1)

instruction("Turn ON Facility Air & Fuel")
    
wait("FCS_AirRdy = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not ON")
wait("FCS_FuelRdy = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Fuel not ON")


if skipgv:
	result("Operator skipped Facility ON instruction {} ManStart ".format(REPORT))
	pass

instruction("Set Throttle to IDLE (0 Deg)")

wait("TLA = 0", 10, 1.0, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Throttle is not at GI after 10 s.")


if skipgv:
	result("Operator skipped Throttle IDLE check. {} ManStart ".format(REPORT))

	pass

instruction("Set Mode Selector to NORMAL")

set_channel("EngSelectorNRML", 1)
set_channel("EngSelectorIGN", 0)
set_channel("EngSelectorCRNK", 0)



note("NOTE: Make sure the starter air supply is sufficient")

note("      (25 psig recommended)")


caution("Obey the oil pressure limits. If the engine operates at low")

caution("oil pressures, bearing damage can occur.")


note("NOTE: If the engine was operated during the previous 2 hours, ")

note("      dry-motor the engine for approximately 90 seconds.")

note("NOTE: In the event of an aborted start, the entire starting")

note("       sequence may have to be repeated from the beginning")


caution("Do not operate the engine above IDLE with the cowling doors OPEN.")


note("NOTE: The IDLE leak check will be done with the cowling doors OPEN")


caution("Carefully monitor the start cycle when you use lower starter")

caution("inlet air-pressure than recommended.  Low air-pressure at the")

caution("starter inlet can cause higher peak EGT and unusual time to idle.")


caution("Do not operate the engine if the fuel inlet pressure is not")

caution("positive")


lvFuelPress = prompt_boo("Is the fuel pressure sufficient for an engine start?")


if lvFuelPress:
	result("Fuel pressure is adequate for an engine start. {} ManStart ".format(REPORT))

else:
	result("Fuel pressure is not adequate for an engine start. {} ManStart ".format(REPORT))

	pass

instruction("Set Left and Right Ignitors to ON")

set_channel("IgnPwrL", 1)
set_channel("IgnPwrR", 1)
    
    
start_log("Start")


instruction("Turn Manual Start switch to ON")

set_channel("ManualStartSel", 1)


instruction("Set Mode Selector to IGNITION")

set_channel("EngSelectorNRML", 0)
set_channel("EngSelectorIGN", 1)
set_channel("EngSelectorCRNK", 0)


instruction("Check for positive, increasing oil pressure")

#wait "APOilLoc >= 5", 5, 0.5,,,,,"POIL did not reach 5 psi. Press SKIP to abort"
wait("POIL >= 5", 5, 0.5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, "POIL did not reach 5 psi. Press SKIP to abort")


if skipgv:
	auto_start("05AbortStart")

	pass

wait("N2PCT > 20", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach 20 % N2 or Max motoring speed in 30 s. Press SKIP to abort.")


instruction("Set MASTER LEVER to ON")

wait("D03114 = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "MASTER LEVER not ON")


if skipgv:
	result("Operator skipped Fuel ON instruction {} ManStart ".format(REPORT))

	pass

wait("EndLite = 1", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "No Lite")


if getCV("tToLite") > getCV("tToLiteMax"):
	result("Time to Lite is > {} Start Aborted {} ManStart ".format(getCV("tToLiteMax") , REPORT), "RED")

	auto_start("05AbortStart")

	pass

result("Fuel flow during start is {} lb per hour. {} ManStart ".format(getCV("WFK") , REPORT))


#wait("N2S >= 7230", 30, 50, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach 7230 rpm N2 in 30 s. Press SKIP to abort.")


if skipgv:
	auto_start("05AbortStart")

	pass

wait("EndStartL = 1", 120, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "End Start indication not received in 120 s")


if getCV("tToIdle") >= 120:
	result("Time from Fuel ON to Idle exceeded 120 s {} ManStart ".format(REPORT), "RED")

	auto_start("05AbortStart")

	pass

#*  engine at idle

instruction("Set Mode Selector to NORMAL")

set_channel("EngSelectorNRML", 1)
set_channel("EngSelectorIGN", 0)
set_channel("EngSelectorCRNK", 0)
    



do_fullset(1, "Ground Idle following Start", "ManStart")


stop_log("Start")

instruction("Close Facility Air supply valve")

wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")
