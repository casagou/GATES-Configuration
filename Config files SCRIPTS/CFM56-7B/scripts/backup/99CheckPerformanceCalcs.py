import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 99CheckPerformanceCalcs.tps
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
channel("Eng_On,tAtGI,AIFlag,GIFlag,N1R,HoldFNK3,N1R_MC,N1R_TO,N1KRated_MC,WFK3_MC,SFC_MC,N2HD_MC,EGTHDLim_MC,EGTHDMMrg_MC,EGTK3_MC,EGTHDM_MC,FNK3_MC,FNMrg_MC,N1RMC,N2K3_MC,N1KRated_TO,WFK3_TO,SFC_TO,SFCRef_TO,SFCMrg_TO,N2HD_TO,N2HDLim_TO,N2HDMrg_TO,EGTHDLim_TO,EGTHDMMrg_TO,EGTK3_TO,EGTHDM_TO,FNK3_TO,FNMrg_TO,N1RTO,N2K3_TO,WFK3,SFCK3,SFCMrg,N2CC3,N2HDMrg,EGTHDMMrg,EGTK3,EGTHD,FNK3,FNMrgPC,N1R,N2K3,TO_Pnt,EGTHDM,WFK3_kgHr, WFK3_TO, SFC_TO, SFCMrg_TO, N2HD_TO, N2HDMrg_TO, EGTHDMMrg_TO, EGTK3_TO, FNK3_TO, FNMrg_TO, N1RTO,N2K3_TO, WFK3_MC, SFC_MC, N2HD_MC, AN1ActNoTrm, AN2Act, AT25Sel,APS3Sel,AT3Sel ,T2_1,T2_2,T2_3 , RH , FNA, LHV, PCD,Pambd,PS2SIG_1,PT17RHX,PT17LHX,FF1,FF2,PT495X,SGsamp,TSGsamp,TF_fac,AT495Sel,A27013,AP25")


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

instruction("2.C.(11) Accelerate slowly to Take-Off.")

note("Stabilize the engine for 5 min.")

set_channel("A27013", 1)

set_channel("AN1ActNoTrm", 94.0)

set_channel("AN2Act", 93.0)

set_channel("T2_1", -30)

set_channel("T2_2", -30)

set_channel("T2_3", -30)

set_channel("RH", 35)

set_channel("FNA", 27750)

set_channel("LHV", 18800)

set_channel("AT25Sel", 130)

set_channel("AT495Sel", 700)

set_channel("PCD", 15)

set_channel("Pambd", 0.1)

set_channel("PS2SIG_1", -2.6)

set_channel("APS3Sel", 487)

set_channel("AT3Sel", 555)

set_channel("PT17RHX", 23.2)

set_channel("PT17LHX", 23.3)

set_channel("FF1", 1400)

set_channel("FF2", 500)

set_channel("PT495X", 67)

set_channel("SGsamp", 0.79)

set_channel("TSGsamp", 20)

set_channel("TF_fac", 26)

set_channel("AP25", 45)


wait("N1R = " + str(round(getCV("N1R_TO"), 4)) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 s.")

#delay 290 - Commented out by TJ for testing
delay(2)

set_channel("HoldFNK3", 1)

delay(5)

instruction("store TO fullset")

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


set_channel("A27013", 1)

set_channel("AN1ActNoTrm", 90)

set_channel("AN2Act", 91.0)

set_channel("T2_1", -30)

set_channel("T2_2", -30)

set_channel("T2_3", -30)

set_channel("RH", 35)

set_channel("FNA", 26100)

set_channel("LHV", 18800)

set_channel("AT25Sel", 120)

set_channel("AT495Sel", 635)

set_channel("PCD", 15)

set_channel("Pambd", 0.1)

set_channel("PS2SIG_1", -2.5)

set_channel("APS3Sel", 480)

set_channel("AT3Sel", 550)

set_channel("PT17RHX", 23.5)

set_channel("PT17LHX", 23.6)

set_channel("FF1", 1550)

set_channel("FF2", 350)

set_channel("PT495X", 65)

set_channel("SGsamp", 0.79)

set_channel("TSGsamp", 20)

set_channel("TF_fac", 26)

set_channel("AP25", 40)


delay(5)


instruction("store MC fullset")

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


OilConYes = prompt_boo("Do you want to complete Oil Consuption Check?")

#If OilConYes = 1 Then
#	autostart "OilConsumption"
#End If
