import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 11VibrationSurvey.py
#******************************************************************************
#*  AUTHOR: John Tamplin
#*
#*  DESCRIPTION:72-00-00, TESTING 002, CFM56-5B Manual
#*  IDENTIFIER :Page
#*  Engine Vibration Survey during acceleration and deceleration
#*
#*  DATE: 1/10/2013 5:18:50 PM
#*
#*  MODIFICATIONS:
#*  REV    DATE       WHO  NCR    DESCRIPTION
#*
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
PerfStrYes = None

# Channel Registration
channel("GIFlag,VibReset,Accel,Vib1N1Pk,N1atV1MxA,Vib2N1Pk,N1atV2MxA,Vib1N2Pk,N2atV1MxA,Vib2N2Pk,N2atV2MxA,GetAccTrg,N1K,N1TO,ID,ID_N1TOMx")


set_channel("ID", getCV("ID_N1TOMx"))


caution("THE FAN MUST BE BALANCED FOR THIS TEST")


#*  reset Vibration Parameters at Acceleration
set_channel("VibReset", 1)

delay(2)

set_channel("VibReset", 0)

set_channel("Accel", 1)


start_log("Vibration", "VibAccel")

result("Vibration Acceleration log started {} Vibration ".format(REPORT))

instruction("Slowly and constantly accelerate to Take Off in 2 min, ")

note("hold it there for 30 s and set the throttle stop.")


wait("N1K = " + str(getCV("N1TO")) , 120, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 120 s")


if SkipGV:
	result("Operator skipped Take Off check {} Vib_Accel ".format(REPORT))

	pass

delay(5)

stop_log("Vibration")


instruction("Record fullset")

do_fullset(1, "Vib Survey Accel", "Vib_Survey_Acc")

delay(2)


set_channel("GetAccTrg", 1)


start_log("Vibration", "VibDecel")


result("Vibration Deceleration log started {} Vibration ".format(REPORT))


instruction("Slowly and constantly decelerate to Ground Idle")

note("in 2 minutes and stabilize for 5 minutes.")

wait("GIFlag = 1", 120, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Did not reach GI in 120 s")

delay(10)

stop_log("Vibration")


instruction("Record fullset")

do_fullset(1, "Vib Survey Deceleration ", "Vib_Survey_Dec")

delay(5)

result("Vibration check - Deceleration {} Vib_Decel ".format(REPORT))


result("Max #1 Brg Vibn = {} mils. N1 at #1 Brg Vibn = {} rpm. {} Vib_Accel ".format(getFV("Vib1N1Pk") , getFV("N1atV1MxA") , REPORT))

result("Max Turb Fr. Fwd Flange Vibn = {} mils. N1 at TFF Flange Vibn = {} rpm. {} Vib_Accel ".format(getFV("Vib2N1Pk") , getFV("N1atV2MxA") , REPORT))

result("Max #1 Brg Vibn = {} ips. N2 at #1 Brg Vibn = {} rpm. {} Vib_Accel ".format(getFV("Vib1N2Pk") , getFV("N2atV1MxA") , REPORT))

result("Max Turb Fr. Fwd Flange Vibn = {} ips. N2 at TFF Flange Vibn = {} rpm. {} Vib_Accel ".format(getFV("Vib2N2Pk") , getFV("N2atV2MxA") , REPORT))

delay(300)


PerfStrYes = prompt_boo("Do you want to start Performance Check?")


if PerfStrYes:
	autostart("98Performance_Multi.py")

	pass

