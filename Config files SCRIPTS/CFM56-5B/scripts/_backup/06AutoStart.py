import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 06AutoStart.tps
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:
#*  IDENTIFIER: 72-00-00, TESTING-000,
#*  CFM56-5B Auto Starting Procedure
#*
#*  DATE: 12/04/2020
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*
#******************************************************************************

# Channel Registration
channel("ECUpwrAbtn,ECUpwrBbtn,EndLite,EndStartL,FCS_AirRdy,FCS_FuelRdy,tToIdle,tToLite,tToLiteMax,WFK,N2PCT")

channel("ManualStartSel,IgnPwrL,IgnPwrR,EngSelectorIGN,EngSelectorNRML,EngSelectorCRNK,D03114,D03115")

In_ExhOK = None

instruction("Ensure Facility fuel and air are OFF")
    wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")
    wait("FCS_FuelRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Fuel not OFF")

if skipgv:
	result("Operator skipped Facility OFF instruction {} AutoStart ".format(REPORT))

	pass

instruction("Check inlet and exhaust")

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


if skipgv:
	result("Operator skipped Fuel OFF instruction {} AutoStart ".format(REPORT))

	pass

instruction("Set Throttle to IDLE (0 Deg)")

wait("TLA = 0", 10, 1.0, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Throttle is not at GI after 10 s.")


if skipgv:
	result("Operator skipped Throttle IDLE check. {} AutoStart ".format(REPORT))

	pass


instruction("Turn ON Facility Air & Fuel")
    
    wait("FCS_AirRdy = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not ON")
    wait("FCS_FuelRdy = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Fuel not ON")


if skipgv:
	result("Operator skipped Facility ON instruction {} ManStart ".format(REPORT))

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


caution("Do not operate the engine above the IDLE with the cowling doors OPEN.")


note("NOTE: The IDLE leak check will be done with the cowling doors OPEN")


caution("Carefully monitor the start cycle when you use lower starter")

caution("inlet air-pressure than recommended.  Low air-pressure at the")

caution("starter inlet can cause higher peak EGT and unusual time to idle.")


caution("Do not operate the engine if the fuel inlet pressure is not")

caution("positive")


instruction("Turn Start Mode to Automatic")

    set_channel("ManualStartSel", 0)


instruction("Set Mode Selector to IGNITION")

    set_channel("EngSelectorNRML", 0)
    set_channel("EngSelectorIGN", 1)
    set_channel("EngSelectorCRNK", 0)


instruction("Set Left and Right Ignitors to ON")

    set_channel("IgnPwrL", 1)
    set_channel("IgnPwrR", 1)


start_log("Start")


instruction("Set MASTER LEVER to ON")

wait("D03114 = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "MASTER LEVER not ON")


if skipgv:
	result("Operator skipped Fuel ON instruction {} AutoStart ".format(REPORT))

	pass

wait("N2PCT > 20", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach 20 % N2 or Max motoring speed in 30 s. Press SKIP to abort.")


wait("EndLite = 1", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "No Lite")


if getCV("tToLite") > getCV("tToLiteMax"):
	result("Time to Lite is > {} Start Aborted {} AutoStart ".format(getCV("tToLiteMax") , REPORT), "RED")

	pass

result("Fuel flow during start is {} lb per hour. {} AutoStart ".format(getCV("WFK") , REPORT))


wait("EndStartL = 1", 120, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "End Start indication not received in 120 s")


if getCV("tToIdle") >= 120:
	result("Time from Fuel ON to Idle exceeded 120 s {} AutoStart ".format(REPORT), "RED")

	auto_start("05AbortStart")

	pass

#*  engine at idle

instruction("Set Mode Selector to NORMAL")

    set_channel("EngSelectorNRML", 1)
    set_channel("EngSelectorIGN", 0)
    set_channel("EngSelectorCRNK", 0)




do_fullset(1, "Ground Idle following Start", "AutoStart")

stop_log("Start")


instruction("Close Facility Air supply valve")
    wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")

delay(300)


