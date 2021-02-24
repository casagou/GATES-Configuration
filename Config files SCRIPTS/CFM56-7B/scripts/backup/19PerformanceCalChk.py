import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 14Performance.tps
#******************************************************************************
#*  AUTHOR: John Tamplin
#*
#*  DESCRIPTION:
#*  Performance Test
#*
#*  DATE: 1/18/2006 5:29:28 PM
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*    1/18/2006    IF   -----  Converted to proDAS script
#*    06/01/2006   JT          V1.00 Initial write (from 263)
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
OilConYes = None

# Channel Registration
channel("AIFlag,EGTHD,EGTHDLim_MC,EGTHDLim_TO,EGTHDM,EGTHDM_MC,EGTHDM_TO,EGTHDMMrg,EGTHDMMrg_MC,EGTHDMMrg_TO,EGTK3,EGTK3_MC,EGTK3_TO,Eng_On,FNK3,FNK3_MC,FNK3_TO,FNK3_TO,FNMrg_MC,FNMrg_TO,FNMrgPC,GIFlag,HoldFNK3,N1KRated_MC,N1KRated_TO,N1R,N1R_MC,N1R_TO,N1RMC,N1RTO,N2CC3,N2HD_MC,N2HD_TO,N2HDLim_TO,N2HDMrg,N2HDMrg_TO,N2K3,N2K3_MC,N2K3_TO,SFC_MC,SFC_TO,SFCK3,SFCMrg,SFCMrg_TO,SFCRef_TO,tAtGI,TO_Pnt,WFK3,WFK3_kgHr,WFK3_MC,WFK3_TO")

# test FF1,FF2,FNA,PCD,

#*  [lookup]
#*  channel=
#*  [validation]
#*  security=1
#*  modification="3017230253"
#*  [test script]
#*  name=Performance
#/ *
#*  /
#*  Performance
#*  Modification History
#*  Ver   Date        By  Description
#*  V1.00 06/01/2006 JT  Initial write (from 263)

#show_view "NPO_RTD2","View1", "Performance.v",0,0,10,10

set_channel("TO_Pnt", 0)


set_channel("HoldFNK3", 0)


instruction("Stabilize at Idle for 5 minutes")

# test wait "GIFlag = 1", 30, 0.1, , , , , , MSG, " Did not reach GI in 30 s "
# test wait "tAtGI > 300", 300, 2, , , , , , MSG, "Time at GI has not reached 300 s "
# vreal delay 300
instruction("Start No:4 bearing analysising test")

instruction("2.C.(9) Carefully and slowly accelerate to MAX CONT.")

note("Stabilize the engine for 10 min.")


set_channel("A27013", 1)

set_channel("AN1ActNoTrm", 97)

set_channel("AN2Act", 98)

set_channel("T2_1", 48)

set_channel("T2_2", 46)

set_channel("T2_3", 50)

set_channel("RH", 33)

set_channel("FNA", 26300)

set_channel("LHV", 18800)

set_channel("AT25Sel", 120)

set_channel("AT495Sel", 835)

set_channel("PCD", 14.4)

set_channel("Pambd", 0.1)

set_channel("PS2SIG_1", 12)

set_channel("APS3Sel", 480)

set_channel("AT3Sel", 550)

set_channel("PT17RHX", 23.5)

set_channel("PT17LHX", 23.6)

set_channel("FF1", 2000)

set_channel("FF2", 2100)

set_channel("PT495X", 65)

set_channel("SGsamp", 0.79)

set_channel("TSGsamp", 20)

set_channel("TF_fac", 26)


wait("N1R = " + str(round(getCV("N1R_MC"), 4)) , 120, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 120 s.")

#delay 470-Commented out TJ for TP Testing
delay(2)

do_fullset(10, "Perf Point: MC warmup", "MC_WarmUp")

#delay 120 -Commented out TJ for TP Testing
delay(2)


instruction("2.C.(11) Accelerate slowly to Take-Off.")

note("Stabilize the engine for 5 min.")

wait("N1R = " + str(round(getCV("N1R_TO"), 4)) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 s.")

#delay 290 - Commented out by TJ for testing
delay(2)

set_channel("HoldFNK3", 1)

delay(5)

do_fullset(10, "Perf Point: Take-Off", "Take_Off")

delay(5)


#*  V1.02 set_channel WFK3_TO = fv_WFK3
set_channel("WFK3_TO", round(getFV("WFK3_kgHr"), 4))

set_channel("SFC_TO", round(getFV("SFCK3"), 4))

set_channel("SFCMrg_TO", round(getFV("SFCMrg"), 4))

set_channel("N2HD_TO", round(getFV("N2CC3"), 4))

set_channel("N2HDMrg_TO", round(getFV("N2HDMrg"), 4))

set_channel("EGTHDMMrg_TO", round(getFV("EGTHDMMrg"), 4))

set_channel("EGTK3_TO", round(getFV("EGTK3"), 4))

set_channel("EGTHDM_TO", round(getFV("EGTHDM"), 4))

set_channel("FNK3_TO", round(getFV("FNK3"), 4))

set_channel("FNMrg_TO", round(getFV("FNMrgPC"), 4))

set_channel("N1RTO", round(getFV("N1R"), 4))

set_channel("N2K3_TO", round(getFV("N2K3"), 4))


set_channel("TO_Pnt", 1)

set_channel("HoldFNK3", 0)


instruction("2.C.(12) Decelerate to MAX CONT.")

note("Stabilize the engine for 5 min.")

wait("N1R = " + str(round(getCV("N1R_MC"), 4)) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 30 s.")

#delay 270 - Commented out by TJ for Testing

set_channel("HoldFNK3", 1)

delay(5)


do_fullset(10, "Perf Point: MAX CONT", "MAX_CONT")

delay(5)

#*  V1.02 set_channel WFK3_MC = fv_WFK3
set_channel("WFK3_MC", round(getFV("WFK3_kgHr"), 4))

set_channel("SFC_MC", round(getFV("SFCK3"), 4))

set_channel("N2HD_MC", round(getFV("N2CC3"), 4))

set_channel("EGTHDMMrg_MC", round(getFV("EGTHDMMrg"), 4))

set_channel("EGTK3_MC", round(getFV("EGTK3"), 4))

set_channel("EGTHDM_MC", round(getFV("EGTHDM"), 4))

set_channel("FNK3_MC", round(getFV("FNK3"), 4))

set_channel("FNMrg_MC", round(getFV("FNMrgPC"), 4))

set_channel("N1RMC", round(getFV("N1R"), 4))

set_channel("N2K3_MC", round(getFV("N2K3"), 4))


instruction("2.C.(13) Decelerate slowly to AI in 2 minutes.")

note("Stabilize the engine for 5 min.")

# test wait "AIFlag = 1", 120, 0.1, , , , , , SKIP, "Failed to reach AI in 120 s"
#delay 300 -Commented out TJ for TP Testing
delay(2)

do_fullset(10, "Perf Point: AI", "Perf_AI")


instruction("2.C.(14) Select MIN IDLE.")

note("Stabilize the engine for 5 min.")

# test wait "GIFlag = 1", 30, 0.1, , , , , , SKIP, "Failed to reach MIN. IDLE in 30 s"
# test wait "tAtGI > 180", 190, 2, , , , SKIP, "Engine wasn't at GI for 3 min"
do_fullset(10, "Perf Point: GI", "Perf_GI")

instruction("stop No:4 bearing analysising test")

OilConYes = prompt_boo("Do you want to complete Oil Consuption Check?")

if OilConYes == 1:
	auto_start("14OilConsumption")

	pass
