import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* <04ManualStart.tps>
#******************************************************************************
#*  AUTHOR: John Tamplin
#*
#*  DESCRIPTION:REFERANCE CFM56-7B ENGINE MANUAL 72-00-00 TESTING 000
#*  10.A CFM56-7B Manual Starting Procedure
#*
#*  DATE: 1/18/2006 3:44:14 PM
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*    27/09/08     DP   -----  V1.15 remove abort starts; added Reset for start timers
#*    13/13/286    SL   -----  V1.14 Commented out showview
#*    6/10/2006    TS   -----  V1.13 StartMode changed
#*    6/10/2006    TS   -----  V1.12 instruction updated
#*    6/10/2006    TS   -----  V1.11 instruction updated
#*    6/10/2006    TS   -----  V1.09/10 ">=" corrected
#*    6/10/2006    TS   -----  V1.08 Ignition selecting added
#*    6/10/2006    TS   -----  V1.07 prompt_num added
#*    6/09/2006    TS   -----  V1.06 "instruction" added
#*    6/09/2006    TS   -----   v1.05 skipgv modified
#*    1/18/2006    IF   -----  Converted to proDAS script
#*    1/16/2006    JT	        V1.01 New for Morocco based on SRT
#*    3/25/2006    EL          "do_fullset 0" changed to "do_fullset 1"
#*    10Apr06      JT          Updated Time to Lite/Endlite check V1.1
#******************************************************************************


# Channel Registration
channel("GndPower,tToLite,tToLiteMax,WFK_kgHr,EndStartL,tToIdle,EndLite,N2S,A27211,StartMode,ModePosn,APOilLoc,A35122_O,A35121_O,FuelEnable,Nm0,Crk0,IgSt0,LIgnit,RIgnit,StartReset")


lvIgnSelect = None
Numeric = None

#*  [lookup]
#*  channel=
#*  [validation]
#*  security=1
#*  modification="3017230253"
#*  [test script]
#*  name=ManualStart
#/ *
#*  /
#*  IDENTIFIER: 72-00-00, TESTING-000, page 1340
#*  10.A CFM56-7B Manual Starting Procedure
#*  Modification History
#*  Ver   Date       By  Description
#*  V1.01 Jan 2006   JT  New for Morocco based on SRT

# v1.14
#show_view "SMES-RTD2", "View1", "Start.v",0,0,1280,1024

instruction("Manually OPEN Fuel Main Valve")

# V1.11 instraction updated
#instruction "Set the Manual Start switch to ON"
instruction("Set the Manual Start swicth to ON")

set_channel("StartMode", 1)

#*V1.13 StartMode changed
#set_channel StartMode, 0
wait("A27211 = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Place StartMode switch in Manual mode ")

#v1.05 skipgv modified
if skipgv:
	result("Operator skipped Start Mode MANUAL instruction. {} ManStart ".format(REPORT))

else:
	result("Start Mode set to MANUAL {} ManStart ".format(REPORT))

	pass

instruction("Manually Turn on Ground Power")

set_channel("GndPower", 1)

instruction("Manually Open Test Cell Start Air supply valve")


note("NOTE: Make sure the starter air supply is sufficient (25 psig recommended)")


caution("Obey the oil pressure limits. If the engine operates at low")

caution("oil pressures, bearing damage can occur.")


note("NOTE: If the engine was operated during the previous 2 hours, ")

note("      dry-motor the engine for approximately 90 seconds.")

note("NOTE: In the event of an aborted start, the entire starting")

note("       sequence may have to be repeated from the beginning")


caution("Do not operate the engine above the GI with the cowl OPEN.")


note("NOTE: The GI leak check will be done with the cowlings OPEN")


caution("Carefully monitor the start cycle when you use lower starter")

caution("inlet air-pressure than recommended.  Low air-pressure at the")

caution("starter inlet can cause higher peak EGT and unusual time to idle.")


caution("Do not operate the engine if the fuel inlet pressure is not")

caution("positive")


instruction("Manually Set fuel select switch to CUTOFF position")

wait("FuelEnable = 0", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel select switch not in Cutoff position after 10 s.")

# V1.05 skipgv modified
if skipgv:
	result("Operator skipped fuel select switch Cutoff check. Procedure aborted. {} ManStart ".format(REPORT))

	quit()

	pass

# V1.15 added set/clear of StartReset - this is necessary to enable the Start calculations
set_channel("StartReset", 1)

delay(2)

set_channel("StartReset", 0)


instruction("Manually Set Throttle to GI (36 Deg)")

# V1.12 instruction updated
#instruction "Set Mode Selector to Normal"
instruction("Set Mode Selector Normal swicth to ON")

#*  V1.01 new chn name
set_channel("Nm0", 1)

if round(getCV("ModePosn"), 4) != 2:
	wait("ModePosn = 2", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Mode Selector Switch not responding.")

#v1.05 skipgv modified
	if skipgv:
		result("Operator skipped Mode Selector to NORMAL {} ManStart ".format(REPORT))

	else:
		result("Mode Selector Switch selected to NORMAL {} ManStart ".format(REPORT))

		pass
else:
	result("Mode Selector Switch was already in NORMAL position {} ManStart ".format(REPORT))

	pass

instruction("Make sure a sufficient fuel supply is available")

# V1.07 prompt_num added
#prompt_num "Select Ignitors: 1-R, 2-L, 3-Both", lvIgnSelect,Numeric,4,1
lvIgnSelect = prompt_num("Select Ignitors: 1-R, 2-L, 3-Both", Numeric, 4, 3)

#instruction "Make sure there is sufficient fuel pressure"
#*  define a Start log with:
#*  EGT, WFM, WFM1, N2S, N1S, APOilLoc, TLA
#start_log "Start",  Start
# V1.07 start log added
start_log("Start","Start")


instruction("Set Mode Selector to Ignition")


#*  V 1.01 new chn name
set_channel("IgSt0", 1)

set_channel("Nm0", 0)

wait("ModePosn = 3", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, "Mode Selector Switch not responding.")

#v1.05 skipgv modified
if skipgv:
	result("Operator skipped Mode Selector Switch IGNITION instruction {} ManStart ".format(REPORT))

else:
	result("Mode Selector Switch selected to IGNITION {} ManStart ".format(REPORT))

	pass
# V1.08 Ignition selecting added
#instruction "Select Ignition On"
instruction("Turn left and right Ignitors ON")

if lvIgnSelect == 1:
	set_channel("RIgnit", 1)

	wait("A35121_O=1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "RIgnit not ON")

	result("RIgnit is fi {} Start ".format(REPORT), "RED")

else:
	if lvIgnSelect == 2:
		set_channel("LIgnit", 1)

		wait("A35122_O=1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "LIgnit not ON")

		result("LIgnit is fi {} Start ".format(REPORT), "RED")

	else:
		if lvIgnSelect == 3:
			set_channel("RIgnit", 1)

			set_channel("LIgnit", 1)

			wait("A35121_O=1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "RIgnit not ON")

			wait("A35122_O=1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "LIgnit not ON")

			result("RIgnit and LIgnit are fi {} Start ".format(REPORT), "RED")

			pass
		pass
	pass

# instruction "Turn left and right Ignitors ON"
# '*  V1.01 new chn name
# set_channel RIgnit, 1
# wait "A35121_O = 1", 3, 0.1,,,,,"Mode Selector Switch not responding."
# '*  V1.01 new chn name
# set_channel LIgnit, 1
# wait "A35122_O = 1", 3, 0.1,,,,,"Mode Selector Switch not responding."

instruction("Check for positive, increasing oil pressure")

# V1.09 ">=" not working
# wait "APOilLoc >= 5", 5, 0.5,,,,,"POIL did not reach 5 psi. Press SKIP to abort"

# V1.15 wait "APOilLoc > 5", 15, 0.5,,,,,"POIL did not reach 5 psi. Press SKIP to abort start"
wait("APOilLoc > 5", 15, 0.5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, "POIL did not reach 5 psi")


#v1.05 skipgv modified
if skipgv:
# V1.15 autostart "AbortStart"
	result("Operator skipped POIL > 5 psi ")

	pass

# V1.15 "N2S > 2880", 30, 0.1, , , , , , MSG, "Engine didn't reach 20 % N2 or Max motoring speed in 30 s. Press SKIP to abort."
wait("N2S > 2880", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach 20 % N2 or Max motoring speed in 30 s")

#v1.05 skipgv modified
if skipgv:
# V1.15 autostart "AbortStart"
	result("Operator skipped N2S>2880 ")

	pass

instruction("10.A.(3)(c) Manually Set Fuel ON when N2 gets %20")

wait("FuelEnable = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel not ON")

#v1.05 skipgv modified
if skipgv:
	result("Operator skipped Fuel ON instruction {} ManStart ".format(REPORT))

	pass

#old stuff V1.1        'wait "EndLite = 1", 20, 0.1, , , , , , MSG, "No lite-off after 20 s. Press SKIP to abort Start"
#If skipgv Then
#result "Start aborted", REPORT & "ManStart"
#autostart "AbortStart"
#End If

#If cv_tToLite > 15 Then
#result "Time to lite is " & cv_tToLite & " s and it should be 15 s max. Start aborted", REPORT & "ManStart", RED
#autostart "AbortStart"
#End If
wait("EndLite = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "No Lite")

if round(getCV("tToLite"), 4) > round(getCV("tToLiteMax"), 4):
	result("Time to Lite is > {} Start Aborted {} ManStart ".format(round(getCV("tToLiteMax"), 4) , REPORT), "RED")

	result("Time to lite off exceeded the limit {} ManStart ".format(Report), "RED")

# V1.15 instruction "Start can be aborted", skip
#autostart "AbortStart"
	pass
result("Fuel flow during start is: {} kg per hour. {} ManStart ".format(round(getCV("WFK_kgHr"), 4) , REPORT))

# V1.10 ">=" not working
#wait "N2S >= 7230", 30, 50, , , , , , MSG, "Engine didn't reach 7230 rpm N2 in 30 s. Press SKIP to abort."

# V1.15 wait "N2S > 7230", 30, 50, , , , , , MSG, "Engine didn't reach 7230 rpm N2 in 30 s. Press SKIP to abort."
wait("N2S > 7230", 30, 50, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach 7230 rpm N2 in 30 s")


if skipgv:
# V1.15 autostart "AbortStart"
	result("Operator skipped N2S>7230 ")

	pass

wait("EndStartL = 1", 20, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "End Start indication not received in 120 s")

#V1.10 ">=" not working
#If cv_tToIdle >= 120 Then
if round(getCV("tToIdle"), 4) > 120:
	result("Time from Fuel ON to Idle exceeded 120 s {} ManStart ".format(REPORT), "RED")

	pass

#*  engine at idle
# V1.12 instruction updated
#instruction "Set Mode Selector to Normal"

instruction("Manually Set Mode Selector swicth to Normal")


if round(getCV("ModePosn"), 4) != 2:
#*  V1.01 new chn name
	set_channel("Nm0", 1)

	set_channel("IgSt0", 0)

	wait("ModePosn = 2", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, "Mode Selector Switch not responding.")

	if skipgv:
		result("Operator skipped Mode Selector to NORMAL {} ManStart ".format(REPORT))

	else:
		result("Mode Selector Switch selected to NORMAL {} ManStart ".format(REPORT))

		pass
else:
	result("Mode Selector Switch was already in NORMAL position {} ManStart ".format(REPORT))

	pass

delay(3)

instruction("Turn left and right Ignitors OFF")

#*  V1.01 new chn name
set_channel("RIgnit", 0)

wait("A35121_O = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, "Right Ignitor not responding")

#*  V1.01 new chn name
set_channel("LIgnit", 0)

wait("A35122_O = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, "Left Ignitor not responding")


# V1.06 following instruction added
instruction("Record full_set")

do_fullset(1, "Ground Idle following Start", "ManStart")


stop_log("Start")

instruction("Close Test Cell Start Air supply valve" ,SKIP)



