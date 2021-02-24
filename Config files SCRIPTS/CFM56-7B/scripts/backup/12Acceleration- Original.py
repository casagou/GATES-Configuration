import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 12Acceleration.tps
#******************************************************************************
#*  AUTHOR: John Tamplin
#*
#*
#*  DESCRIPTION:Accel: CFM56-7B ENGINE MANUAL 72-00-00,
#*  Identifier : 72-00-00, TESTING 003, Page 1304
#*  3. Acceleration/Deceleration
#*
#*  DATE: 1/27/2006 9:48:57 AM
#*
#*  MODIFICATIONS:
#*    Rev   DATE         WHO  NCR    DESCRIPTION
#*    1.12  03Mar13      MSk  ----   Updated file names in autostart and call_tp calls.
#*    1.11  02Sep09      DP   ----   Added set_channel for ID to solve problem of no Accel Target for Multi-Derivative configuration
#*    1.10  13Dec06      SL   ----   no more showview
#*    1.09  27Nov06      TS   ---    this is not correct
#*    1.08  19Jun06      TS   ----   N1R_TO changed to N1TO
#*    1.07  09Jun06      DP          Added TORange to allow calculations to determine which target is being set
#*    1.06  10Jun06      TS   -----  ">=" modified
#*    1.05  09Jun06      TS   ----   instruction added
#*    1.04  09Jun06      TS   -----   V1.04skipgv modified
#*    1.03  18May06      DP   ----   Added set_channel for TORange
#*    1.02  24/01/2006   JT   -----  V1.00 Initial-Taken from 263
#*    1.01  27/01/2006   IF   -----  V1.01 Conversion to proDAS script
#*    1.00  3/25/2006    EL          "do_fullset 0" changed to "do_fullset 1"
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
SkipAcc = None
booperfor = None

# Channel Registration
channel("Eng_On,GIFlag,tAcc1,tAtGI,TransReset,N1R,N1R_TO,N1TO15,GetAccTrg,Accel,TransReset,TORange,AccelTime,OilConsSta,TOil_OCStr,N1S,N1TO,AccTrg1,ID,ID_N1TOMx")


RTD1 = None

RTD1 = "SMESRTD1"

# v1.10
# show_view "SMES-RTD2", "View1","Acceleration.v",0,0,1280,1024
# V1.11 added the following set_channel
set_channel("ID", round(getCV("ID_N1TOMx"), 4))


instruction("Start Oil consumption")


if round(getCV("Eng_On"), 4) == True:
	call_tps("16Shutdown")

	
	set_channel("OilConsSta", 0)

	delay(2)

	set_channel("OilConsSta", 1)

	
	delay(2)

	
	result("Oil temperature at shut down was {} DegC. {} StartOilCons ".format(round(getCV("TOil_OCStr"), 4) , REPORT))

	delay(300)

	delay(300)

#delay 3
else:
	set_channel("OilConsSta", 0)

	delay(2)

	set_channel("OilConsSta", 1)

	
	delay(2)

	
	result("Oil temperature at shut down was {} DegC. {} StartOilCons ".format(round(getCV("TOil_OCStr"), 4) , REPORT))

	pass


instruction("Within 15 minutes from shutdown check oil level")


caution("Oil tank is pressurized. Wait 10 minutes before removing")

caution("oil tank cap.")

note("If oil level is to high, drain oil tank until oil")

note("level reaches bottom of the filler valve.  If oil is")

note("to be added, add oil to bottom of the filler valve.")


instruction("If engine was shut down, perform following warmup pocedure or SKIP ", SKIP)

if skipgv:
	call_tps("07WarmUp")

	pass

if round(getCV("GetAccTrg"), 4) == False:
	note("IF not already done, Throttle stop at TO must be set")

	instruction("Slowly accelerate to Take Off and")

	note("hold for 30 s and set the throttle stop.")

#* V1.08 wait "N1R = cv_N1R_TO", 120, 10, , , , , , MSG, "Engine not at TO in 120 s."
	wait("N1S ="+ str(round(getCV("N1TO"), 4))  , 120, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 120 s.")

	
# V1.04skipgv modified
	if skipgv:
		result("Operator skipped Take Off for throttle stop {} Acceleration ".format(REPORT))

		pass
	delay(30)

	set_channel("GetAccTrg", 1)

	instruction("Slowly decelerate to Min. Idle ")

	pass

instruction("Stabilize at Idle for 5 minutes")

wait("GIFlag = 1", 90, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Did not reach GI in 90 s ")

# V1.06 ">=" not working
#wait "tAtGI >= 300", 300, 10, , , , SKIP, " Did not stabilize at GI for 5 min"

wait("tAtGI > 300", 300, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, " Did not stabilize at GI for 5 min")


instruction("Slowly accelerate to 15 % of TO thrust and")

note("stabilize for 5 minutes")

wait("N1S = "+str(round(getCV("N1TO15"), 4))  , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "15 % TO N1 not reached in 30 s.")

# V1.04skipgv modified
if skipgv:
	result("Operator skipped 15% TO N1 check {} Acceleration ".format(REPORT))

	pass
delay(300)

#delay 3

set_channel("Accel", 1)

set_channel("TransReset", 1)

delay(2)

set_channel("TransReset", 0)

start_log("Acceleration",  "Accel_log")

#*  TT4.95, N1A, N2A, FNOBS, BIGV, WFM, Vib( if necessary)

# V1.07 added the following set_channel
#set_channel TORange, 1

instruction("2.D.(8)(a) Rapidly advance throttle to full forward thrust")

note("position (throttle stop at TO) and stabilize for 30 s. ")

# V1.06 ">=" not working
#wait "N1R >= cv_N1R_TO", 30, 10, , , , , , MSG, "Engine not at TO in 30 s."
#*V1.08 wait "N1R > cv_N1R_TO", 30, 10, , , , , , MSG, "Engine not at TO in 30 s."
wait("N1S > str(round(getCV("N1TO"), 4)) ", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 s.")

#V1.09 this is not correct: wait "N1S = "& cv_AccTrg1, 30, 10, , , , , , MSG, "Engine not at  %95TO in 30 s."

# V1.04skipgv modified
if skipgv:
	result("Operator skipped Take Off check {} Acceleration ".format(REPORT))

	SkipAcc = 1
else:
	result("Engine reached TO {} Acceleration ".format(REPORT))

	SkipAcc = 0
	pass

if SkipAcc == False:
	result("Acceleration time: {} seconds. {} Acceleration ".format(round(getCV("tAcc1"), 4) , REPORT))

	note("The acceleration time should not exceed 5 seconds.")

	delay(30)

	set_channel("AccelTime", round(getCV("tAcc1"), 4))

#V1.06 following instruction added
	instruction("Record fullset")

	do_fullset(1, "Acceleration to TO FN", "Acceleration_TO")

	
	pass

stop_log("Acceleration")


#instruction "2.C.(8)(b) Rapidly (1 second) decelerate to Ground Idle"
#note "and stabilize for 5 minutes."
#' V1.07 added the following set_channel
#'set_channel TORange, 0
#wait "GIFlag = 1", 10, 0.1, , , , , , MSG, "GI not selected in 10 s"
#delay 300
#'delay 2
#prompt_boo "Do you want to perform performance test", booperfor
#If booperfor Then
#result "Exit accel test and select performance test"
#quit
#else
#result "Conclude oilconsumtion"
#autostart "OilConsumption"
#End If


instruction("2.C.(8) Decelerate to MAX CONT.")

note("Stabilize the engine for 8 min.")


wait("N1S = " + str(round(getCV("N1MC"), 4)) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 30 s.")

#delay 360
#delay 120

#instruction "Record fullset"
#do_fullset 5, "MAX CONT", "MAX_CONT"
#delay 5



