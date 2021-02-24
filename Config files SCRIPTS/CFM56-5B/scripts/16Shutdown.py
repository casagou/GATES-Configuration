import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 16Shutdown.tps
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:
#*  Identifier : CFM56-5B Manual 72-00-00 Testing 000
#*  12. Shutdown procedure
#*
#*  DATE: 12/09/2020 
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
Rotnbr = None
RundownOK = None
stop1 = None
Whyshutdown = None
Drymotor = None
TailFire = None

# Channel Registration
channel("Eng_On,GIFlag,N1RDWN,N2RDWN,NARDWN,NBRDWN,TransReset,NAStop,NBStop,D03114,D03115")

channel("EngSelectorNRML,EngSelectorIGN,EngSelectorCRNK,ManualStartSel,FCS_AirRdy,FCS_FuelRdy,N2S")

if getCV("Eng_On") == 0:
	quit()

	pass

instruction("Run the engine 5 minutes at Ground Idle, or press SKIP" , SKIP)


if not skipgv:
	wait("GIFlag = 1", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "Engine not at Min IDLE")

	delay(300)

	pass

set_channel("NAStop", 0)

set_channel("NBStop", 0)

set_channel("TransReset", 1)

delay(2)

set_channel("TransReset", 0)


note("SHUT DOWN PROCEDURE")


caution("MAKE SURE THE EGT CONSTANTLY DECREASES TO PREVENT")

caution("DAMAGE TO THE ENGINE")


note("NOTE: If EGT does not decrease or if there is a tailpipe")

note("      fire, motor the engine until the fire stops.")

if getCV("EngSelectorNRML") != 1

    instruction("Set MODE SELECTOR to NORMAL")

    set_channel("EngSelectorNRML", 1)
    set_channel("EngSelectorIGN", 0)
    set_channel("EngSelectorCRNK", 0)
    pass

instruction("Set MASTER LEVER to OFF")

wait("D03115 = 1", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "MASTER LEVER was not set to OFF in 10 seconds")


if skipgv:
	result("Operator skipped Cutoff instruction. {} Shutdown ".format(REPORT))

	result("Shutdown will be aborted {} Shutdown ".format(REPORT))

	quit()

else:
	result("Engine shut down {} Shutdown ".format(REPORT))

	pass


instruction("Check N2, EGT and fuel flow for immediate")

note("indication of engine shutdown.")


instruction("Listen to rundown, report any unusual noises")


instruction("Observe engine for evidence of internal fire or")

note("tailpipe fire. If they occur, dry motor the engine.")

TailFire =  prompt_boo("Is there any evidence of engine or tail fire?") 

if TailFire:
    instruction("Turn ON Facility Air supply")
    
    wait("FCS_AirRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not ON")

    if getCV("ManualStartSel") = 0:
        instruction("Turn Manual Start switch to ON")

        set_channel("ManualStartSel", 1)
        pass
    
    instruction("Set MODE SELECTOR to CRANK")
    note("And DRY MOTOR engine until fire stops.")
    
    set_channel("EngSelectorNRML", 0)
    set_channel("EngSelectorIGN", 0)
    set_channel("EngSelectorCRNK", 1)
    
    pass



RundownOK = prompt_boo("Do you want to do a Rundown check?")

if RundownOK:
	stop1 = prompt_boo("Press YES button when the first rotor has fully stopped")

	set_channel("NAStop", 1)

	stop1 = prompt_boo("Press YES button when the second rotor has fully stopped")

	set_channel("NBStop", 1)

	Rotnbr = prompt_boo("Did N2 Rotor stop first?")

	
	if not Rotnbr:
		set_channel("N1RDWN", getCV("NARDWN"))

		set_channel("N2RDWN", getCV("NBRDWN"))

	else:
		set_channel("N1RDWN", getCV("NBRDWN"))

		set_channel("N2RDWN", getCV("NARDWN"))

		pass
	
    delay(2)

    result("Rundown times were: N1 = {} secs  N2 = {} secs. {} Shutdown ".format(getCV("N1RDWN") , getCV("N2RDWN") , REPORT))

    pass

Whyshutdown = prompt_str("Enter reason for shutdown")


Drymotor = prompt_boo("Do you want to do a dry motoring at this time?")


if Drymotor:
	
	note("DRY MOTORING for 2 minutes")

	
	instruction("Ensure Test Facility Air & Fuel supply is available")
           
	wait("FCS_AirRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not ON")
    wait("FCS_FuelRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Fuel not ON")
	
	#instruction("Set Throttle to Min IDLE (0 Deg)")

	#wait("TLA = 0", 10, 1.0, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Throttle is not at Min IDLE after 10 seconds.")

	
	#if skipgv:
		#result("Operator skipped Throttle Min IDLE check. {} Motoring ".format(REPORT))

		#pass
	instruction("Turn Manual Start switch to ON")

	set_channel("ManualStartSel", 1)
    
	instruction("Set MODE SELECTOR to CRANK and DRY MOTOR engine for 2 minutes")
    
    set_channel("EngSelectorNRML", 0)
    set_channel("EngSelectorIGN", 0)
    set_channel("EngSelectorCRNK", 1)
    
    
    delay(120)

	
	instruction("Set MODE SELECTOR back to NORMAL")
    note("To close starter valve")
    
    set_channel("EngSelectorNRML", 1)
    set_channel("EngSelectorIGN", 0)
    set_channel("EngSelectorCRNK", 0)
	

	
	instruction("Turn OFF Test Facility Air & Fuel supply", SKIP)
    
    if skipgv:
        result("Facility Air & Fuel left ON.")
        
        pass
        
	wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")
    wait("FCS_FuelRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Fuel not OFF")

else
        result("Operator skipped DRY MOTOR instruction. {} Shutdown ".format(REPORT))
    pass
    
pass