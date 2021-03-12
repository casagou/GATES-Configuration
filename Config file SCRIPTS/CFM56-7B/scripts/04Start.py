import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* <04Start.py>
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:REFERANCE CFM56-7B ENGINE MANUAL 72-00-00 TESTING 000 & 002
#*  10.A & 4.  CFM56-7B Manual Starting Procedure
#*
#*  DATE: 1/6/2021
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*  
#******************************************************************************

# Channel Registration
channel("EngStrtLvr,StrtSwitch,ECUpwrA,ECUpwrB,IgnPwrL,IgnPwrR,Ignit1X,Ignit2X,FIFB,FCS_AirRdy,FCS_FuelRdy,N2PCT,N2,tToLite,tToLiteMax,WFK,EndStartL,tToIdle,EndLite,N2,PEOFILTR,StartReset")

In_ExhOK = None
Numeric = None
#lvIgnSelect = None


#show_view "SMES-RTD2", "View1", "Start.v",0,0,1280,1024

instruction("Ensure Facility fuel and air are OFF")

wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")

wait("FCS_FuelRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Fuel not OFF")

if SkipGV:
	result("Operator skipped Facility OFF instruction {} ManStart ".format(REPORT))

	pass
	

instruction("Before performing start, check inlet and exhaust")

In_ExhOK = prompt_boo("Was inlet and exhaust check satisfactory?")


if In_ExhOK:
	result("Inlet and exhaust checked OK. {} InExCheck ".format(REPORT))

else:
	result("A problem was found in the inlet or exhaust. {} InExCheck ".format(REPORT))

	pass


instruction("Set all engine controls to default positions and ECU power OFF")

set_channel("EngStrtLvr",0)
set_channel("StrtSwitch",0)
set_channel("IgnPwrL",0)
set_channel("IgnPwrR",0)
set_channel("ECUpwrA",0)
set_channel("ECUpwrB",0)
set_channel("FIFB",0)

instruction("Power On the ECU and Ignitors")
set_channel("ECUpwrA",1)
set_channel("ECUpwrB",1)
set_channel("IgnPwrL",1)
set_channel("IgnPwrR",1)

instruction("Turn ON Facility Air & Fuel")
	
wait("FCS_AirRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not ON")

wait("FCS_FuelRdy = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Fuel not ON")



note("NOTE: Make sure the starter air supply is sufficient (25 psig recommended)")

note("NOTE: Make sure there is sufficient fuel pressure.")


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


#added set/clear of StartReset - this is necessary to enable the Start calculations
set_channel("StartReset", 1)

delay(2)

set_channel("StartReset", 0)



instruction("Set Throttle to IDLE (TLA = 0Deg)")

wait("TLA = 0", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "TLA not at IDLE position.")


instruction("Select LEFT or RIGHT Ignitor")

wait("Ignit1X = 1" or "Ignit2X = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Ignition not selected.")


#lvIgnSelect = prompt_num("Select Ignitors: 1-R, 2-L, 3-Both", Numeric, 4, 3)


instruction("Set ENGINE START SWITCH to GRD")

start_log("Start","Start")

set_channel("StrtSwitch", 1)

if getCV("StrtSwitch") == 0:
	wait("StrtSwitch = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "ENGINE START SWITCH not in GRD position.")


	if SkipGV:
		result("Operator skipped ENGINE START SWITCH set to GRD {} Start ".format(REPORT))

	else:
		result("ENGINE START SWITCH set to GRD {} Start ".format(REPORT))

		pass
else:
	result("ENGINE START SWITCH was already in GRD position {} Start ".format(REPORT))

	pass


instruction("Check for positive, increasing oil pressure")

wait("PEOFILTR > 5", 15, 0.5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, "POIL did not reach 5 psi")


if SkipGV:

	result("Operator skipped POIL > 5 psi ")
	
	autostart("05AbortStart.py")
	
	pass

wait("N2PCT > 20", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach 20 % N2 in 30 seconds")


if SkipGV:
	result("Operator skipped N2PCT > 20% ")

	pass


instruction("Set ENGINE START LEVER to IDLE when N2 is over 20%")

#NJ not sure about the wait function below
wait("N2PCT > 20", , , WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT,)

set_channel("EngStrtLvr", 1)


if SkipGV:
	result("Operator skipped Fuel ON instruction {} ManStart ".format(REPORT))

	pass


wait("EndLite = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "No Lite")

if getCV("tToLite") > getCV("tToLiteMax"):
	result("Time to Lite is > {} Start Aborted {} Start ".format(getCV("tToLiteMax"), REPORT), "RED")

	result("Time to lite off exceeded the limit {} Start ".format(Report), "RED")


	pass
	
result("Fuel flow during start is: {} PPH. {} Start ".format(getCV("WFK"), REPORT))


wait("N2 > 7230", 30, 5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N2 speed did not reach 7230 rpm in 30 seconds")


if SkipGV:

	result("Operator skipped N2>7230 rpm ")

	pass

wait("EndStartL = 1", 120, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not achieve IDLE in 2 minutes")


if getCV("tToIdle") > 120:
	result("Time from Fuel ON to Idle exceeded 120 seconds {} Start ".format(REPORT), "RED")

	pass



instruction("Set ENGINE START SWITCH to OFF")



wait("StrtSwitch = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, "Mode Selector Switch not responding.")

if SkipGV:
		result("Operator skipped Mode Selector to NORMAL {} ManStart ".format(REPORT))

else:
	result("Mode Selector Switch selected to NORMAL {} ManStart ".format(REPORT))
	pass


delay(3)



instruction("Record full_set")

do_fullset(1, "Ground Idle following Start", "Start")


stop_log("Start")


instruction("Close Facility Air supply valve")

wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")

