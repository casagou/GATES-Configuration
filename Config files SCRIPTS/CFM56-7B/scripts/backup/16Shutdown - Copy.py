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
resrvstrnggv = None
lvEndurance = None
lvidle = None
bootot = None
boovalve = None

channel("EngStrtLvr,Eng_On,GIFlag,N1RDWN,N2RDWN,LowPOil,IgSt0,RIgnit,Ign_Ref_E,LIgnit,NADownL,tAtMot,NBDownL,NARDWN,NBRDWN,TransReset,tAtGI,LOP,ModePosn,Nm0,A27211,StartMode,NAStop,NBStop,FuelEnable,Crk0,GndPower,FuelQty,RTHr,Endurance,tStarter,StartReset,N2")



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



instruction("Set ENGINE START LEVER to CUTOFF")

wait("EngStrtLvr = 0", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "ENGINE START LEVER not set to CUTOFF in 10 seconds")

# V1.03 skipgv modified
if skipgv:
	result("Operator skipped Cutoff instruction. {} Shutdown ".format(REPORT))

	result("Shutdown will be aborted {} Shutdown ".format(REPORT))

	quit()

else:
	result("Engine shut down {} Shutdown ".format(REPORT))

	pass


caution("MAKE SURE THAT THERE IS AN ENGINE SHUTDOWN AS EVIDENCED")

caution("BY INDICATION OF FUEL SHUT-OFF VALVE CLOSURE.")

caution("CONTINUED ENGINE OPERATION AFTER SELECTING THE FUEL")

caution("OFF INDICATES A MALFUNCTION.")


#*  LowPOil = Low Oil Pressure Warning Light
# wait "LowPOil = 1", 3, 0.1, , , , , , MSG, "LOP warning light didn't come on after 30 s"
wait("LowPOil = 1", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "LOP warning light did not come on after 10 s")


# V1.03 skipgv modified
if skipgv:
	result("Operator skipped LOP warning light operation check {} Shutdown ".format(REPORT))

else:
	result("LOP warning light came on at {} psig. Limits: 65-67 psig {} Shutdown ".format(round(getCV("LOP"), 4) , REPORT))

	pass

#*  Gen_LOP = IDG OIL PRESS LOW WARNING LIGHT
# wait "Gen_LOP = 1", 10, 0.1, , , , , , MSG, "IDG low POil light did not come ON in 10 s."
# If skipgv  Then
# 	result "IDG press low WARNING LIGHT check was skipped by Operator", REPORT & "Shutdown"
# Else
# 	result "IDG press low WARNING LIGHT came on", REPORT & "Shutdown"
# End If
if round(getCV("Endurance"), 4) == 0:
	if round(getCV("ModePosn"), 4) != 2:
		set_channel("Nm0", 1)

		wait("ModePosn = 2", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Mode Selector Switch not responding.")

# V1.03 skipgv modified
		if skipgv:
			result("Operator skipped Mode Selector to NORMAL {} Shutdown ".format(REPORT))

		else:
			result("Mode Selector Switch selected to NORMAL {} Shutdown ".format(REPORT))

			pass
	else:
		result("Mode Selector Switch was already in NORMAL position {} Shutdown ".format(REPORT))

		pass
	instruction("Check N2, EGT and fuel flow for immediate")

	note("indication of engine shutdown.")

	
	instruction("Listen to rundown, report any unusual noises")

	
	instruction("Observe engine for evidence of internal fire or")

	note("tailpipe fire. If they occur, dry motor the engine.")

	
# V1.09 Added the following Endurance IF logic
	RundownOK = prompt_boo("Do you want to do a rollout check?")

	if RundownOK:
		stop1 = prompt_boo("Press YES button when the first rotor has fully stopped")

		set_channel("NAStop", 1)

		stop1 = prompt_boo("Press YES button when the second rotor has fully stopped")

		set_channel("NBStop", 1)

		Rotnbr = prompt_boo("Did N2 Rotor stop first?")

		if Rotnbr == False:
			set_channel("N1RDWN", round(getCV("NARDWN"), 4))

			set_channel("N2RDWN", round(getCV("NBRDWN"), 4))

		else:
			set_channel("N1RDWN", round(getCV("NBRDWN"), 4))

			set_channel("N2RDWN", round(getCV("NARDWN"), 4))

			pass
		
		delay(2)

		result("Rundown times were: N1 = {} secs  N2 = {} secs. {} Shutdown ".format(round(getCV("N1RDWN"), 4) , round(getCV("N2RDWN"), 4) , REPORT))

		pass
	
	
	Whyshutdown = prompt_str("Enter reason for shutdown")

	
# V1.03 note "DRY MOTORING for 2 minutes"
	
# V1.05 prompt_boo "Have you been performing Endurance test" , lvEndurance
# V1.05 if lvEndurance Then
	
# V1.12 chnged dry motoring time from 4 (previous value) to 2
# V1.12  instruction "DRY MOTORING engine for 2 minutes as follows"
# quit
# else
	instruction("DRY MOTORING engine for 2 minutes as follows")

	instruction("Open Test Cell air supply valve")

	instruction("Turn on Ground Power")

	set_channel("GndPower", 1)

	
#*  if enhanced mode is on
# V1.03 iflogicmodified
	if round(getCV("A27211"), 4) == 1:
		instruction("12.B.(4) Set the Start Mode switch to Manual")

		set_channel("StartMode", 1)

		wait("A27211 = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Place StartMode switch in Manual mode")

# V1.03 skipgv modified
		if skipgv:
			result("Operator skipped Start Mode Manual instruction. {} Shutdown ".format(REPORT))

		else:
			result("Start Mode set to Manual {} Shutdown ".format(REPORT))

			pass
		pass
# V1.08 added the following Reset
	set_channel("TransReset", 1)

	delay(2)

	set_channel("TransReset", 0)

	
#V1.06
	instruction("Engage the starter for dry motoring")

	
# set_channel IgSt0,1
# wait "ModePosn = 3", 3, 0.1, , , , , , MSG, "Select Start Mode "
# else
	set_channel("Crk0", 1)

	wait("ModePosn = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Select Crank Mode ")

	
# V1.08 added the following IF logic
	instruction("Check oil pressure rise and check engine for leaks")

	wait("N2S > 300", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "No positive N2 indication in 30 s. Press SKIP to abort Motoring")

# V1.03 skipgv modified
	if skipgv:
		quit()

		pass
	
	wait("N2S > 3900", 30, 100, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "N2 did not reach 3900 rpm N2 in 30s")

	delay(60)

	
# V1.05 prompt_boo "Do you want to close start valve", boovalve
# V1.05 if boovalve Then
# V1.05  instruction "Set the Mode Selector to Normal"
	instruction("Close Start Valve or press SKIP to continue motoring" , SKIP)

	if skipgv == False:
		set_channel("Nm0", 1)

		wait("ModePosn = 2", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Mode Selector Switch not responding.")

# V1.05 else
# V1.03 skipgv modified
		if skipgv:
			result("Operator skipped Mode Selector to NORMAL {} Shutdown ".format(REPORT))

		else:
			result("Mode Selector Switch selected to NORMAL {} Shutdown ".format(REPORT))

			pass
		
		pass
# V1.06 added the following if logic
# V1.08 if cv_Endurance=0 Then
	bootot = prompt_boo("Do you want to record total used fuel and time")

	if bootot:
		result("total used fuel FuelQty= {} KgHr {} shutdown ".format(round(getCV("FuelQty"), 4) , report))

		result("total test duration RTHr= {} sec {} shutdown ".format(round(getCV("RTHr"), 4) , report))

# V1.07 else
# V1.07   instruction "perform next step"
# V1.07 end if
		pass
# V1.07 if cv_Endurance=0 Then
	Whyshutdown = prompt_str("Enter reason for shutdown")

# V1.07 end if
# V1.08 result resrvstrnggv & REPORT & "Shutdown"
# V1.09 added the following else logic
# Else
# V1.11 added N2 wait and result statement
# V1.12 changed delay from 4 minutes down to 2 minutes for 5th Bleed mods
#  wait "N2 > 2080", 30, 20, , , ,SKIP, "N2 did not reach 2880 rpm N2 in 30s"
#  result "N2 has reached 2080 rpm during motoring cycle", REPORT & "EnduranceShutdown"
#  wait "tStarter > 115", 115, 5, , , ,SKIP, "Starter has not been running for 120 seconds"
else:
	if round(getCV("A27211"), 4) == 1:
		instruction("12.B.(4) Set the Start Mode switch to Manual")

		set_channel("StartMode", 1)

		wait("A27211 = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Place StartMode switch in Manual mode")

		if skipgv:
			result("Operator skipped Start Mode Manual instruction. {} Shutdown ".format(REPORT))

		else:
			result("Start Mode set to Manual {} Shutdown ".format(REPORT))

			pass
		pass
	set_channel("StartReset", 1)

	delay(2)

	set_channel("StartReset", 0)

	wait("N2S < 200", 30, 100, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "No positive N2 indication in 30 s. Press SKIP if required")

	instruction("Engage the starter for dry motoring")

	set_channel("IgSt0", 1)

	set_channel("Nm0", 0)

	wait("ModePosn = 3", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Select Start Mode ")

	wait("tAtMot > 121", 125, 21, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "Did not reach time starter on > 120")

	if skipgv:
		result("Operator skipped delay instruction. {} Shutdown ".format(REPORT))

		pass
	
	pass
