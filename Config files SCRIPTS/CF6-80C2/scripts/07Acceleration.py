import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 07Acceleration.py
#******************************************************************************
#*  AUTHOR: J.Si
#*
#*  DESCRIPTION:
#*  CF6-80 ENGINE MANUAL GEK50481 - Rev 87, 07/15/2017
#*  EM 72-00-00 ENGINE TESTING
#*  CF6-80 Accel Procedure
#*  TESTING 002 72-00-00-760-117
#*
#*  MODIFICATIONS:
#*    REV    DATE         WHO  NCR    DESCRIPTION
#*
#*
#*
#*    1.0   01/04/09      JSi   ---    Initial write
#*
#******************************************************************************
TestYes = None

channel("Eng_On, GIFlag, tAcc1, tAtGI, TransReset, VibReset, AccelOn, TransReset, N1_OBS, N1TO, N1ACC15, N1ACC, Accel")



if getCV("Eng_On") == 0:
	call_tps("04AutoStart")

	pass

#show_view("rtd2host", "View 0", "Acceleration.v")


instruction("Make a slow acceleration to Takeoff Fan Speed (N1).")

wait("N1_OBS=" +str(round(getCV("N1TO"), 4)) , 200, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 not at Take Off")

if SkipGV:
	result("Operator skipped Take Off point", REPORT+"AccelCheck")

else:
	result("Engine at Take Off", REPORT+"AccelCheck")

	pass

instruction("Stabilize for two minutes. Set throttle at stop.")

delay(120)


instruction("Make a slow deceleration to 15%  (N1) Takeoff thrust.")

wait("N1_OBS=" +str(round(getCV("N1ACC15"), 4)) , 100, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 not at 15% N1")

if SkipGV:
	result("Operator skipped 15% N1 point", REPORT+"AccelCheck")

else:
	result("Engine at 15% N1 Take Off thrust.", REPORT+"AccelCheck")

	pass

delay(300)


caution("ENGINE MUST BE STABLE BEFORE DOING SLAM ACCEL")


set_channel("AccelOn", 1)

set_channel("Accel", 1)


set_channel("TransReset", 1)

delay(2)

set_channel("TransReset", 0)


set_channel("VibReset", 1)

delay(2)

set_channel("VibReset", 0)


start_log("Accel","Accel")

result("N1 target is {} rpm.".format(str(round(getCV("N1ACC"), 4)) ), REPORT+"AccelCheck")

instruction("Rapidly (< 1 secs) advance lever to 95% TakeOff N1.")

note(" Hold for Max 10 secs then throttle back to MINIMUM Idle.")

wait("N1_OBS>="+str(round(getCV("N1ACC"), 4)) , 30, 25, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at 95%TO in 30s")

if SkipGV:
	result("Operator skipped Take Off check", REPORT+"AccelCheck")

	pass

do_fullset(1, "Acceleration Check", "Acceleration")


if getFV("tAcc1") > 10:
	result("Acceleration time: {} seconds.".format(str(round(getFV("tAcc1"), 4)) ), REPORT + "AccelCheck", RED)

	result("The acceleration time should not exceed 5 seconds.", REPORT + "AccelCheck", RED)

	result("Test Acceleration check will need to be repeated.", REPORT+"AccelCheck")

else:
	result("Acceleration time: {} seconds.".format(str(round(getFV("tAcc1"), 4)) ), REPORT + "AccelCheck")

	result("The acceleration time is within limit.", REPORT + "AccelCheck")

	result("Test Acceleration check completed and authorized.", REPORT + "Test7")

	pass
delay(5)

set_channel("AccelOn", 0)

stop_log("Accel")


instruction("Stabilize engine at Ground Idle for 5 minutes")

wait("GIFlag = 1", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine N1 spped not at GI")

if SkipGV:
	result("Operator skipped FI check", REPORT + "AccelCheck")

	pass
delay(300)

