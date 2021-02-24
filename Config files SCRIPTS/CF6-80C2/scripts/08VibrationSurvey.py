import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#*  08VibrationSurvey.py
#******************************************************************************
#*  AUTHOR: J.Si
#*
#*  DESCRIPTION:
#*  CF6-80 ENGINE MANUAL GEK92451 - Rev 87, Dated: 07/01/2003
#*  EM 72-00-00 ENGINE TESTING 006
#*  CF6-80 VIB Survey
#*  TESTING 006 TASK 72-00-00-760-006-C
#*
#*  MODIFICATIONS:
#*   REV    DATE      WHO  NCR    DESCRIPTION
#*
#*
#*   1.0    01/04/20  Jsi   ---    Initial write
#*
#******************************************************************************'
TestYes = None
lvWarm = None

channel("Eng_On, GIFlag, FIFlag, N1TO, N1MC, N1_OBS, VibReset, Accel, Vib1N1Pk, Vib2N1Pk, N1atV1MxA, N1atV2MxA, Vib1N2Pk, Vib2N2Pk, N2atV1MxA, N2atV2MxA, Vib1N1PkD, Vib2N1PkD, N1atV1MxD, N1atV2MxD, Vib1N2PkD, Vib2N2PkD, N2atV1MxD, N2atV2MxD")


if getCV("Eng_On") == 0:
	call_tps("04AutoStart")

	pass

#show_view("rtd2host", "View 0", "VibSurvey.v")


instruction("Stabilze at GI for 5 minutes")

wait("GIFlag=1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at GI after 30s")

delay(180)


instruction("Record fullset")

do_fullset(5,"Readings at GI before Accel","VibSurvey")

delay(120)


lvWarm = prompt_boo("Do you need to Warm Up engine?")

if lvWarm:
	call_tps("WarmUp")

	pass


set_channel("VibReset", 1)

delay(2)

set_channel("VibReset", 0)

set_channel("Accel", 1)


start_log("Vibration","VibAccel")

start_log("VSVVBV","Accel")


result("Vibration Acceleration log started", REPORT +"Vibration")


instruction("Slowly and constantly (2 min) accelerate to TO.")

note("Hold for 30 s and set the throttle stop.")

wait("N1_OBS="+str(round(getCV("N1TO"), 4)) , 150, 20, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 2.5min")

if SkipGV:
	result("Operator skipped TO point", REPORT +"Vib_Accel")

	pass
delay(5)

stop_log("Vibration")

stop_log("VSVVBV")


instruction("Record fullset")

do_fullset(1, "Vib Survey Accel","Vib_Survey_Acc")

delay(3)


result("Max #1 Brg Vibn = {} mils. N1 = {} rpm.".format(str(round(getFV("Vib1N1Pk"), 4)) , str(round(getFV("N1atV1MxA"), 4)) ), REPORT+"Vib_Accel")

result("Max TRF Flange Vibn = {} mils. N1 = {} rpm.".format(str(round(getFV("Vib2N1Pk"), 4)) , str(round(getFV("N1atV2MxA"), 4)) ), REPORT +"Vib_Accel")

result("Max #1 Brg Vibn = {} mils. N2 = {} rpm.".format(str(round(getFV("Vib1N2Pk"), 4)) , str(round(getFV("N2atV1MxA"), 4)) ), REPORT +"Vib_Accel")

result("Max TRF Vibn = {} mils. N2 = {} rpm.".format(str(round(getFV("Vib2N2Pk"), 4)) , str(round(getFV("N2atV2MxA"), 4)) ), REPORT +"Vib_Accel")



set_channel("Accel", 0)

start_log("Vibration", "VibDecel")

start_log("VSVVBV","Decel")

result("Vibration Deceleration log started", REPORT +"Vibration")




instruction("Slowly and constantly decelerate (2min) to GI stabilize for 4 min")

wait("GIFlag=1", 120, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at GI after 30s")

delay(5)

stop_log("Vibration")

stop_log("VSVVBV")


instruction("Record fullset")

do_fullset(1, "Vib Survey Deceleration ","Vib_Survey_Dec")

delay(50)

result("Vibration check - Deceleration", REPORT +"Vib_Decel")



result("Max #1 Brg Vibn = {} mils. N1 = {} rpm.".format(str(round(getFV("Vib1N1PkD"), 4)) , str(round(getFV("N1atV1MxD"), 4)) ), REPORT+"Vib_Decel")

result("Max TRF Flange Vibn = {} mils. N1 = {} rpm.".format(str(round(getFV("Vib2N1PkD"), 4)) , str(round(getFV("N1atV2MxD"), 4)) ), REPORT +"Vib_Decel")

result("Max #1 Brg Vibn = {} mils. N2 = {} rpm.".format(str(round(getFV("Vib1N2PkD"), 4)) , str(round(getFV("N2atV1MxD"), 4)) ), REPORT +"Vib_Decel")

result("Max TRF Vibn = {} mils. N2 = {} rpm.".format(str(round(getFV("Vib2N2PkD"), 4)) , str(round(getFV("N2atV2MxD"), 4)) ), REPORT +"Vib_Decel")


delay(240)



TestYes = prompt_boo("Is Test Vibration survey completed?")

if TestYes:
	result("Test Vibration survey completed and authorized.", REPORT + "Test6")

	pass

