import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* <12Acceleration.py>
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:CFM56-7B ESM 72-00-00 TESTING 003
#*  <Slam Accel>
#*
#*  DATE: 12/17/2020
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*    ----------   ---  -----  --------------------------------------------------
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
AutoStaYES = None
SkipAcc = None
TestYes = None
OilConsNow = None
Warmup = None

# Channel Registration
channel("Eng_On,GIFlag,N1MC,N1K,N1TO,N1TO15,N1TO95,tAcc1,tAcc2,TransReset")

channel("B20,B22,B22B1,B24,B24B1,B26,B26B2,B27,ID,Multiple,N1MCWarmup")


#**************************RATING DEFINITION****************************************************
if getCV("Multiple") == 1:
	if getCV("B20") == 1:
		set_channel("ID", 7)

	elif getCV("B22") == 1 :
		set_channel("ID", 5)

	elif getCV("B22B1") == 1 :
		set_channel("ID", 6)

	elif getCV("B24") == 1 :
		set_channel("ID", 3)

	elif getCV("B24B1") == 1 :
		set_channel("ID", 4)

	elif getCV("B26") == 1 :
		set_channel("ID", 2)

	elif getCV("B26B2") == 1 :
		set_channel("ID", 8)

	elif getCV("B27") == 1 :
		set_channel("ID", 1)

		pass
	pass



#*  SEQUENCE# 3
instruction("Accelerate to TO power (TESTING 003 - FIG. 1302)")

note(" and set throttle stop at that position. ")

wait("N1K ="+ str(getCV("N1TO")) , 30, 15, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, " Did not reach target N1TO in 30 s ")


if SkipGV:
	result("Operator skipped N1 TO instruction {} Acceleration ".format(REPORT))

	SkipAcc = 1
else:
	result("N1K reached N1KTO {} Acceleration ".format(REPORT))

	SkipAcc = 0
	pass

note("NOTE: Determine throttle angle to produce stabilized")

note("      take-off N1 and set stop.")


#* show_view "rtd2host", "View 0", "Acceleration.v"
#*  SEQUENCE# 4
instruction("Slowly move thrust lever until N1K = 15% N1TO")

note("position and stabilize for 5 minutes.")

wait("N1K ="+ str(getCV("N1TO15")) , 30, 5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1K did not reach target in 30 s ")

delay(300)


if SkipGV:
	result("Operator skipped  check {} Acceleration ".format(REPORT))

else:
	result("N1K at target rpm. {} Acceleration ".format(REPORT))

	pass

#*  SEQUENCE# 5
set_channel("TransReset", 1)

delay(2)

set_channel("TransReset", 0)

start_log("Acceleration")

instruction("Rapidly move throttle to Take Off stop (in under 1 sec). Monitor N1 speed.")

#wait "N1AcTrgL = 1", 15, 0.1, , , , , , MSG, "Did not reach TO in 15 s"
wait("N1 >"+ str(getCV("N1TO95")), 15, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach 95% TO in 15 seconds.")

stop_log("Acceleration")

delay(5)

do_fullset(5, "Acceleration", "Acceleration")

delay(5)

result("Acceleration time = {} sec. It should not exceed 5 sec. {} Acceleration ".format(getFV("tAcc2") , REPORT))

delay(25)

instruction("Slowly decrease engine N1K speed to MC power.")

set_channel("ID_N1MCMx",getCV("ID"))

result("N1 MC warmup target is: {} +\- 10 rpm ".format(getCV("N1MCWarmup")))

wait("N1K >"+ str(getCV("N1MCWarmup")), 15, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not at Max Contnuous power.")

if SkipGV:
	result("Operator skipped returning engine to MC power {} Acceleration ".format(REPORT))
	pass


#*  SEQUENCE# 6
TestYes = prompt_boo("Is the Acceleration check test completed?")


if TestYes:
	result("Acceleration check test completed {} Acceleration ".format(REPORT))

	pass
	

TestYes = prompt_boo("Do you want to start an Engine Performance Check?")

if TestYes:
	#autostart("98Performance_Multi.py")
	quit()
	
else:

	instruction("Slowly move throttle to Min IDLE position")
	note("and select next test procedure.")
	wait("GIFlag = 1", 35, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not at Min IDLE.")
	pass
pass 