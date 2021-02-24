import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 06EnhancedStart.tps
#******************************************************************************
#*  AUTHOR: John Tamplin
#*
#*  DESCRIPTION:REFERANCE CFM56-7B 72-00-00, TESTING-000, page 1323
#*  IDENTIFIER:(9. CFM56-5C Enhanced Starting Procedure)
#*
#*
#*  DATE: 1/18/2006 4:48:15 PM
#*
#*  MODIFICATIONS:
#*    DATE       WHO  REV    DESCRIPTION
#*
#*    23-Jul-10  ZW   V1.20  5th Bleed Cycle HPT Blade Cycle Update
#*    27/09/08   DP   V1.19  moved prompt for ignitor selection to before rotation begins
#*    27/09/08   DP   V1.18  remove abort starts
#*    20Dec06    DP   V1.17  Decreased POIL wait to 1.5 psi as requested by Mouraffi
#*    19Dec06    DP   V1.16  Added result statement as requested by Mouraffi
#*    18Dec06    DP   V1.15  Minor changes. Cleaned up channel list.
#*    15Dec06    DP   V1.14  Changes to improve timing and speed up Endurance Test
#*    12Dec06    TS   V1.13  POil wait added at 3 psig
#*    07Dec06    DP   V1.12  cleaned up logic of 1.09 through 1.11
#*    05Dec06    TS   V1.11  start/stop log added
#*    05Dec06    TS   V1.10  cv_endurance added
#*    05DEc06    TS   V1.09  prompt_boo,booendr added
#*    19Jun06    TS   V1.08  startmode  changed
#*    10Jun06    TS   V1.07  ">=" modified
#*    09Jun06    TS   V1.06  instruction added
#*    09Jun06    TS   V1.05  skipgv modified
#*    18Jan06    IF          Converted to proDAS script
#*    10Apr06    JT   V1.1   Updated EndLite check
#*    25Mar06    EL          "do_fullset 0" changed to "do_fullset 1"
#*      Jan06    JT   V1.01  New for Morocco based on SRT
#******************************************************************************

# Channel Registration
# V1.15 channel "A27512,A27518,A27519,A27520,B27518,B27519,B27520,FuelEnable,tToLite,WFK_kgHr,EndStartL,tToIdle,FuelOn,EndLite,N2S,ModePosn,APOilLoc,A35122_O,A35121_O,StartMode,GndPower,RIgnit,LIgnit,Nm0,IgSt0,tToLiteMax,Endurance,POIL,StarterFB,StartReset"
channel("FuelEnable,tToLite,WFK_kgHr,EndStartL,Ign_Ref_E,tToIdle,tAtGI,CYCTOT,EndLite,N2S,ModePosn,APOilLoc,A35122_O,A35121_O,StartMode,GndPower,RIgnit,LIgnit,Nm0,IgSt0,tToLiteMax,Endurance,POIL,StarterFB,StartReset,TransReset,N2")

lvIgnSelect = None
Numeric = None
lvidle = None
booendr = None

#*  note 100% N2 = 14460 rpm; 100% N1 = 4784 rpm.
# show_view "SMES-RTD2","View1","Start.v",0,0,1280,1024
# V1.09 added the following prompt_boo and IF logic
if round(getCV("N2S"), 4) <2880:
	if round(getCV("StarterFB"), 4) == 0:
# V1.15 Prompt_boo "Are you performing dry motoring",booendr
# V1.15 if booendr=false then
# V1.14 if cv_StarterFB=0 Then
		instruction("Manually OPEN Test Cell Fuel Supply Valve")

		
		instruction("Turn on Ground Power")

		set_channel("GndPower", 1)

		
		
# instruction "Turn left and right Ignitors ON"
# '*  V1.01 new chn name
# set_channel LIgnit, 1
# wait "A35121_O = 1", 3, 0.1, , , , , , MSG, "Right Ignitor not responding"
# '*  V1.01 new chn name
# set_channel RIgnit, 1
# wait "A35122_O = 1", 3, 0.1, , , , , , MSG, "Left Ignitor not responding"
#
		instruction("Manually Open Test Cell Start Air supply valve")

		
		note("NOTE: Make sure the starter air supply is sufficient")

		note("      (25 psig recommended)")

		
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

		
		note("NOTE: The ECU will control the Fuel Shut Off Valve and will")

		note("      abort the start is an exceedance occurs")

		
		instruction("Manually Set fuel switch to CUTOFF position")

		
		wait("FuelEnable = 0", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel select switch not in Cutoff position after 10 s.")

# V1.05 skipgv modified
		if skipgv:
			result("Operator skipped fuel select switch Cutoff check. Procedure aborted. {} EnhStart ".format(REPORT))

			quit()

			pass
		
		instruction("Manually Set Throttle to GI (36 Deg)")

		wait("TLA = 36", 5, 2, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Throttle not at 36 Deg after 3 s")

		
		instruction("Set Manual Start switch OFF ")

#* V1.08 startmode  changed set_channel StartMode, 1
		set_channel("StartMode", 1)

		wait("A27211 = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Place StartMode switch in Manual mode ")

#V1.05 skipgv modified
		if skipgv:
			result("Operator skipped Start Mode Manual instruction. {} EnhStart ".format(REPORT))

		else:
			result("Start Mode set to Manual {} EnhStart ".format(REPORT))

			pass
		
		instruction("Set Mode Selector Normal switch to ON")

		
		if round(getCV("ModePosn"), 4) != 2:
#*  V1.01 new chn name
			set_channel("Nm0", 1)

			wait("ModePosn = 2", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Mode Selector Switch not responding. ")

			if skipgv:
				result("Operator skipped Mode Selector to NORMAL {} EnhStart ".format(REPORT))

			else:
				result("Mode Selector Switch selected to NORMAL {} EnhStart ".format(REPORT))

				pass
		else:
			result("Mode Selector Switch was already in NORMAL position {} EnhStart ".format(REPORT))

			pass
# V1.15 added the following set_channels to Resets
		set_channel("StartReset", 1)

		delay(2)

		set_channel("StartReset", 0)

		
#*  define a Start log with:
#*  EGT, WFM, WFM1, N2S, N1S, APOilLoc, TLA
# 	start_log "Start", "Start"
# V1.19 moved the ignitor prompt to here
# V1.20 If cv_Endurance=0 Then
#V1.20 JOA    	prompt_num "Select Ignitors: 1-R, 2-L, 3-Both", lvIgnSelect,Numeric,4,1
		
		lvIgnSelect = prompt_num("Select Ignitors: 1-R, 2-L, 3-Both", Numeric, 4, 3)

		
# V1.20 End If
		
		instruction("Set Mode Selector Ignition switch to ON")

#*  V1.01 new chn name
		set_channel("IgSt0", 1)

		set_channel("Nm0", 0)

		wait("ModePosn = 3", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Mode Selector Switch not responding.  ")

#V1.05 skipgv modified
		if skipgv:
			result("Operator skipped Mode Selector Switch IGNITION instruction {} EnhStart ".format(REPORT))

		else:
			result("Mode Selector Switch selected to IGNITION {} EnhStart ".format(REPORT))

			pass
		
# V1.18  wait "N2S > 2880", 30, 0.1, , , , , , MSG, "Engine didn't reach 20%N2 or Max motoring speed in 30 s.Press SKIP to abort."
#V1.05 skipgv modified
# V1.18   If skipgv Then
# V1.18 autostart "AbortStart"
# V1.18     result "Operator skipped N2S> 2880"
		if round(getCV("Endurance"), 4) == 0:
			start_log("Start", "Start")

			pass
# V1.12 added the Else and End If for (Prompt_boo "Are you performing dry motoring",booendr) If booendr=false
	else:
# V1.14 added the following set_channels to Resets
		set_channel("StartReset", 1)

		delay(2)

		set_channel("StartReset", 0)

#  	start_log "Start", "Start"
		pass
	
	instruction("Check for positive, increasing oil pressure")

# V1.07 ">=" not working
#wait "APOilLoc >= 5", 5, 0.5, , , , , , SKIP, "POIL did not reach 5 psi. Press SKIP to abort"
#wait "POIL > 5", 15, 0.5, , , , , , SKIP, "POIL did not reach 5 psi. Press SKIP to abort"
# V1.13 added the following wait
# v1.17 wait "POIL > 3", 15, 0.5, , , , , , SKIP, "POIL did not reach 3 psi. Press SKIP to abort"
	wait("POIL > 1.5", 15, 0.5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, SKIP, "POIL did not reach 1.5 psi. Press SKIP to abort")

# V1.18 added the following if logic on skip
	if skipgv:
		result("Operator skipped POIL > 1.5 ")

		pass
# V1.16 added N2 wait and result statement
	wait("N2 > 2880", 30, 100, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "N2 did not reach 2880 rpm N2 in 30s")

	result("N2 has reached 2080 rpm during motoring cycle {} EnhStart ".format(REPORT))

	
#V1.05 skipgv modified
	if skipgv:
# V1.18  autostart "AbortStart"
		result("Operator skipped N2>2080 ")

		pass
	
# V1.16 Added the following Endurance IF logic
# If cv_Endurance=1 Then
# delay 120
# End If
	
# V1.19  prompt_num "Select Ignitors: 1-R, 2-L, 3-Both", lvIgnSelect,Numeric,4,1
	
	instruction("Turn left and/or right Ignitors ON")

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

				wait("A35121_O =1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "RIgnit not ON")

				wait("A35122_O =1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "LIgnit not ON")

				result("RIgnit and LIgnit are fi {} Start ".format(REPORT), "RED")

				pass
			pass
		pass
# V1.20 Else          ' V1.08 default to use both ignitors for Endurance Test
# V1.20  set_channel "RIgnit",1
# V1.20  set_channel "LIgnit",1
# V1.20  wait "A35121_O =1",3,0.1,,,,,,MSG,"RIgnit not ON"
# V1.20  wait "A35122_O =1",3,0.1,,,,,,MSG,"LIgnit not ON"
# V1.20  result "RIgnit and LIgnit are fired",REPORT &"Start"
#  End if
	
	instruction("10.A.(3)(c) Manually Set Fuel ON when N2 gets to 20%")

	
	wait("FuelEnable = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel not ON")

	if skipgv:
		result("Operator skipped Fuel ON instruction {} EnhStart ".format(REPORT))

		pass
	
#V1.0 wait "LITF = 1", 20, 0.1, , , , , , MSG, "No lite-off after 20 s.                             'Press SKIP to abort Start"
#     If skipgv Then
#	   result "Start aborted", REPORT & "EnhStart"
#	   autostart "AbortStart"
#     End If
	wait("EndLite = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "No Lite afer 20sec Press skip to abort")

	if round(getCV("tToLite"), 4) > round(getCV("tToLiteMax"), 4):
#result "Time to Lite is > " &cv_tToLiteMax& "Start Aborted", REPORT & "EnhStart",RED
		result("Time to Lite is greater than tToLiteMax.Abort Start {} EnhStart ".format(REPORT), "RED")

#autostart "AbortStart"
		pass
	
	result("Fuel flow during start is {} kg per hour. {} EnhStart ".format(round(getCV("WFK_kgHr"), 4) , REPORT))

	
	wait("N2S > 7230", 30, 100, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach 7230 rpm N2 in 30 s. Press SKIP to abort.")

	if skipgv:
# V1.18  autostart "AbortStart"
		result("Operator skipped N2>7230 ")

		pass
	
	wait("EndStartL = 1", 20, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "End Start indication not received in 20 s")

	if round(getCV("tToIdle"), 4) > 120:
		result("Time from Fuel ON to Idle exceeded 120 s {} EnhStart ".format(REPORT), "RED")

		pass
	if round(getCV("Endurance"), 4) == 0:
		instruction("Turn left and right Ignitors OFF")

#*  V1.01 new chn name
#   V1.20 Added for endurance
		set_channel("RIgnit", 0)

		wait("A35121_O = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Right Ignitor not responding")

#*  V1.01 new chn name
		set_channel("LIgnit", 0)

		wait("A35122_O = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Right Ignitor not responding")

		pass
#*  engine at idle
	instruction("Manually Set Mode Selector Normal switch to OFF ")

	if round(getCV("ModePosn"), 4) != 2:
#*  V1.01 new chn name
		set_channel("Nm0", 1)

		set_channel("IgSt0", 0)

		
#*  --------
		wait("ModePosn = 2", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Mode Selector Switch not responding.  ")

		if skipgv:
			result("Operator skipped Mode Selector to NORMAL {} EnhStart ".format(REPORT))

		else:
			result("Mode Selector Switch selected to NORMAL {} EnhStart ".format(REPORT))

			pass
	else:
		result("Mode Selector Switch was already in NORMAL position {} EnhStart ".format(REPORT))

		pass
	
#	If cv_ModePosn <> 2 Then
#*  V1.01 new chn name
#	set_channel Nm0, 1
#	set_channel IgSt0, 0
#*  --------
#	wait "ModePosn = 2", 3, 0.1, , , , , , MSG, "Mode Selector Switch not responding.  "
#	If skipgv Then
#		result "Operator skipped Mode Selector to NORMAL", REPORT & "EnhStart"
#	Else
#		result "Mode Selector Switch selected to NORMAL", REPORT & "EnhStart"
#	End If
#	Else
#	result "Mode Selector Switch was already in NORMAL position", REPORT & "EnhStart"
#	End If
# V1.16 removed Fullset for Endurance Testing
	if round(getCV("Endurance"), 4) == 0:
# V1.06 following instruction added
		instruction("Record full set")

		do_fullset(1, "Ground Idle following Start", "AutoStart")

		stop_log("Start")

		instruction("Manually Close Test Cell Start Air supply valve" , SKIP)

#instruction "Manually Set Manual Start switch to OFF"
#* V1.08 startmode changed set_channel StartMode, 0
		set_channel("StartMode", 1)

		wait("A27211 = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Place StartMode switch in Manual mode using ")

		if skipgv:
			result("Operator skipped Start Mode MANUAL instruction. {} EnhStart ".format(REPORT))

		else:
			result("Start Mode set to MANUAL {} EnhStart ".format(REPORT))

			pass
	else:
#V1.10 prompt_boo "Are you performing Endurance test",lvidle
# 	if cv_Endurance=1 Then
#  	instruction "If Endurance test, stabilize engine 3 minutes at min Idle"
# V1.10 delay 60
# V1.20 delay 50 changed idlle delay drom 1 min. to 3 mins (there are 15 secs delay in the EnduranceTO.tps) reduced to 145 secs from 165 secs 26Jul10 per Snecma SMES request
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

					wait("A35121_O =1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "RIgnit not ON")

					wait("A35122_O =1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "LIgnit not ON")

					result("RIgnit and LIgnit are fi {} Start ".format(REPORT), "RED")

					pass
				pass
			pass
		
		set_channel("Ign_Ref_E", 1)

		wait("tAtGI > 121", 130, 1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "GI condition not met in 130s")

		do_fullset(10, "Min Idle", "Min Idle"&round(getCV("CYCTOT"), 4) )

		wait("tAtGI > 181", 190, 1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "GI condition not met in 190s")

#	else
#	instruction "If NOT Endurance Test , Stabilize engine 5 min. at min Idle"
#  	delay 300
#	end if
		pass
else:
	
#V1.20 JOA 	prompt_num "Select Ignitors: 1-R, 2-L, 3-Both", lvIgnSelect,Numeric,4,1
	lvIgnSelect = prompt_num("Select Ignitors: 1-R, 2-L, 3-Both", Numeric, 4, 3)

	instruction("Turn left and/or right Ignitors ON")

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

				wait("A35121_O =1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "RIgnit not ON")

				wait("A35122_O =1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "LIgnit not ON")

				result("RIgnit and LIgnit are fi {} Start ".format(REPORT), "RED")

				pass
			pass
		pass
	instruction("Set Mode Selector Ignition switch to ON")

	set_channel("IgSt0", 1)

	set_channel("Nm0", 0)

	wait("ModePosn = 3", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Mode Selector Switch not responding.  ")

	if skipgv:
		result("Operator skipped Mode Selector Switch IGNITION instruction {} EnhStart ".format(REPORT))

	else:
		result("Mode Selector Switch selected to IGNITION {} EnhStart ".format(REPORT))

		pass
	instruction("10.A.(3)(c) Manually Set Fuel ON when N2 gets to 20%")

	wait("FuelEnable = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel not ON")

	if skipgv:
		result("Operator skipped Fuel ON instruction {} EnhStart ".format(REPORT))

		pass
	wait("EndLite = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "No Lite afer 20sec Press skip to abort")

	if round(getCV("tToLite"), 4) > round(getCV("tToLiteMax"), 4):
		result("Time to Lite is greater than tToLiteMax.Abort Start {} EnhStart ".format(REPORT), "RED")

		pass
	result("Fuel flow during start is {} kg per hour. {} EnhStart ".format(round(getCV("WFK_kgHr"), 4) , REPORT))

	wait("N2S > 7230", 30, 100, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach 7230 rpm N2 in 30 s. Press SKIP to abort.")

	if skipgv:
		result("Operator skipped N2>7230 ")

		pass
	wait("EndStartL = 1", 20, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "End Start indication not received in 20 s")

	if round(getCV("tToIdle"), 4) > 120:
		result("Time from Fuel ON to Idle exceeded 120 s {} EnhStart ".format(REPORT), "RED")

		pass
	instruction("Manually Set Mode Selector Normal switch to OFF ")

	if round(getCV("ModePosn"), 4) != 2:
#*  V1.01 new chn name
		set_channel("Nm0", 1)

		set_channel("IgSt0", 0)

		
#*  --------
		wait("ModePosn = 2", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Mode Selector Switch not responding.  ")

		if skipgv:
			result("Operator skipped Mode Selector to NORMAL {} EnhStart ".format(REPORT))

		else:
			result("Mode Selector Switch selected to NORMAL {} EnhStart ".format(REPORT))

			pass
	else:
		result("Mode Selector Switch was already in NORMAL position {} EnhStart ".format(REPORT))

		pass
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

				wait("A35121_O =1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "RIgnit not ON")

				wait("A35122_O =1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "LIgnit not ON")

				result("RIgnit and LIgnit are fi {} Start ".format(REPORT), "RED")

				pass
			pass
		pass
	
	set_channel("Ign_Ref_E", 1)

	wait("tAtGI > 121", 130, 1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "GI condition not met in 130s")

	do_fullset(10, "Min Idle", "Min Idle {}".format(round(getCV("CYCTOT"), 4)) )

	wait("tAtGI > 181", 190, 1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "GI condition not met in 190s")

	pass
