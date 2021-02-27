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
#*  DESCRIPTION:CFM56-5B ESM 72-00-00 TESTING 003
#*  <Slam Accel>
#*
#*  DATE: 12/08/2020
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*    ----------   ---  -----  --------------------------------------------------
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
AutoStaYES = None
HighPower = None
SkipAcc = None
TestYes = None
OilConsNow = None

# Channel Registration
channel("Eng_On,GIFlag,N1MC,N1M,N1K,N1TO,N1TO15,N1TO95,tAcc1,tAcc2,TransReset")

channel("B1,B2,B3,B4,B5,B6,B7,B8,B9,ID,MultiDevTest")


#* V1.01 MSk start ***************************************************************************
if getCV("MultiDevTest") == 1:
	if getCV("B8") == 1:
		set_channel("ID", 8)

	elif getCV("B5") == 1 :
		set_channel("ID", 5)

	elif getCV("B9") == 1 :
		set_channel("ID", 9)

	elif getCV("B6") == 1 :
		set_channel("ID", 6)

	elif getCV("B7") == 1 :
		set_channel("ID", 7)

	elif getCV("B4") == 1 :
		set_channel("ID", 4)

	elif getCV("B1") == 1 :
		set_channel("ID", 1)

	elif getCV("B2") == 1 :
		set_channel("ID", 2)

	elif getCV("B3") == 1 :
		set_channel("ID", 3)

		pass
	pass
#* V1.01 MSk end *****************************************************************************

#*  SEQUENCE# 2
if getCV("GIFlag") == 1:
	instruction("Stabilize at MIN IDLE for 5 min. ")

	wait("GIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Did not reach GI in 30 s ")

	delay(300)

	pass

# V1.01 prompt_boo " Is this test conducted immediately after Start run ? ", HighPower
HighPower = prompt_boo("Was the engine warmed up for five minutes at high power? ")

# V1.01 If HighPower Then

if not HighPower:
	instruction("Slowly accelerate (60 sec) to Max Continuous for 5 min.")

	wait("N1K ="+ str(getCV("N1MC")) , 60, 5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Did not reach Max Cont in 60 s ")

	delay(300)

	instruction("Slowly decelerate (60 sec) to GI and stabilize for 5 minutes. ")

	wait("GIFlag = 1", 80, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach GI in 80 s ")

	delay(300)

	pass

#*  SEQUENCE# 3
instruction("Accelerate to TO power and set throttle ")

note(" stop at that position. ")

wait("N1K ="+ str(getCV("N1TO")) , 30, 15, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, " Did not reach target N1TO in 30 s ")


if skipgv:
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

note("position and stabilize for three minutes.")

wait("N1K ="+ str(getCV("N1TO15")) , 30, 5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1K did not reach target in 30 s ")

delay(180)


if skipgv:
	result("Operator skipped  check {} Acceleration ".format(REPORT))

else:
	result("N1K at target rpm. {} Acceleration ".format(REPORT))

	pass

#*  SEQUENCE# 5
set_channel("TransReset", 1)

delay(2)

set_channel("TransReset", 0)

start_log("Acceleration")

instruction("Rapidly move throttle to Take Off stop (in under 1 sec). Monitor N1K speed.")

#wait "N1AcTrgL = 1", 15, 0.1, , , , , , MSG, "Did not reach TO in 15 s"
wait("N1 >"+ str(getCV("N1TO95")), 15, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach 95% TO in 15 seconds.")

stop_log("Acceleration")

delay(5)

do_fullset(5, "Acceleration", "Acceleration")

delay(5)

result("Acceleration time = {} sec. It should not exceed 5 sec. {} Acceleration ".format(getFV("tAcc2") , REPORT))

delay(25)

instruction("Slowly decrease engine N1K speed to MC power.")
wait("N1K >"+ str(getCV("N1MC")), 15, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not at Max Contnuous power.")

if skipgv:
	result("Operator skipped returning engine to MC power {} Acceleration ".format(REPORT))
	pass


#*  SEQUENCE# 6
TestYes = prompt_boo("Is the Acceleration check test completed?")


if TestYes:
	result("Acceleration check test completed {} Acceleration ".format(REPORT))

	pass
    

TestYes = prompt_boo("Do you want to start an Engine Performance Check?")

if TestYes:
	auto_start("98Performance_Multi")
else:
	instruction("Slowly move throttle to Min IDLE position")
	note("and select next test procedure.")
	wait("GIFlag = 1", 35, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not at Min IDLE.")
	pass
pass 