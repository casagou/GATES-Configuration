import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 03ManualStart.py
#******************************************************************************
#*  AUTHOR: J.Si
#*
#*  DESCRIPTION:
#*  CF6-80 ENGINE MANUAL GEK92451 - Rev xx, 07/01/2003
#*  EM 72-00-00 ENGINE TESTING
#*  CF6-80 Starting Procedure
#*  TESTING 003 72-00-00-760-293
#*
#*  MODIFICATIONS:
#*    REV    DATE         WHO  NCR    DESCRIPTION
#*
#*    1.0   01/04/20      JSi   ---    Initial write
#*
#******************************************************************************

# Channel Registration

lv = None


channel("FCS_AirRdy,FCS_FuelRdy,IGN1Pwr,IGN2Pwr,GrndTestMode,SAV_ON,StrtVlvEnST,FuelLvrRunST,SingleIgnitor,DualIgnitor,SingleIGNST,DualIGNST,AutoStrtST,P_Fuel_Fac,OILQTY,IdleCtrlST,IdleCtrl,StartControl,FUEL_ON,TLAFILTR,StartReset,LITF,tToLite,tToLiteMax,POIL,GIFlag,N1_OBS,N2_OBS,PeakEGT,STCorr,tToIdleLim,POILC,POILCLOLO,POILCHIHI,ECUFltChaA,ECUFltChaB,HPTCDelta,LPTCDelta")


# ***** LOCAL VARIABLE DECLARATIONS *****

#show_view("rtd2host", "View 0", "Start.v")

instruction("Ensure all engine control switches are in default position.")

set_channel("FUEL_ON", 0)
set_channel("StartControl", 0)
set_channel("SAV_ON", 0)


note("First starts may be done with cowls open")

caution("DO NOT RUN ABOVE MIN IDLE WITH COWLS OPEN")


# ***** TESTING 003 PARA 2.AA (1) *****

#if getCV("CellRdy") == 1:
	#result("Test Cell ready is ON.", REPORT + "ManStart")

#else:
	#instruction("Set Test Cell Ready status ON.")

	#wait("CellRdy = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Cell Ready light is not.")

	#if SkipGV:
		#result("Operator skipped Script wil abort", REPORT + "Start")

		#quit()

	#else:
		#result("Cell Ready light turned On", REPORT + "Start")

		#pass
	#pass

# ***** TESTING 003 PARA 2.AA (1) (a) ***** Test Cell Starter Inlet Air Pressure Available

if getCV("FCS_AirRdy") == 0:
	instruction("Ensure Facility air supply is ON.")

	
	wait("FCS_AirRdy = 1", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Start Air not responding.")

	if SkipGV:
		result("Operator skipped Start Air ON instruction", REPORT + "Start", YELLOW)

	else:
		result("Start Air turned ON", REPORT + "Start")

		pass
else:
	result("Start Air was already ON", REPORT + "Start")

	pass

# ***** TESTING 003 PARA 2.AA (1) (b) (c)***** Test Cell Fuel Pressure Available

if getCV("FCS_FuelRdy") == 0:
	instruction("Ensure Facility fuel supply is ON")


	wait("FCS_FuelRdy = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel Pump not responding.")

	if SkipGV:
		result("Operator skipped Fuel Pump On instruction", REPORT + "Start")

	else:
		result("Fuel supply turned On", REPORT + "Start")

		pass
	wait("P_Fuel_Fac>15", 30, 5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, MSG, "Test Cell Fuel pressure under 10 psig after 30 secs")

	result("Fuel pressure is {} psig.".format(str(round(getCV("P_Fuel_Fac"), 4)) ), REPORT + "Start")

	pass


# ***** TESTING 003 PARA 2.AA (1) (d) ***** Test Cell Engine Oil Quantity Available

result("Oil Quantity is {} L.".format(str(round(getCV("OILQTY"), 4)) ), REPORT + "Start")


# ***** TESTING 003 PARA 2.AA (1) (e) ***** Engine Minimum Idle selected

if getCV("IdleCtrlST") == 1:
	result("MIN IDLE selected", REPORT + "Start")

else:
	set_channel("IdleCtrl", 1)

	wait("IdleCtrlST = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine NOT in Minimun IDLE")

	if SkipGV:
		result("Operator skipped GROUND mode.", REPORT + "Start")

	else:
		result("Minimun Idle Selected", REPORT + "Start")

		pass
	pass


# ***** TESTING 003 PARA 2.AA (1) (f) ***** Ignition selection - Single


instruction("Select Single ignition ")


wait("SingleIGNST = 1", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "IGNITION SELECT SWITCH not in SINGLE mode. ")

if SkipGV:
	result("Operator skipped SINGLE ignition mode.", REPORT + "Start")

else:
	result("Ignition Mode set to SINGLE", REPORT + "Start")

	pass

# ***** TESTING 003 PARA 2.AA (1) (i) ***** Manual/Auto Start

instruction("Set AUTO/MANUAL SWITCH to MANUAL")


wait("AutoStrtST = 0", 3, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Set AUTO/MANUAL SWITCH to Manual mode. ")

if SkipGV:
	result("Operator skipped Start Mode MANUAL instruction.", REPORT + "Start")

else:
	result("Start Mode set to MANUAL", REPORT + "Start")

	pass


# ***** TESTING 003 PARA 2.AA (1) (i) ***** Starter Air Valve (SAV) OFF

instruction("Engine Start Valve is OFF.")

note(" Adjust to 37.2 + or - 3 psig for ATS100-350 starter .")

note(" Adjust to 31.5 + or - 3 psig for PS600-6 starter .")

note(" Observe Starter Limit Testing 001 Subtask 72-00-00-760-051.")


wait("StrtVlvEnST=0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine Start Air Valve not close within 5 sec")

if SkipGV:
	result("Operator skipped Starter OFF instruction", REPORT + "Start", YELLOW)

else:
	result("Starter turned OFF", REPORT + "Start")

	pass

# ***** TESTING 003 PARA 2.AA (1) (j) ***** Engine Fuel Shutoff OFF

instruction("Set FUEL CONDITION LEVER to CUTOFF position")


if getCV("FuelLvrRunST") == 1:
	wait("FuelLvrRunST = 0", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Master Lever was not set to Cutoff in 10 s")

	if SkipGV:
		result("Operator skipped Master Lever OFF check", REPORT + "Start")

	else:
		result("FUEL CONDITION LEVER is in OFF position", REPORT + "Start")

		pass
else:
	result("FUEL CONDITION LEVER is in OFF position", REPORT + "Start")

	pass

# ***** TESTING 003 PARA 2.AA (1) (k) ***** Engine throttle to Idle position

instruction("Set Throttle to IDLE (35 deg TRA)")

wait("TLAFILTR=35", 6, 1.0, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Throttle is not at GI")

if SkipGV:
	result("Operator skipped Throttle to GI {} Start".format(report), "", YELLOW)

else:
	result("Throttle PLA at 30.5 degree (GI) {} Start".format(report))

	pass


set_channel("StartReset", 1)

delay(2)

set_channel("StartReset", 0)


start_log("Start", "Start")


# ***** TESTING 003 PARA 2.AA (2) ***** Starter Air Valve (SAV) ON

instruction("ENABLE Starter air valve. ")

note(" Adjust to 37.2 + or - 3 psig for ATS100-350 starter .")

note(" Adjust to 31.5 + or - 3 psig for PS600-6 starter .")

note(" Observe Starter Limit Testing 001 Subtask 72-00-00-760-051.")


wait("StrtVlvEnST=1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine Start Air Valve not open within 5 sec")

if SkipGV:
	result("Operator skipped Starter ON instruction", REPORT + "Start", YELLOW)

else:
	result("Starter turned ON", REPORT + "Start")

	pass

# ***** TESTING 003 PARA 2.AA (3) (a) ***** Set FUEL SHUTOFF to ON

instruction("Allow N2 to reach 1500 rpm then Set FUEL CONDITION LEVER to RUN")

wait("N2_OBS>1500", 30, 100, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N2 below 1500rpm")

wait("FuelLvrRunST=1", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Fuel switch not on")

wait("LITF=1", 45, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "No Lite after 45 secs")

#JOA what is Max?

if getCV("tToLite") > getCV("tToLite") Max:
	result("tTolite = {} secs".format(str(round(getCV("tToLite"), 4)) ), REPORT +"Start")

	result("Time to lite is > {} .".format(str(round(getCV("tToLiteMax"), 4)) ), REPORT +"Start", RED)

else:
	result("tTolite = {} secs".format(str(round(getCV("tToLite"), 4)) ), REPORT +"Start")

	pass

# ***** TESTING 003 PARA 2.AA (3) (b) ***** Check for positive and increasing oil pressure

wait("POIL>5", 30, 2.5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "POIL did not reach 2.5 psi. Press SKIP to abort start")

if SkipGV:
	result("Start aborted due to no Oil pressure indication", REPORT + "Start")

	autostart("AbortStart")

else:
	result("Oil pressure indication positive", REPORT + "Start")

	pass



# ***** TESTING 003 PARA 2.AA (4) *****  When core speed N2 is at Minimum Idle,
# *************** ENGINE AT IDLE ***********************

wait("GIFlag = 1", 20, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach idle in 20 s")


instruction("Record start data")

do_fullset(1, "Ground Idle following Start","Start")

delay(2)


# ***** TESTING 003 PARA 2.A (3) (a) ***** If fan speed is not positive in 30 seconds

if getFV("N1_OBS") <10:
	result("NO N1 indication at Idle {}".format(red), REPORT +"Start")

	result("SHUTDOWN ENGINE {}".format(red), REPORT +"Start")

	call_tps("Shutdown")

else:
	result("N1 = {} secs".format(str(round(getFV("N1_OBS"), 4)) ), REPORT +"Start")

	pass

if getFV("POIL") < 10:
	result("Oil pressure below min idle limit of 10 psig {}".format(red), REPORT +"Start")

	result("SHUTDOWN ENGINE {}".format(red), REPORT +"Start")

	call_tps("Shutdown")

else:
	result("Direct OIL pressure = {} psig".format(str(round(getFV("POIL"), 4)) ), REPORT +"Start")

	pass

if getFV("STCorr") >getFV("tToIdleLim"):
	result("Start time longer than permitted", REPORT +"Start")

	result("Start time = {} secs".format(str(round(getFV("STCorr"), 4)) ), REPORT +"Start", RED)

else:
	result("Start time = {} secs".format(str(round(getFV("STCorr"), 4)) ), REPORT +"Start")

	pass


if getFV("PeakEGT") >750:
	result("HOT START EGT Start Max = {} Deg C {}".format(str(round(getFV("PeakEGT"), 4)) , red), REPORT +"Start")

else:
	result("Start Max = {} Deg C".format(str(round(getFV("PeakEGT"), 4)) ), REPORT +"Start")

	pass


# ***** TESTING 003 PARA 2.A (3) (b) ***** If the oil pressure is not in limits, in two minutes

delay(120)


if (getCV("POILC") <getCV("POILCLOLO")or (getCV("POILC") >getCV("POILCHIHI"):
	result("Oil pressure is not within idle limits {}".format(red), REPORT +"Start")

	result("Oil pressure corrected = {} psig {}".format(str(round(getCV("POILC"), 4)) , red), REPORT +"Start")

else:
	result("Oil pressure corrected = {} psig".format(str(round(getCV("POILC"), 4)) ), REPORT +"Start")

	pass


instruction("Set Start Air Supply OFF")

wait("StrtVlvEnST = 0", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Start Air not responding.")

if SkipGV:
	result("Operator skipped Start Air OFF instruction", REPORT + "Start")

else:
	result("Start Air turned OFF", REPORT + "Start")

	pass

instruction("Turn Facility air supply OFF.")

wait("FCS_AirRdy = 0", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility air supply not OFF.")


instruction("Select Ignition 1 & 2 OFF ")

set_channel("IGN1Pwr", 0)
set_channel("IGN2Pwr", 0)



stop_log("Start")


# ***** TESTING 003 PARA 2.AA (5) ***** Stabilize at Minimum Idle for five minutes minimum.

delay(300)

# ***** TESTING 003 PARA 2.AA (6) (d) ***** Interrogate the FADEC Interface Unit (FIU) for FADEC System faults.

if getCV("ECUFltChaA") == 1:
	result("FAULT: ECU Cha A.", REPORT + "Start", RED)

else:
	result("ECU Cha A - NO FAULT", REPORT + "Start")

	pass

if getCV("ECUFltChaB") == 1:
	result("FAULT: ECU Cha B.", REPORT + "Start", RED)

else:
	result("ECU Cha B - NO FAULT", REPORT + "Start")

	pass

if getCV("HPTCDelta") == 1:
	result("FAULT: HPTC DEMAND vs SELECT over 2 %.", REPORT + "Start", RED)

else:
	result("HPTC DEMAND vs SELECT within 2 %", REPORT + "Start")

	pass

if getCV("LPTCDelta") == 1:
	result("FAULT: LPTC DEMAND vs SELECT over 2 %.", REPORT + "Start", RED)

else:
	result("LPTC DEMAND vs SELECT within 2 %", REPORT + "Start")

	pass
