import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 02Motoring.py
#******************************************************************************
#*  AUTHOR: JSi
#*
#*  DESCRIPTION:REFERENCE ENGINE MANUAL 72-00-00 TESTING 002
#*  CF6-80 ENGINE MANUAL GEK92451 - Rev
#*  EM 72-00-00 ENGINE TESTING
#*  TESTING 002 - TASK 72-00-00-760-002-C
#*
#*  MODIFICATIONS:
#*    REV    DATE         WHO  NCR    DESCRIPTION
#*
#*
#*    1.0   01/04/20      JSi   ---    Initial write
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
lvtemp = None
lvcheck1 = None
TestYes = None
lvcheck2 = None
InExOK = None
OilReTop = None
RunDwnOK = None
lvChFuel = None


channel("FCS_AirRdy,FCS_FuelRdy,IGN1Pwr,IGN2Pwr,GrndTestMode,StrtVlvEnST,FuelLvrRunST,AutoStrtST,TLAFILTR,StartReset,N1,N2,POIL,ECUModeST,ECUFltChaA, ECUFltChaB,WF")


#show_view("rtd2host", "View 0", "Start.v")


# ***** TESTING 002 PARA 2.A (1) (a) ***** IGNITION switch to OFF.

caution("During the motoring check the cowling must be open to provide access for visual inspection")

caution("THE FUEL PUMP AND HYDROMECHANICAL UNIT ARE FUEL LUBRICATED")

caution("DO NOT MOTOR, START OR OPERATE THE ENGINE UNLESS A POSITIVE FUEL INLET PRESSURE IS INDICATED")


instruction("Ensure ignition power is OFF")

wait("IGN1Pwr = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Ignition 1 status shows IGNITION ON")

if SkipGV:
	result("Operator skipped ignition check", REPORT + "Motoring")

else:
	result("Ignition 1 is in OFF position", REPORT + "Motoring")

	pass

wait("IGN2Pwr = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Ignition 2 status shows IGNITION ON")

if SkipGV:
	result("Operator skipped ignition check", REPORT + "Motoring")

else:
	result("Ignition 2 is in OFF position", REPORT + "Motoring")

	pass


# ***** TESTING 002 PARA 2.A (1) (b) ***** FUEL SHUTOFF lever to OFF.

instruction("Turn Engine fuel OFF")

wait("FuelOn = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel switch not off")

if SkipGV:
	result("Operator skipped turn fuel off {} Motoring".format(report), "", YELLOW)

else:
	result("fuel is in OFF position {} Motoring".format(report))

	pass

# ***** TESTING 002 PARA 2.A (1) (c) ***** AUTO/MANUAL switch to MANUAL.

instruction("Set Start Mode switch to MANUAL")


wait("AutoStrtST = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Set StartMode switch in Manual mode. ")

if SkipGV:
	result("Operator skipped Start Mode MANUAL instruction.", REPORT + "ManStart")

else:
	result("Start Mode set to MANUAL", REPORT + "ManStart")

	pass

# ***** TESTING 002 PARA 2.A (1) (d) ***** FUEL BOOST pump to ON.

if getCV("FCS_FuelRdy") == 0:
	instruction("Turn on facility fuel supply")

	note("Check for fuel leaks with cowling open")


	wait("FCS_FuelRdy = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel Pump not responding.  Use PLC")

	if SkipGV:
		result("Operator skipped Fuel Pump On instruction", REPORT + "TestPreparation")

	else:
		result("Fuel Pump turned On", REPORT + "TestPreparation")

		pass
else:
	result("Facility fuel supply was already ON", REPORT + "TestPreparation")

	pass


instruction("Set Throttle to IDLE (35 deg TRA)")

wait("TLAFILTR=35", 6, 1.0, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Throttle is not at GI")

if SkipGV:
	result("Operator skipped Throttle to GI {} Motoring".format(report), "", YELLOW)

else:
	result("Throttle PLA at 35 degree (GI) {} Motoring".format(report))

	pass

# ***** FACILITY AIR SUPPLY ON ***** 

if getCV("FCS_AirRdy") == 0:
	instruction("Turn on facility air supply")
	
	note(" Adjust to 37.2 + or - 3 psig for ATS100-350 starter .")

	note(" Adjust to 31.5 + or - 3 psig for PS600-6 starter .")

	note("Check for air leaks with cowling open")


	wait("FCS_AirRdy = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel Pump not responding.  Use PLC")

	if SkipGV:
		result("Operator skipped Facility air ON instruction", REPORT + "TestPreparation")

	else:
		result("Facility air turned On", REPORT + "TestPreparation")

		pass
else:
	result("Facility air supply was already ON", REPORT + "TestPreparation")

	pass


# ***** TESTING 002 PARA 2.A (2) ***** Turn STARTER AIR VALVE to ON


set_channel("StartReset", 1)

delay(2)

set_channel("StartReset", 0)

delay(2)



instruction("Energize Engine Start valve.")


note(" Observe Starter Limit Testing 001 Subtask 72-00-00-760-051.")



wait("StrtVlvEnST= 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine Start Air Valve not open within 5 sec")

if SkipGV:
	result("Operator skipped Starter ON instruction", REPORT + "Motoring", YELLOW)

else:
	result("Starter turned ON", REPORT + "Motoring")

	pass

# ***** TESTING 002 PARA 2.A (2) (a) (b) (c) *****

instruction("Allow N2 to stabilize at max crank speed (approx 2200 rpm)")

wait("N2>2200", 30, 200, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N2 below 2000rpm")

wait("N1>200", 1, 20, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 below 200rpm")


instruction("Check for positive and increasing oil pressure")

wait("POIL>2.5", 3, 0.5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "POIL did not reach 2 psi. Press SKIP to ABORT motoring")


# ***** TESTING 002 PARA 2.A (3) *****

instruction("Initiate self test of the FADEC system.")

note("Set GROUND TEST POWER to ON.")


wait("ECUModeST = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "ECU ChA Ground Test switch not responding.")

if SkipGV:
	result("Operator skipped ECU GROUND TEST switch", REPORT + "Motoring")

	pass


note("FADEC must remained powered for a minimum of 30 seconds")

note("for all possible faults to be set.")


delay(30)


if getCV("ECUFltChaA") == 1:
	result("FAULT: ECU Cha A light is ON", REPORT + "Motoring", RED)

else:
	result("ECU Cha A - NO FAULT", REPORT + "Motoring")

	pass

if getCV("ECUFltChaB") == 1:
	result("FAULT: ECU Cha B light is ON", REPORT + "Motoring", RED)

else:
	result("ECU Cha B - NO FAULT", REPORT + "Motoring")

	pass

instruction("Record Fullset")

do_fullset(1, "Dry Motoring Fullset","Motoring")


lvtemp = prompt_boo("Proceed to WET MOTORING?")

if lvtemp:
	
	
# **************** WET MOTORING start *************************
	
	
# ***** TESTING 002 PARA 2.B (4) *****
	
	
	instruction("Set FUEL CONTROL SWITCH to RUN")

	wait("FuelLvrRunST = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel switch not on")

	delay(5)

	wait("WF>200", 30, 100, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel fow is below 100 pph")

	if getCV("WF") >200:
		result("Motoring Fuel Flow = {} lb/hr".format(str(getCV("WF")) ), REPORT +"Motoring")

	else:
		result("Motoring Fuel Flow = {} lb/hr - less than 200 pph".format(str(getCV("WF")) ), REPORT +"Motoring")

		pass
	
	instruction("Record Fullset")

	do_fullset(1,"Wet Motoring","Motoring")

	delay(2)

	result("Fuel flow {} lb/hr".format(str(round(getFV("WF"), 4)) ), REPORT +"Motoring")

	if getFV("WF") >700:
		result("Fuel flow is over 700 lb/hr limit", REPORT +"Motoring", RED)

		pass
	
	
# ***** TESTING 002 PARA 2.B (5) *****
	
	instruction("Set FUEL CONTROL SWITCH to CUTOFF, and continue to motor for 60 s")

	wait("FuelLvrRunST = 0", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel switch not off")

	if SkipGV:
		result("Operator skipped Fuel Supply OFF instruction", REPORT + "Motoring", YELLOW)

	else:
		result("Fuel Supply turned OFF", REPORT + "Motoring")

		pass
	delay(30)

	wait("WF<50", 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel fow is NOT below 50 pph")

	if getCV("WF") >10:
		result("Motoring Fuel Flow = {} lb/hr".format(str(round(getCV("WF"), 4)) ), REPORT +"Motoring", RED)

		result("Fuel flow should drop to zero.", REPORT +"Motoring", RED)

	else:
		result("Fuel flow drop to zero.", REPORT + "Motoring")

		pass
	pass

# **************** WET MOTORING end *************************


# ***** TESTING 002 PARA 2.B (7) *****

instruction("Turn Facility air supply OFF")



wait("FCS_AirRdy = 0", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Start Air not responding.  Use PLC")

if SkipGV:
	result("Operator skipped Start Air OFF instruction", REPORT + "Shutdown", YELLOW)

else:
	result("Start Air turned OFF", REPORT + "Shutdown")

	pass
delay(20)


instruction("De-energize starter. Check for unusual noises during rundown")


wait("StrtVlvEnST=0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Start Air Valve did not close in 5 sec")

if SkipGV:
	result("Operator skipped Start Air OFF instruction", REPORT + "Start", YELLOW)

else:
	result("Start Air turned OFF", REPORT + "Start")

	pass

# ***** TESTING 002 PARA 2.B (8) *****

instruction("Check for leaks and listen for rundowns")


lvcheck2 = prompt_boo("Are there fuel leaks?")

if lvcheck2:
	result("There are fuel leaks", REPORT +"Motoring")

else:
	result("Fuel leak check OK", REPORT +"Motoring")

	pass

lvcheck1 = prompt_boo("Are there oil leaks?")

if lvcheck1:
	result("There are oil leaks", REPORT +"Motoring")

else:
	result("Oil leak check OK", REPORT +"Motoring")

	pass

instruction("Listen to rundown and Check engine, Fan frame ")

note("and turbine area for unusual roughness.")


RunDwnOK = prompt_boo("Was rundown satisfactory?")

if RunDwnOK:
	result("Rundown was satisfactory", REPORT + "Motoring")

else:
	result("There were problems during rundown", REPORT + "Motoring")

	pass

instruction("Check inlet and exhaust")

InExOK = prompt_boo("Were inlet and exhaust found satisfactory when checked?")

if InExOK:
	result("Inlet and exhaust checked OK.", REPORT + "Motoring")

else:
	result("A problem was found in the inlet or exhaust.", REPORT + "Motoring")

	pass

instruction("Top up engine oils if required")

note("Service per 72-00-00, Testing 000, Effect C")


OilReTop = prompt_boo("Were oil levels checked and retopped as required?")

if OilReTop:
	result("Oil levels are checked and retopped", REPORT + "Motoring")

else:
	result("Oil levels are not checked and retopped", REPORT + "Motoring")

	pass

#*  SEQUENCE#
TestYes = prompt_boo("Is Motoring completed?")

if TestYes:
	result("Test Motoring completed and authorized.", REPORT + "Test2")

	pass
