import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 13Performance.tps
#******************************************************************************
#*  AUTHOR: John Tamplin
#*
#*  DESCRIPTION:REFERANCE: CFM56-7B ENGINE MANUAL 72-00-00, TESTING 003,
#*  Performance Test
#*
#*  DATE: 1/18/2006 5:29:28 PM
#*
#*  MODIFICATIONS:
#*  REV   DATE         WHO  NCR    DESCRIPTION
#*  1.12  03Mar13      MSk  ---    Updated file names in autostart and call_tp calls.
#*  1.11  14Oct09     DP   ----   Added set_channel for ID to solve problem of no Accel Target for Multi-Derivative configuration
#*  1.10  14/oct/2009  YL   ---    Rev 40
#*  1.09  27/Sep/2008  DP   ---    Added set TOPoint to set correct calculations (EGTHDLimit); Changed TO_Pnt control
#*  1.08  15/Apr/2008  DP   ---    Added recording of EGTHD_MC
#*  1.07  13/Dec/2006  SL   ---    no more showview
#*  1.06  19/Jun/2006  TS   ---    N1R_TO changed to N1TO
#*  1.05  19/Jun/2006  TS   ---    N1R_MC changed to N1MC
#*  1.04  18/06/2006   TS   ---    parameters removed
#*  1.03  09/06/2006   DP  Added TORange to allow calculations to determine which target is being set
#*  1.02  06/09/2006    TS   -----  instruction added
#*  1.01  01/18/2006    IF   -----  Converted to proDAS script
#*  1.00  06/01/2006   JT          V1.00 Initial write (from 263)
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
OilConYes = None

# Channel Registration
channel("Eng_On,tAtGI,AIFlag,GIFlag,N1R,HoldFNK3,N1R_MC,N1R_TO,N1KRated_MC,WFK3_MC,SFC_MC,N2HD_MC,EGTHDLim_MC,EGTHDMMrg_MC,EGTK3_MC,EGTHDM_MC,FNK3_MC,FNMrg_MC,N1RMC,N2K3_MC,N1KRated_TO,WFK3_TO,SFC_TO,SFCRef_TO,SFCMrg_TO,N2HD_TO,N2HDLim_TO,N2HDMrg_TO,EGTHDLim_TO,EGTHDMMrg_TO,EGTK3_TO,EGTHDM_TO,FNK3_TO,FNMrg_TO,N1RTO,N2K3_TO,WFK3,SFCK3,SFCMrg,N2CC3,N2HDMrg,EGTHDMMrg,EGTK3,EGTHD,FNK3,FNMrgPC,N1R,N2K3,TO_Pnt,EGTHDM,WFK3_kgHr, WFK3_TO, SFC_TO, N2HD_TO, N2HDMrg_TO,FNK3_TO,FNMrg_TO, N1RTO,N2K3_TO, WFK3_MC, SFC_MC, N2HD_MC, TORange,N2HDMMrg_TO,N2HDMMrg,EGTHD_TO,EGTHD_MC,EGTHD,N1S,N1MC,N1TO,TOPoint,ID,ID_N1TOMx,TransReset,GetAccTrg,Accel,TORange,AccelTime,OilConsSta,TOil_OCStr,AccTrg1,ID,ID_N1TOMx")



# V1.04 following parameters not in the channel editor
#N2HD,N2Mrg,N2Mrg_TO,EGTMrg,EGTMrg_MC,SFCMrg_MC,EGTMrg_TO

# 1.07
# show_view "SMES-RTD2","View1","Performance.v",0,0,1280,1024
# V1.11 added the following set_channel
set_channel("ID", round(getCV("ID_N1TOMx"), 4))


set_channel("TO_Pnt", 0)


set_channel("HoldFNK3", 0)


instruction("Start engine and Stabilize at Idle for 5 minutes")

wait("GIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Did not reach GI in 30 s ")

wait("tAtGI > 300", 300, 2, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Time at GI has not reached 300 s ")

delay(300)


call_tps("12Acceleration")


#instruction "Stabilize at MAX CONT then take fullset"

note("Stabilize the engine for 8 min.")

#* V1.05 wait "N1R ="&cv_N1R_MC, 120, 10, , , , , , MSG, "Engine not at MC in 120 s."
wait("N1S ="+str(round(getCV("N1MC"), 4)) , 120, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 120 s.")

delay(300)

delay(60)

#delay 2
#V1.09 added the following set_channel
set_channel("TOPoint", 0)

#'V1.03 following instruction added
instruction("Record fullset")

do_fullset(10, "Perf Point: MC warmup", "MC_WarmUp")

delay(120)

#delay 2

instruction("2.C.(11) Accelerate slowly to Take-Off.")

note("Stabilize the engine for 5 min.")

#V1.09 added the following set_channel
set_channel("TOPoint", 1)

#*V1.06 wait "N1R ="& cv_N1R_TO, 30, 10, , , , , , MSG, "Engine not at TO in 30 s."
wait("N1S ="+ str(round(getCV("N1TO"), 4)) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 s.")

delay(290)

#delay 2
set_channel("HoldFNK3", 1)

# V1.09 moved TO_Pnt set_channel to here
set_channel("TO_Pnt", 1)

delay(5)

#V1.03 following instruction added
instruction("Record fullset")

do_fullset(10, "Perf Point: Take-Off", "Take_Off")

delay(5)

#V1.09 added the following set_channel
set_channel("TO_Pnt", 0)


#*  V1.02 set_channel WFK3_TO = fv_WFK3
set_channel("WFK3_TO", round(getFV("WFK3"), 4))

set_channel("SFC_TO", round(getFV("SFCK3"), 4))

set_channel("SFCMrg_TO", round(getFV("SFCMrg"), 4))

#set_channel N2HD_TO, fv_N2HD
set_channel("N2HD_TO", round(getFV("N2CC3"), 4))

set_channel("N2HDMrg_TO", round(getFV("N2HDMrg"), 4))

set_channel("EGTHDMMrg_TO", round(getFV("EGTHDMMrg"), 4))

#set_channel N2Mrg_TO, fv_N2Mrg
#set_channel EGTMrg_TO, fv_EGTMrg
set_channel("EGTK3_TO", round(getFV("EGTK3"), 4))

set_channel("EGTHDM_TO", round(getFV("EGTHDM"), 4))

set_channel("FNK3_TO", round(getFV("FNK3"), 4))

set_channel("FNMrg_TO", round(getFV("FNMrgPC"), 4))

set_channel("N1RTO", round(getFV("N1R"), 4))

set_channel("N2K3_TO", round(getFV("N2K3"), 4))

set_channel("EGTHD_TO", round(getFV("EGTHD"), 4))

# V1.09 set_channel TO_Pnt, 1
set_channel("HoldFNK3", 0)

set_channel("N2HDMMrg_TO", round(getFV("N2HDMMrg"), 4))

#V1.09 added the following set_channel
set_channel("TOPoint", 0)


instruction("2.C.(12) Decelerate to MAX CONT.")

# V1.03 added the following set_channel
#set_channel TORange, 0
note("Stabilize the engine for 3 min.")

#* V1.05 wait "N1R = " & cv_N1R_MC, 30, 10, , , , , , MSG, "Engine not at MC in 30 s."
wait("N1S = " + str(round(getCV("N1MC"), 4)) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 30 s.")

delay(170)


# V1.09 this is not needed for MC set_channel HoldFNK3, 1
delay(5)

#V1.03 following instruction added
instruction("Record fullset")

do_fullset(10, "Perf Point: MAX CONT", "MAX_CONT")

delay(5)

#*  V1.02 set_channel WFK3_MC = fv_WFK3
set_channel("WFK3_MC", round(getFV("WFK3"), 4))

set_channel("SFC_MC", round(getFV("SFCK3"), 4))

#set_channel SFCMrg_MC, fv_SFCMrg
#set_channel N2HD_MC, fv_N2HD
set_channel("N2HD_MC", round(getFV("N2CC3"), 4))

set_channel("EGTHDMMrg_MC", round(getFV("EGTHDMMrg"), 4))

#set_channel EGTMrg_MC, fv_EGTMrg
set_channel("EGTK3_MC", round(getFV("EGTK3"), 4))

set_channel("EGTHDM_MC", round(getFV("EGTHDM"), 4))

set_channel("FNK3_MC", round(getFV("FNK3"), 4))

set_channel("FNMrg_MC", round(getFV("FNMrgPC"), 4))

set_channel("N1RMC", round(getFV("N1R"), 4))

set_channel("N2K3_MC", round(getFV("N2K3"), 4))

# V1.08 added the following set_channel
set_channel("EGTHD_MC", round(getFV("EGTHD"), 4))


instruction("2.C.(13) Decelerate slowly to AI in 2 minutes.")

note("Stabilize the engine for 5 min.")

wait("AIFlag = 1", 120, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, SKIP, "Failed to reach AI in 120 s")

delay(300)

#delay 2
#V1.03 following instruction added
instruction("Record fullset")

do_fullset(10, "Perf Point: AI", "Perf_AI")


instruction("2.C.(14) Select MIN IDLE.")

note("Stabilize the engine for 7 min.")

wait("GIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, SKIP, "Failed to reach MIN. IDLE in 30 s")

wait("tAtGI > 180", 190, 2, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "Engine wasn't at GI for 3 min")

#V1.03 following instruction added
delay(300)

delay(100)

instruction("Record fullset")

do_fullset(10, "Perf Point: GI", "Perf_GI")

delay(20)

OilConYes = prompt_boo("Do you want to complete Oil Consuption Check?")

if OilConYes:
	auto_start("14OilConsumption")

	pass
