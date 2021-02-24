import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 17Shutdown.py
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:
#*  Identifier : CFM56-7B Manual 72-00-00 Testing 000, page 1334
#*  12. Shutdown procedure
#*
#*  DATE: 1/6/2021
#*
#*  MODIFICATIONS:
#*    DATE         WHO  REV    DESCRIPTION
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

channel("EngStrtLvr,StrtSwitch,Eng_On,GIFlag,N1RDWN,N2RDWN,NARDWN,NBRDWN,NAStop,NBStop")



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


instruction("Ensure ENGINE START SWITCH is set to OFF")

wait("StrtSwitch = 0", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "ENGINE START SWITCH not set to OFF in 10 seconds")


instruction("Set ENGINE START LEVER to CUTOFF")

wait("EngStrtLvr = 0", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "ENGINE START LEVER not set to CUTOFF in 10 seconds")

# V1.03 skipgv modified
if skipgv:
	result("Operator skipped Cutoff instruction. {} Shutdown ".format(REPORT))

	result("Shutdown will be aborted {} Shutdown ".format(REPORT))

	quit()
    
    pass



result("Engine shut down {} Shutdown ".format(REPORT))

	
instruction("Listen to rundown, report any unusual noises")

	
instruction("Observe engine for evidence of internal fire or")

note("tailpipe fire. If they occur, dry motor the engine.")

TailFire =  prompt_boo("Is there any evidence of engine or tail fire?") 

if TailFire:
    instruction("Turn ON Facility Air supply")
    
    wait("FCS_AirRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not ON")

	instruction("Set ENGINE START SWITCH to GRD")
    note("And DRY MOTOR engine until fire stops.")
    
    set_channel("StrtSwitch", 1)
    
    pass
    
    

RundownOK = prompt_boo("Do you want to do a rundown check?")

if RundownOK:
	stop1 = prompt_boo("Press YES button when the first rotor has fully stopped")

	set_channel("NAStop", 1)

	stop1 = prompt_boo("Press YES button when the second rotor has fully stopped")

	set_channel("NBStop", 1)

	Rotnbr = prompt_boo("Did N2 Rotor stop first?")


	if Rotnbr == False:
		set_channel("N1RDWN",getCV("NARDWN"))

		set_channel("N2RDWN",getCV("NBRDWN"))

	else:
		set_channel("N1RDWN",getCV("NBRDWN"))

		set_channel("N2RDWN",getCV("NARDWN"))
        pass
		
    delay(2)

    result("Rundown times were: N1 = {} secs  N2 = {} secs. {} Shutdown ".format(getCV("N1RDWN"),getCV("N2RDWN"), REPORT))

    pass

Whyshutdown = prompt_str("Enter reason for shutdown")

Drymotor = prompt_boo("Do you want to do a dry motoring at this time?")


if Drymotor:
	
	note("DRY MOTORING for 2 minutes")

	
	instruction("Ensure Test Facility Air & Fuel supply is available")
           
	wait("FCS_AirRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not ON")
    wait("FCS_FuelRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Fuel not ON")
	

	instruction("Set ENGINE START SWITCH to GRD and DRY MOTOR engine for 2 minutes")
    
    set_channel("StrtSwitch", 1)
   
    
    
    delay(120)

	
	instruction("Set ENGINE START SWITCH back to NORMAL")
    note("To close starter valve")
    
    set_channel("StrtSwitch",0)
	

	
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