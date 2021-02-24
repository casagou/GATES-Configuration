import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 09FADECCheck.tps
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:REFERANCE CFM56-7B ENGINE MANUAL 72-00-00 TESTING 002
#*  FADEC System Check
#*
#*  DATE: 12/16/2020
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*    
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
ACHInCont = None
alvl1_270 = None
AutoStrt = None
blvl1_270 = None
CHConCheck = None
IDGEng = None
lvAinControl = None


channel("A27013,B27013,Eng_On,GIFlag,ECUpwrA,ECUpwrB,A27524,B27524,EngStable30s,EngStable")


instruction("If the engine is running, please shutdown engine.")

if getCV("Eng_On") == 1:

	call_tps("16Shutdown")
    
    pass

if skipgv:

	result("Operator skipped Engine Shutdown instruction {} AutoStart ".format(REPORT))

	pass

instruction("After engine shutdown, remove power to both channels of the ECU and wait at least 30 seconds")
    
    wait("ECUpwrA = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "ECU Ch.A not Powered OFF")
    wait("ECUpwrB = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "ECU Ch.B not Powered OFF")
    delay(30)
    
instruction("Power back on ECU.")
set_channel("ECUpwrA", 1)
set_channel("ECUpwrB", 1)
 
note("NOTE: One channel will have primary control of the ECU. The other channel will")
note("be the secondary control channel and not in control. If both channels are servicable, at")
note("each engine shutdown the primary control channel will become the secondary control")
note("channel and the secondary will become the primary control channel.")


 
lvAinControl = 0



if getCV("A27013") == 1:
        
        lvAinControl = 1
    
        result("ECU channel A is Primary channel in control {} FADECCheck ".format(REPORT))
        result("ECU channel B is Secondary channel in control")        
        
    else
        if getCV("B27013") == 1:
        
        lvAinControl = 0
        
        result("ECU channel B is Primary channel in control {} FADECCheck ".format(REPORT))
        result("ECU channel A is Secondary channel in control")
        pass    
    pass
    
    
    
instruction("Ensure that there are no FADEC faults indicated on the ARINC output.")
note("ARINC Label 275 bit 24 = 0, for both channels")

wait("A27524 = 0", 2, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "ECU Ch.A is indicating a fault")
wait("B27524 = 0", 2, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "ECU Ch.B is indicating a fault")


instruction("Do an engine start precedure and stabilize at Min. Idle.")

call_tps("06AutoStart")

if getCV("Eng_On") == 1
    delay(120)
    pass
    

			
instruction("Slowly increase engine speed (60 sec) to 11,100RPM N2 and")
note("stabilize for 30 seconds.")

wait("N2 = 11100", 35, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N2 speed is not at 11,100 RPM")

#TLA command movement here

wait("EngStable30s = 1", 95, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine has not stabilized for 30 seconds")
    
    if getCV("EngStable30s") == 1:
        result("Engine has stabilized for 30 seconds.")
        pass
    
    if skipgv:
		result("Operator skipped Engine stabilization time {} FADECCheck ".format(REPORT))
        pass



instruction("Decrease engine speed (30 sec) to MIN IDLE and")
note("stabilize for 5 minutes.")

wait("GIFlag = 1", 35, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not at MIN IDLE speed")

#TLA command movement here

if getCV("EngStable") == 1 and getCV("tAtGI") == 300:
    
    result("Engine has been stabilized for 5 minutes.")
    pass
    

instruction("Ensure there are no FADEC faults output on the ARINC."
note("If a fault appears, perform necessary troubleshooting to")
note("correct the fault(s)")

if getCV("A27524") == 1 or getCV("B27524") == 1:
    
    result("Fault occured, correct fault and repeat procedure.")
    pass


instruction("Do an engine shutdown procedure.")

if getCV("Eng_On") == 1:

	call_tps("16Shutdown")
    
    pass
    
instruction("Ensure the secondary channel from the intial power on of the ECU")
note("is the now the primary channel in control of the engine. The initial primary channel")
note("is now the secondary control channel."

if  lvAinControl == 0 and getCV("A27013") == 1:

    result("FADEC check succesful.")
    
else 
    if lvAinControl == 1 and getCV("B27013") == 1:
    
        result("FADEC check succesful.")

    else
        result("FADEC check unsuccesful. Troubleshoot FADEC and repeat test.")
        
        pass
    pass
pass

instruction("Repeat steps 3 - 10.")


# command for repeating steps?    



TestYes = prompt_boo("Is Test Fadec check completed?")


if TestYes:
	result("Test Fadec check completed and authorized. {} Test4 ".format(REPORT))

	pass

Functional = prompt_boo("Do you want to procede to the Functional Check?")

if VibSurvey:
	auto_start("10FunctionalCheck")

	pass
    
