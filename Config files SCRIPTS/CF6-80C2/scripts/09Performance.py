import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 09Performance.py
#******************************************************************************
#*  AUTHOR: J.Si
#*
#*  DESCRIPTION:
#*  CF6-80 ENGINE MANUAL GEK92451 - Rev , Dated: 12/01/2007
#*  EM 72-00-00 ENGINE TESTING
#*  CF6-80 Performance Procedure
#*  TESTING 007 TASK 72-00-00-760-007-C
#*
#*  MODIFICATIONS:
#*    REV    DATE         WHO  NCR    DESCRIPTION
#*    1.0   01/04/20      JSi   ---    Initial write
#*
#******************************************************************************
lvtemp = None
tempvar0gv = None
lvWarmup = None
lvStOilC = None
TestYes = None
TestYes1 = None
OilYes = None
lvTP = None
lvPerfo = None

channel("Eng_On, N1MC, N1_OBS, N2_OBS, VSV, VBV, N1TO, N2GIH, N2GIL, N2FIH, N2FIL, TT2,T495SELAOB, OILQTY, FANBRGN1, FANBRGN2, FANBRGN1_ALT, FANBRGN2_ALT, VIBCRFN1, VIBCRFN2, POIL, POILC,POILCLOLO,POILCHIHI,FNnet, WF,VSVSEL,VBVSEL, IdleCtrl, FIFlag, GIFlag, FNK_MC, FNK_TO, FNKSD, FNMAR, FNMar_MC, FNMar_TO, EGTHDMar_MC, EGTHDMar_TO, EGTMAR, EGTKSD_MC, EGTKSD_TO, EGTKSD, EGTKHD_MC, EGTKHD_TO, EGTKHD, WFK_MC, WFK_TO, WFKSD, WFMAR_TO, WFMAR_MC, WFMAR, N2KHD_MC, N2KHD_TO, N2KHD, N2HDMar_TO, N2KSD_MC, N2KSD_TO, N2KSD, N2HDMar_MC, N2MAR, FNMPC, N1KSDMC, N1KSDTO, N1KTest, N1ModLvlTO, N1ModLvlMC, tAtGI, B2F, B1F, B4F")



# ***** TESTING 007 PARA 3.B. (1) (a) *****
if getCV("Eng_On") == 0:
	call_tps("04AutoStart")

	pass

#show_view("rtd2host", "View 0", "Idle.v")


instruction("Stabilize at ground idle for 5 minutes")

note("Make sure the VSVs are within limits")

wait("GIFlag=1", 180, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Not at GI after 3min")

if SkipGV:
	result("Ground Idle not Selected", REPORT + "PerfCheck")

else:
	result("Ground Idle Selected", REPORT + "PerfCheck")

	pass
wait("tAtGI>300", 30, 1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Skip button enable in 30 secs ")


instruction("Record full_set")

do_fullset(5, "Ground Idle Functional Check","GIPerfCheck")

delay(2)


if (getFV("N2_OBS") <getFV("N2GIL")or (getFV("N2_OBS") >getFV("N2GIH"):
	result("N2 is not within idle limits - adjust", REPORT + "PerfCheck", RED)

	result("N2= {} rpm".format(str(round(getFV("N2_OBS"), 4)) ), REPORT + "PerfCheck", RED)

else:
	result("N2= {} rpm".format(str(round(getFV("N2_OBS"), 4)) ), REPORT + "PerfCheck")

	pass

result("T2 = {} DegC".format(str(round(getFV("TT2"), 4)) ), REPORT + "PerfCheck")

result("Oil Level = {} Qt".format(str(round(getFV("OILQTY"), 4)) ), REPORT + "PerfCheck")

result("N2 = {} rpm".format(str(round(getFV("N2_OBS"), 4)) ), REPORT + "PerfCheck")

result("N1 = {} rpm".format(str(round(getFV("N1_OBS"), 4)) ), REPORT + "PerfCheck")

result("EGT = {} degC".format(str(round(getFV("T495SELAOB"), 4)) ), REPORT + "PerfCheck")

result("Fan Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1"), 4)) ), REPORT + "PerfCheck")

result("Fan Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2"), 4)) ), REPORT + "PerfCheck")

result("Alt Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1_ALT"), 4)) ), REPORT + "PerfCheck")

result("Alt Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2_ALT"), 4)) ), REPORT + "PerfCheck")

result("TMF Vibs N1 = {} mils".format(str(round(getFV("VIBCRFN1"), 4)) ), REPORT + "PerfCheck")

result("TMF Vibs N2 = {} mils".format(str(round(getFV("VIBCRFN2"), 4)) ), REPORT + "PerfCheck")

result("Oil pressure is {} psig.".format(str(round(getFV("POIL"), 4)) ), REPORT + "PerfCheck")

if (getFV("POILC") <getFV("POILCLOLO")or (getFV("POILC") >getFV("POILCHIHI"):
	result("Oil pressure is not within idle limits", REPORT + "IdleLeakCheck", RED)

	result("Oil pressure corrected = {} psig".format(str(round(getFV("POILC"), 4)) ), REPORT + "PerfCheck", RED)

else:
	result("Oil pressure corrected = {} psig".format(str(round(getFV("POILC"), 4)) ), REPORT + "PerfCheck")

	pass
result("VSV = {} deg".format(str(round(getFV("VSVSEL"), 4)) ), REPORT + "PerfCheck")

result("VBV = {} in".format(str(round(getFV("VBVSEL"), 4)) ), REPORT + "PerfCheck")

result("Thrust = {} lbs".format(str(round(getFV("FNnet"), 4)) ), REPORT + "PerfCheck")

result("WF = {} lbs".format(str(round(getFV("WF"), 4)) ), REPORT + "PerfCheck")


instruction("Select Flight Idle and stabilize for 2 minutes.")

set_channel("IdleCtrl", 2)

wait("FIFlag=1", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at AI after 10s")

if SkipGV:
	result("Flight Idle not attained", REPORT + "PerfCheck")

else:
	result("Flight Idle attained", REPORT + "PerfCheck")

	pass
delay(120)


instruction("Record full_set")

do_fullset(5, "Flight Idle","FIPerfCheck")

delay(2)


if (getFV("N2_OBS") <getFV("N2GIL")or (getFV("N2_OBS") >getFV("N2GIH"):
	result("N2 is not within idle limits - adjust", REPORT + "PerfCheck", RED)

	result("N2= {} rpm".format(str(round(getFV("N2_OBS"), 4)) ), REPORT + "PerfCheck", RED)

else:
	result("N2= {} rpm".format(str(round(getFV("N2_OBS"), 4)) ), REPORT + "PerfCheck")

	pass

result("T2 = {} DegC".format(str(round(getFV("TT2"), 4)) ), REPORT + "PerfCheck")

result("Oil Level = {} Qt".format(str(round(getFV("OILQTY"), 4)) ), REPORT + "PerfCheck")

result("N2 = {} rpm".format(str(round(getFV("N2_OBS"), 4)) ), REPORT + "PerfCheck")

result("N1 = {} rpm".format(str(round(getFV("N1_OBS"), 4)) ), REPORT + "PerfCheck")

result("EGT = {} degC".format(str(round(getFV("T495SELAOB"), 4)) ), REPORT + "PerfCheck")

result("Fan Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1"), 4)) ), REPORT + "PerfCheck")

result("Fan Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2"), 4)) ), REPORT + "PerfCheck")

result("Alt Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1_ALT"), 4)) ), REPORT + "PerfCheck")

result("Alt Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2_ALT"), 4)) ), REPORT + "PerfCheck")

result("TMF Vibs N1 = {} mils".format(str(round(getFV("VIBCRFN1"), 4)) ), REPORT + "PerfCheck")

result("TMF Vibs N2 = {} mils".format(str(round(getFV("VIBCRFN2"), 4)) ), REPORT + "PerfCheck")

result("Oil pressure is {} psig.".format(str(round(getFV("POIL"), 4)) ), REPORT + "PerfCheck")

if (getFV("POILC") <getFV("POILCLOLO")or (getFV("POILC") >getFV("POILCHIHI"):
	result("Oil pressure is not within idle limits", REPORT + "IdleLeakCheck", RED)

	result("Oil pressure corrected = {} psig".format(str(round(getFV("POILC"), 4)) ), REPORT + "PerfCheck", RED)

else:
	result("Oil pressure corrected = {} psig".format(str(round(getFV("POILC"), 4)) ), REPORT + "PerfCheck")

	pass
result("VSV = {} deg".format(str(round(getFV("VSVSEL"), 4)) ), REPORT + "PerfCheck")

result("VBV = {} in".format(str(round(getFV("VBVSEL"), 4)) ), REPORT + "PerfCheck")

result("Thrust = {} lbs".format(str(round(getFV("FNnet"), 4)) ), REPORT + "PerfCheck")

result("WF = {} lbs".format(str(round(getFV("WF"), 4)) ), REPORT + "PerfCheck")


# ***** TESTING 007 PARA 3.B. (1) (b) *****

instruction("Accelerate to MAX CON and stabilize for 5 minutes", SKIP)

note("Or press SKIP if MC Warmup not required.")

wait("N1_OBS="+str(round(getCV("N1MC"), 4)) , 60, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC after 1min")

if SkipGV:
	result("Operator skipped MC warm up point")

	pass
delay(300)

do_fullset(10, "Perf Point 1 MC","MC_Warmup")


#show_view("rtd2host", "View 0", "PerfCheck.v")


instruction("Accelerate to TAKE OFF, stabilize and take fullset after 3 min")

wait("N1_OBS="+str(round(getCV("N1TO"), 4)) , 60, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO after 1min")

if SkipGV:
	result("Operator skipped Take Off power setting")

	pass
delay(180)

do_fullset(10, "Perf Point: TO","Take_Off")

delay(5)

set_channel("FNK_TO", getFV("FNKSD"))

set_channel("FNMar_TO", getFV("FNMAR"))

set_channel("EGTHDMar_TO", getFV("EGTMAR"))

set_channel("EGTKSD_TO", getFV("EGTKSD"))

set_channel("EGTKHD_TO", getFV("EGTKHD"))

set_channel("WFK_TO", getFV("WFKSD"))

set_channel("WFMAR_TO", getFV("WFMAR"))

set_channel("N2KHD_TO", getFV("N2KHD"))

set_channel("N2HDMar_TO", getFV("N2MAR"))

set_channel("N2KSD_TO", getFV("N2KSD"))

set_channel("N1KSDTO", getFV("N1KTest"))


delay(100)



if getCV("B2F") == 1:
	set_channel("N1ModLvlTO", 0)

	if getCV("B1F")  = 1 or getCV("B4F") = 1 Then
	if getFV("FNMPC") >= 0 and getFV("FNMPC") < 2.4:
		result("N1 Modifier level is 0 {} N1level".format(report))

		pass
	if getFV("FNMPC") >= 2.4 and getFV("FNMPC") < 2.8:
		set_channel("N1ModLvlTO", 1)

		pass
	if getFV("FNMPC") >= 2.8 and getFV("FNMPC") < 3.2:
		set_channel("N1ModLvlTO", 2)

		pass
	if getFV("FNMPC") >= 3.2 and getFV("FNMPC") < 3.6:
		set_channel("N1ModLvlTO", 3)

		pass
	if getFV("FNMPC") >= 3.6 and getFV("FNMPC") < 4:
		set_channel("N1ModLvlTO", 4)

		pass
	if getFV("FNMPC") >= 4 and getFV("FNMPC") < 10:
		set_channel("N1ModLvlTO", 5)

		pass
else:
	if getFV("FNMPC") >= 0 and getFV("FNMPC") < 2.2:
		set_channel("N1ModLvlTO", 0)

		pass
	if getFV("FNMPC") >= 2.2 and getFV("FNMPC") < 2.6:
		set_channel("N1ModLvlTO", 1)

		pass
	if getFV("FNMPC") >= 2.6 and getFV("FNMPC") < 3:
		set_channel("N1ModLvlTO", 2)

		pass
	if getFV("FNMPC") >= 3 and getFV("FNMPC") < 3.4:
		set_channel("N1ModLvlTO", 3)

		pass
	if getFV("FNMPC") >= 3.4 and getFV("FNMPC") < 3.8:
		set_channel("N1ModLvlTO", 4)

		pass
	if getFV("FNMPC") >= 3.8 and getFV("FNMPC") < 10:
		set_channel("N1ModLvlTO", 5)

		pass
	pass
pass


instruction("Decelerate to  MAX CON, stabilize and take fullset after 2 min")

wait("N1_OBS="+str(round(getCV("N1MC"), 4)) , 60, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC after 1min")

if SkipGV == True:
	result("Operator skipped Max Con power setting")

	pass
delay(120)

do_fullset(10, "Perf Point 2 MC","MAX_CONT")

delay(5)

set_channel("FNK_MC", getFV("FNKSD"))

set_channel("FNMar_MC", getFV("FNMAR"))

set_channel("EGTHDMar_MC", getFV("EGTMAR"))

set_channel("EGTKSD_MC", getFV("EGTKSD"))

set_channel("EGTKHD_MC", getFV("EGTKHD"))

set_channel("WFK_MC", getFV("WFKSD"))

set_channel("WFMAR_MC", getFV("WFMAR"))

set_channel("N2KHD_MC", getFV("N2KHD"))

set_channel("N2HDMar_MC", getFV("N2MAR"))

set_channel("N2KSD_MC", getFV("N2KSD"))

set_channel("N1KSDMC", getFV("N1KTest"))


if getCV("B2F") == 1:
	set_channel("N1ModLvlMC", 0)

	IF getCV("B1F")  = 1 or getCV("B4F") = 1 Then
	if getFV("FNMPC") >= 0 and getFV("FNMPC") < 2.4:
		set_channel("N1ModLvlMC", 0)

		pass
	if getFV("FNMPC") >= 2.4 and getFV("FNMPC") < 2.8:
		set_channel("N1ModLvlMC", 1)

		pass
	if getFV("FNMPC") >= 2.8 and getFV("FNMPC") < 3.2:
		set_channel("N1ModLvlTO", 2)

		result("N1 Modifier level is 2 {} N1level".format(report))

		pass
	if getFV("FNMPC") >= 3.2 and getFV("FNMPC") < 3.6:
		set_channel("N1ModLvlMC", 3)

		pass
	if getFV("FNMPC") >= 3.6 and getFV("FNMPC") < 4:
		set_channel("N1ModLvlMC", 4)

		pass
	if getFV("FNMPC") >= 4 and getFV("FNMPC") < 10:
		set_channel("N1ModLvlMC", 5)

		pass
else:
	if getFV("FNMPC") >= 0 and getFV("FNMPC") < 2.2:
		set_channel("N1ModLvlMC", 0)

		pass
	if getFV("FNMPC") >= 2.2 and getFV("FNMPC") < 2.6:
		set_channel("N1ModLvlMC", 1)

		pass
	if getFV("FNMPC") >= 2.6 and getFV("FNMPC") < 3:
		set_channel("N1ModLvlMC", 2)

		pass
	if getFV("FNMPC") >= 3 and getFV("FNMPC") < 3.4:
		set_channel("N1ModLvlMC", 3)

		pass
	if getFV("FNMPC") >= 3.4 and getFV("FNMPC") < 3.8:
		set_channel("N1ModLvlMC", 4)

		pass
	if getFV("FNMPC") >= 3.8 and getFV("FNMPC") < 10:
		set_channel("N1ModLvlMC", 5)

		pass
	pass
pass



instruction("Select GI Stabilize for 5min")

set_channel("IdleCtrl", 1)

wait("GIFlag=1", 150, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, SKIP, "Not at AI after 2.5min")

if SkipGV:
	result("Operator skipped GI power setting")

	pass
delay(180)

instruction("Record full_set")

do_fullset(10, "Perf Point: GI","Perf_GI")

delay(120)


TestYes = prompt_boo("Is Test Performance completed?")

if TestYes:
	result("Test Performance completed and authorized.", REPORT + "Test8")

	pass
