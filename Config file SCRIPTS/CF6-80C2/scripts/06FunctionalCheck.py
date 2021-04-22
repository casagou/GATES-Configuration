import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 04FunctionalCheck.py
#******************************************************************************
#*  AUTHOR: J.Si
#*
#*  DESCRIPTION:
#*  CF6-80 ENGINE MANUAL GEK92451 - Rev ,Dated: 06/01/2006
#*  EM 72-00-00 ENGINE TESTING
#*  CF6-80 Functional Check Procedure
#*  TESTING 005,004,005,006 TASK 72-00-00-760-005-C
#*
#*  MODIFICATIONS:
#*    REV    DATE         WHO  NCR    DESCRIPTION
#*    1.00   01/04/20     JSi   ---    Initial write
#*
#*
#*
#******************************************************************************

TestYes = None

# Channel Registration

channel("Eng_On,IdleCtrlST,GIFlag,FIFlag,N1TO,N1MC,N1_OBS,N2_OBS,N2GIL,N2GIH,N2FIH,N2FIL,TT2,T495SELAOB,OILQTY,FANBRGN1,FANBRGN2,FANBRGN1_ALT,FANBRGN2_ALT,VIBCRFN1,VIBCRFN2,POIL,PoilC,POILCLOLO,POILCHIHI,FN,WF,VSVSEL,VBVSEL,VibReset,Accel,Vib1N1Pk,Vib2N1Pk,N1atV1MxA,N1atV2MxA,Vib1N2Pk,Vib2N2Pk,N2atV1MxA,N2atV2MxA,Vib1N1PkD,Vib2N1PkD,N1atV1MxD,N1atV2MxD,Vib1N2PkD,Vib2N2PkD,N2atV1MxD,N2atV2MxD")



# ***** TESTING 005 PARA 3.A *****

if getCV("Eng_On") == 0:
	call_tps("04AutoStart.py")

	pass

#show_view("rtd2host","View 0","Idle.v")


instruction("Stabilize engine at GROUND IDLE for 5 minutes")

note("Make sure the VSVs are withing limits")

wait("GIFlag=1",180,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Not at GI after 3min")

if SkipGV:
	result("Ground Idle not Selected",REPORT + "FuncCheck")

else:
	result("Ground Idle Selected",REPORT + "FuncCheck")

	pass
wait("tAtGI>300",30,1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Skip button enable in 30 secs ")


instruction("Record full_set")

do_fullset(5,"Ground Idle Functional Check","GIFuncCheck")

delay(2)


if getCV("N2_OBS") < getCV("N2GIL") or getCV("N2_OBS") > getCV("N2GIH"):
	result("N2 is not within idle limits - adjust",REPORT + "FuncCheck",RED)

	result("N2= {} rpm".format(str(round(getFV("N2_OBS"),4))),REPORT + "FuncCheck",RED)

else:
	result("N2= {} rpm".format(str(round(getFV("N2_OBS"),4))),REPORT + "FuncCheck")

	pass

result("T2 = {} DegC".format(str(round(getFV("TT2"),4))),REPORT + "FuncCheck")

result("Oil Level = {} Qt".format(str(round(getFV("OILQTY"),4))),REPORT + "FuncCheck")

result("N2 = {} rpm".format(str(round(getFV("N2_OBS"),4))),REPORT + "FuncCheck")

result("N1 = {} rpm".format(str(round(getFV("N1_OBS"),4))),REPORT + "FuncCheck")

result("EGT = {} degC".format(str(round(getFV("T495SELAOB"),4))),REPORT + "FuncCheck")

result("Fan Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1"),4))),REPORT + "FuncCheck")

result("Fan Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2"),4))),REPORT + "FuncCheck")

result("Alt Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1_ALT"),4))),REPORT + "FuncCheck")

result("Alt Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2_ALT"),4))),REPORT + "FuncCheck")

result("TMF Vibs N1 = {} mils".format(str(round(getFV("VIBCRFN1"),4))),REPORT + "FuncCheck")

result("TMF Vibs N2 = {} mils".format(str(round(getFV("VIBCRFN2"),4))),REPORT + "FuncCheck")

result("Oil pressure is {} psig.".format(str(round(getFV("POIL"),4))),REPORT + "FuncCheck")

if (getCV("PoilC") <getCV("POILCLOLO")or (getCV("PoilC") >getCV("POILCHIHI"):
	result("Oil pressure is not within idle limits",REPORT + "FuncCheck",RED)

	result("Oil pressure corrected = {} psig".format(str(round(getFV("PoilC"))),REPORT + "FuncCheck",RED)

else:
	result("Oil pressure corrected = {} psig".format(str(round(getFV("PoilC"))),REPORT + "FuncCheck")

	pass
result("VSV = {} deg".format(str(round(getFV("VSVSEL"),4))),REPORT + "FuncCheck")

result("VBV = {} in".format(str(round(getFV("VBVSEL"),4))),REPORT + "FuncCheck")

result("Thrust = {} lbs".format(str(round(getFV("FN"),4))),REPORT + "FuncCheck")

result("WF = {} lbs".format(str(round(getFV("WF"),4))),REPORT + "FuncCheck")



# ***** TESTING 004 PARA 3.D. E. (1) (2) (3) *****

instruction("Select Flight Idle and stabilize for 2 minutes.")

wait("IdleCtrlST=0",3,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Flight Idle has not been selected")

wait("FIFlag=1",180,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Not at FI after 3min")

if SkipGV:
	result("Flight Idle not selected",REPORT + "FuncCheck")

else:
	result("Flight Idle selected",REPORT + "FuncCheck")

	pass
delay(120)


instruction("Record full_set")

do_fullset(5,"Flight Idle","FIFuncCheck")

delay(2)


if (getFV("N2") > getFV("N2FIH"))or(getFV("N2") < getFV("N2FIL")):
	result("N2 is not within idle limits - adjust",REPORT + "FuncCheck",RED)

	result("N2= {} rpm".format(str(round(getFV("N2_OBS"),4))),REPORT + "FuncCheck",RED)

else:
	result("N2= {} rpm".format(str(round(getFV("N2_OBS"),4))),REPORT + "FuncCheck")

	pass

result("T2 = {} DegC".format(str(round(getFV("TT2"),4))),REPORT + "FuncCheck")

result("Oil Level = {} Qt".format(str(round(getFV("OILQTY"),4))),REPORT + "FuncCheck")

result("N2 = {} rpm".format(str(round(getFV("N2_OBS"),4))),REPORT + "FuncCheck")

result("N1 = {} rpm".format(str(round(getFV("N1_OBS"),4))),REPORT + "FuncCheck")

result("EGT = {} degC".format(str(round(getFV("T495SELAOB"),4))),REPORT + "FuncCheck")

result("Fan Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1"),4))),REPORT + "FuncCheck")

result("Fan Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2"),4))),REPORT + "FuncCheck")

result("Alt Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1_ALT"),4))),REPORT + "FuncCheck")

result("Alt Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2_ALT"),4))),REPORT + "FuncCheck")

result("TMF Vibs N1 = {} mils".format(str(round(getFV("VIBCRFN1"),4))),REPORT + "FuncCheck")

result("TMF Vibs N2 = {} mils".format(str(round(getFV("VIBCRFN2"),4))),REPORT + "FuncCheck")

result("Oil pressure is {} psig.".format(str(round(getFV("POIL"),4))),REPORT + "FuncCheck")

if (getCV("PoilC") <getCV("POILCLOLO")or (getCV("PoilC") >getCV("POILCHIHI"):
	result("Oil pressure is not within idle limits",REPORT + "FuncCheck",RED)

	result("Oil pressure corrected = {} psig".format(str(round(getFV("PoilC"),4))),REPORT + "FuncCheck",RED)

else:
	result("Oil pressure corrected = {} psig".format(str(round(getFV("PoilC"),4))),REPORT + "FuncCheck")

	pass
result("VSV = {} deg".format(str(round(getFV("VSVSEL"),4))),REPORT + "FuncCheck")

result("VBV = {} in".format(str(round(getFV("VBVSEL"),4))),REPORT + "FuncCheck")

result("Thrust = {} lbs".format(str(round(getFV("FN"),4))),REPORT + "FuncCheck")

result("WF = {} lbs".format(str(round(getFV("WF"),4))),REPORT + "FuncCheck")



# ***** TESTING 004 PARA 3.E *****

instruction("Stabilize at ground idle for 5 minutes")

note("Make sure the VSVs are withing limits")

set_channel("IdleCtrl",1)

wait("IdleCtrlST=1",3,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Ground Idle has not been selected")

wait("GIFlag=1",180,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Not at GI after 3min")

if SkipGV:
	result("Ground Idle not Selected",REPORT + "FuncCheck")

else:
	result("Ground Idle Selected",REPORT + "FuncCheck")

	pass
wait("tAtGI>300",30,1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Skip button enable in 30 secs ")



# ***** TESTING 005 PARA 3.C *****

set_channel("VibReset",1)

delay(2)

set_channel("VibReset",0)

set_channel("Accel",1)


start_log("Vibration","VibAccel")

start_log("VSVVBV","Accel")


instruction("Do a 2 minutes acceleration to Take Off Power.")

wait("N1=getCV("N1TO")" ,200,10,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"N1 not at Take Off")

if SkipGV:
	result("Operator skipped Take Off point",REPORT+"FuncCheck")

else:
	result("Engine at Take Off")

	pass
delay(2)


stop_log("Vibration")

stop_log("VSVVBV")

do_fullset(1,"Vib Survey Accel","Vib_Survey_Acc")


delay(3)


result("Max #1 Brg Vibn = {} mils. N1 = {} rpm.".format(str(round(getFV("Vib1N1Pk"),4)) ,str(round(getFV("N1atV1MxA"),4))),REPORT+"FuncCheck")

result("Max TRF Flange Vibn = {} mils. N1 = {} rpm.".format(str(round(getFV("Vib2N1Pk"),4)) ,str(round(getFV("N1atV2MxA"),4))),REPORT +"FuncCheck")

result("Max #1 Brg Vibn = {} mils. N2 = {} rpm.".format(str(round(getFV("Vib1N2Pk"),4)) ,str(round(getFV("N2atV1MxA"),4))),REPORT +"FuncCheck")

result("Max TRF Vibn = {} mils. N2 = {} rpm.".format(str(round(getFV("Vib2N2Pk"),4)) ,str(round(getFV("N2atV2MxA"),4))),REPORT +"FuncCheck")


# ********  3.D   *********

instruction("Decelerate to MC Power and stabilize for 5 minutes.")


wait("N1= getCV("N1MC")" ,30,10,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Engine not at MC power")

if SkipGV:
	result("Operator skipped MC point",REPORT+"FuncCheck")

else:
	result("Engine at Max Continuous")

	pass
delay(180)


instruction("Record full_set")

do_fullset(10,"Functional Check","MC_Warmup")


result("T2 = {} DegC".format(str(round(getFV("TT2"),4))),REPORT + "FuncCheck")

result("Oil Level = {} Qt".format(str(round(getFV("OILQTY"),4))),REPORT + "FuncCheck")

result("N2 = {} rpm".format(str(round(getFV("N2_OBS"),4))),REPORT + "FuncCheck")

result("N1 = {} rpm".format(str(round(getFV("N1_OBS"),4))),REPORT + "FuncCheck")

result("EGT = {} degC".format(str(round(getFV("T495SELAOB"),4))),REPORT + "FuncCheck")

result("Fan Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1"),4))),REPORT + "FuncCheck")

result("Fan Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2"),4))),REPORT + "FuncCheck")

result("Alt Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1_ALT"),4))),REPORT + "FuncCheck")

result("Alt Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2_ALT"),4))),REPORT + "FuncCheck")

result("TMF Vibs N1 = {} mils".format(str(round(getFV("VIBCRFN1"),4))),REPORT + "FuncCheck")

result("TMF Vibs N2 = {} mils".format(str(round(getFV("VIBCRFN2"),4))),REPORT + "FuncCheck")

result("Oil pressure is {} psig.".format(str(round(getFV("POIL"),4))),REPORT + "FuncCheck")

if (getCV("PoilC") <getCV("POILCLOLO")or (getCV("PoilC") >getCV("POILCHIHI"):
	result("Oil pressure is not within idle limits",REPORT + "FuncCheck",RED)

	result("Oil pressure corrected = {} psig".format(str(round(getFV("PoilC"),4))),REPORT + "FuncCheck",RED)

else:
	result("Oil pressure corrected = {} psig".format(str(round(getFV("PoilC"),4))),REPORT + "FuncCheck")

	pass
result("VSV = {} deg".format(str(round(getFV("VSVSEL"),4))),REPORT + "FuncCheck")

result("VBV = {} in".format(str(round(getFV("VBVSEL"),4))),REPORT + "FuncCheck")

result("Thrust = {} lbs".format(str(round(getFV("FN"),4))),REPORT + "FuncCheck")

result("WF = {} lbs".format(str(round(getFV("WF"),4))),REPORT + "FuncCheck")


delay(120)


# ********  3.E   *********

instruction("Acceleration to Take Off Power in 10 - 15 seconds.")

wait("N1=" +str(round(getFV("N1TO"),4)) ,30,10,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"N1 not at Take Off")

if SkipGV:
	result("Operator skipped Take Off point",REPORT+"FuncCheck")

else:
	result("Engine at Take Off")

	pass
delay(180)

do_fullset(10,"Functional Check","TO_Warmup")


result("T2 = {} DegC".format(str(round(getFV("TT2"),4))),REPORT + "FuncCheck")

result("Oil Level = {} Qt".format(str(round(getFV("OILQTY"),4))),REPORT + "FuncCheck")

result("N2 = {} rpm".format(str(round(getFV("N2_OBS"),4))),REPORT + "FuncCheck")

result("N1 = {} rpm".format(str(round(getFV("N1_OBS"),4))),REPORT + "FuncCheck")

result("EGT = {} degC".format(str(round(getFV("T495SELAOB"),4))),REPORT + "FuncCheck")

result("Fan Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1"),4))),REPORT + "FuncCheck")

result("Fan Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2"),4))),REPORT + "FuncCheck")

result("Alt Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1_ALT"),4))),REPORT + "FuncCheck")

result("Alt Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2_ALT"),4))),REPORT + "FuncCheck")

result("TMF Vibs N1 = {} mils".format(str(round(getFV("VIBCRFN1"),4))),REPORT + "FuncCheck")

result("TMF Vibs N2 = {} mils".format(str(round(getFV("VIBCRFN2"),4))),REPORT + "FuncCheck")

result("Oil pressure is {} psig.".format(str(round(getFV("POIL"),4))),REPORT + "FuncCheck")

if (getCV("PoilC") <getCV("POILCLOLO")or (getCV("PoilC") >getCV("POILCHIHI"):
	result("Oil pressure is not within idle limits",REPORT + "FuncCheck",RED)

	result("Oil pressure corrected = {} psig".format(str(round(getFV("PoilC"),4))),REPORT + "FuncCheck",RED)

else:
	result("Oil pressure corrected = {} psig".format(str(round(getFV("PoilC"),4))),REPORT + "FuncCheck")

	pass
result("VSV = {} deg".format(str(round(getFV("VSVSEL"),4))),REPORT + "FuncCheck")

result("VBV = {} in".format(str(round(getFV("VBVSEL"),4))),REPORT + "FuncCheck")

result("Thrust = {} lbs".format(str(round(getFV("FN"),4))),REPORT + "FuncCheck")

result("WF = {} lbs".format(str(round(getFV("WF"),4))),REPORT + "FuncCheck")


# ********  3.F   *********

set_channel("Accel",0)

start_log("Vibration","Decel")

start_log("VSVVBV","Decel")

delay(2)



instruction("Slowly and constantly decelerate (2min) to MIN IDLE.")

wait("GIFlag=1",150,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Did not reach MIN IDLE in 2.5min")

delay(10)

stop_log("Vibration")

stop_log("VSVVBV")


do_fullset(1,"Vib Survey Deceleration ","Vib_Survey_Dec")

delay(2)

result("Vibration check - Deceleration",REPORT +"Vib_Decel")


result("Max #1 Brg Vibn = {} mils. N1 = {} rpm.".format(str(round(getFV("Vib1N1PkD"),4)) ,str(round(getFV("N1atV1MxD"),4))),REPORT+"FuncCheck")

result("Max TRF Flange Vibn = {} mils. N1 = {} rpm.".format(str(round(getFV("Vib2N1PkD"),4)) ,str(round(getFV("N1atV2MxD"),4))),REPORT +"FuncCheck")

result("Max #1 Brg Vibn = {} mils. N2 = {} rpm.".format(str(round(getFV("Vib1N2PkD"),4)) ,str(round(getFV("N2atV1MxD"),4))),REPORT +"FuncCheck")

result("Max TRF Vibn = {} mils. N2 = {} rpm.".format(str(round(getFV("Vib2N2PkD"),4)) ,str(round(getFV("N2atV2MxD"),4))),REPORT +"FuncCheck")



instruction("Stabilize to Ground Idle for 4 min")

wait("GIFlag=1",180,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Not at GI after 3min")

delay(240)

instruction("Record full_set")

do_fullset(5,"GI point after decel","FuncCheck")

delay(2)

result("T2 = {} DegC".format(str(round(getFV("TT2"),4))),REPORT + "FuncCheck")

result("Oil Level = {} Qt".format(str(round(getFV("OILQTY"),4))),REPORT + "FuncCheck")

result("N2 = {} rpm".format(str(round(getFV("N2_OBS"),4))),REPORT + "FuncCheck")

result("N1 = {} rpm".format(str(round(getFV("N1_OBS"),4))),REPORT + "FuncCheck")

result("EGT = {} degC".format(str(round(getFV("T495SELAOB"),4))),REPORT + "FuncCheck")

result("Fan Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1"),4))),REPORT + "FuncCheck")

result("Fan Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2"),4))),REPORT + "FuncCheck")

result("Alt Vibs N1 = {} mils".format(str(round(getFV("FANBRGN1_ALT"),4))),REPORT + "FuncCheck")

result("Alt Vibs N2 = {} mils".format(str(round(getFV("FANBRGN2_ALT"),4))),REPORT + "FuncCheck")

result("TMF Vibs N1 = {} mils".format(str(round(getFV("VIBCRFN1"),4))),REPORT + "FuncCheck")

result("TMF Vibs N2 = {} mils".format(str(round(getFV("VIBCRFN2"),4))),REPORT + "FuncCheck")

result("Oil pressure is {} psig.".format(str(round(getFV("POIL"),4))),REPORT + "FuncCheck")

if (getCV("PoilC") <getCV("POILCLOLO")or (getCV("PoilC") >getCV("POILCHIHI"):
	result("Oil pressure is not within idle limits",REPORT + "FuncCheck",RED)

	result("Oil pressure corrected = {} psig".format(str(round(getFV("PoilC"),4))),REPORT + "FuncCheck",RED)

else:
	result("Oil pressure corrected = {} psig".format(str(round(getFV("PoilC"),4))),REPORT + "FuncCheck")

	pass
result("VSV = {} deg".format(str(round(getFV("VSVSEL"),4))),REPORT + "FuncCheck")

result("VBV = {} in".format(str(round(getFV("VBVSEL"),4))),REPORT + "FuncCheck")

result("Thrust = {} lbs".format(str(round(getFV("FN"),4))),REPORT + "FuncCheck")

result("WF = {} lbs".format(str(round(getFV("WF"),4))),REPORT + "FuncCheck")

delay(180)



TestYes = prompt_boo("Is Test Functional check completed?")

if TestYes:
	result("Test Functional check completed and authorized.",REPORT + "Test5")

	pass
