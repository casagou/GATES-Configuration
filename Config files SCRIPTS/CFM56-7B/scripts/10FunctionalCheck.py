import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 10FunctionalCheck.tps
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:REFERANCE CFM56-7B ENGINE MANUAL 72-00-00 TESTING 002
#*  Functional Check, CFM56-7B Manual, TESTING 002, page 1306
#*
#*  DATE: 12/16/2020
#*
#*  MODIFICATIONS:
#*  REV   DATE         WHO  NCR    DESCRIPTION
#*  
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
AutoStrt = None
VibSurvey = None


# Channel Registration
channel("Eng_On,FI,EngStable,MCFlag,tAtGI,GIFlag,AIFlag,N1K,ID,ID_N1TOMx")


#set_channel("ID", round(getCV("ID_N1TOMx"), 4))


if getCV("Eng_On") == 0:
    
    instruction("Perform engine start procedure.")

       AutoStrt = prompt_boo("Enter YES for Enhanced Start or NO for Manual Start.")

	if AutoStrt:
		call_tps("06EnhancedStart")

	else:
		call_tps("04ManualStart")

		pass
	pass

if getCV("GIFlag") == 0:

	instruction("Stabilize engine at MIN IDLE for 5 minutes")
    
    set_channel("FI",0)
    
	wait("GIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N2 did not reach N2 GI in 30 s ")
    
    pass

wait("tAtGI > 300", 300, 2, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Time at GI has not reached 300 s")

if skipgv:
        result("Operator skipped 5 minute stabilization time {} FunctionalCheck ".format(REPORT))
        pass


instruction("Record fullset")

do_fullset(5, "GI Check ", "FuncCheck_GI")


instruction("Accelerate in 30s to N1K=3500, hold for 5s")

note("the decelerate in 10s to N1K=3300")

wait("N1K = 3500", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1K did not reach 3500 rpm in 30 s.")

delay(5)

wait("N1K = 3300", 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1K did not reach 3300 rpm in 10 s.")

# V1.05 skipgv modified
if skipgv:
	result("Operator skipped 3300 rpm N1K check {} FunctionalCheck ".format(REPORT))

	pass
instruction("Stabilize for 3.5 minutes")

delay(210)

#delay 2
#V1.06 following instruction added
instruction("Record fullset")

do_fullset(5, "3300 N1K", "FuncCheck_1")


instruction("Accelerate in 30s to N1K=4600, hold for 5s")

note("then decelerate in 10s to N1K=4200 rpm")

wait("N1K = 4600", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1K did not reach 4600 rpm in 30 s.")

delay(5)

wait("N1K = 4200", 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1K did not reach 4200 rpm in 10 s.")

# V1.05 skipgv modified
if skipgv:
	result("Operator skipped 4200 rpm N1K check {} FunctionalCheck ".format(REPORT))

	pass
instruction("Stabilize for 3.5 minutes")

delay(210)

#delay 2
#V1.06 following instruction added
instruction("Record fullset")

do_fullset(5, "4200 N1K", "FuncCheck_2")


instruction("Accelerate to MC in 30s, hold for 5s")

note("then decelerate to N1K =4600 rpm")


wait("N1K = "+str(getCV("N1MC")), 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1K did not reach 5042 rpm in 30 s.")

delay(5)

wait("N1K = 4600", 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1K did not reach 4600 rpm in 10 s.")


if skipgv:
	result("Operator skipped 4600 rpm N1K check {} FunctionalCheck ".format(REPORT))

	pass
instruction("Stabilize for 3.5 minutes")

delay(210)


instruction("Record fullset")

do_fullset(5, "4600 N1K", "FuncCheck_3")



instruction("Accelerate in 30s to TO, hold for 5 sec.")
note("then decelerate in 10s to MC")

wait("N1K ="+ str(getCV("N1TO")), 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 s.")


delay(5)


wait("N1K ="+ str(getCV("N1MC")), 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at Max Cont in 10 s.")



if skipgv:
	result("Operator skipped Max Cont check {} FunctionalCheck ".format(REPORT))

	pass
instruction("Stabilize at MC for 5 minutes")
wait("EngStable =1" and "MCFlag = 1", 15, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not stabilized at MC.")

delay(300)


instruction("Record fullset")

do_fullset(5, "FuncCheck_MC", "FuncCheck_MC")



instruction("Rapidly decelerate engine in 1 second to MI and hold for 9 minutes")

caution("If shutdown of engine is requirted, perform only after 9 minutes at MI")



wait("GIFlag = 1", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not at GI after 10 s")


if skipgv:
	result("Operator skipped GI check {} FunctionalCheck ".format(REPORT))

	pass
delay(300)

delay(240)

instruction("Record fullset")

do_fullset(5, "GI Check", "FuncCheck_GI_end")


instruction("Select APPROACH IDLE and hold for 5 min")

note("Stabilize the engine for 5 min.")

set_channel("FI",1)

wait("AIFlag = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, SKIP, "Failed to reach AI in 5 s")

delay(300)

instruction("Record fullset")

do_fullset(5, "AI Check ", "FuncCheck_AI")



instruction("select MIN IDLE and hold for 5 min")

set_channel("FI",0)

wait("GIFlag = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not at GI after 5 s")

delay(300)

instruction("Record fullset")

do_fullset(10, "GI Check ", "FuncCheck_GI")



VibSurvey = prompt_boo("Do you want to perform the Vibration Survey at this time?")


if VibSurvey:
	auto_start("11VibrationSurvey")

	pass