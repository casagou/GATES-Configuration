import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 98Performance_Multi.py
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:REFERANCE: CFM56-7B ENGINE MANUAL 72-00-00, TESTING 003,
#*  Performance Test - Multi-Derivative
#*
#*  DATE: 1/7/2021
#*
#*  MODIFICATIONS:
#*  REV    DATE         WHO  NCR    DESCRIPTION
#* 
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
OilConYes = None
Done = None
AutoStaYES = None
SkipAcc = None
TestYes = None
OilConsNow = None
SlamNow = None
Warmup = None

# Channel Registration
channel("Multiple,Eng_On,tAtGI,AIFlag,ID_N1MCMx,GIFlag,N1R,HoldFNK3,N1R_MC,N1R_TO,N1KRated_MC,WFK3_MC,SFC_MC,N2HD_MC,EGTHDLim_MC,EGTHDMMrg_MC,EGTK3_MC,EGTHDM_MC,FNK3_MC,FNMrg_MC,N1RMC,N2K3_MC,N1KRated_TO,WFK3_TO,SFC_TO,SFCRef_TO,SFCMrg_TO,N2HD_TO,N2HDLim_TO,N2HDMrg_TO,EGTHDLim_TO,EGTHDMMrg_TO,EGTK3_TO,EGTHDM_TO,FNK3_TO,FNMrg_TO,N1RTO,N2K3_TO,WFK3,SFCK3,SFCMrg,N2CC3,N2HDMrg,EGTHDMMrg,EGTK3,EGTHD,FNK3,FNMrgPC,N1R,N2K3,TO_Pnt,EGTHDM,WFK3_kgHr, WFK3_TO, SFC_TO, N2HD_TO, N2HDMrg_TO,FNK3_TO,FNMrg_TO, N1RTO,N2K3_TO, WFK3_MC, SFC_MC, N2HD_MC, TORange,N2HDMMrg_TO,N2HDMMrg,EGTHD_TO,EGTHD_MC,EGTHD,N1K,N1MC,N1TO,N1ModReset,ID_N1TOMx,N1MCWarmup,B27,B26,B24,B24B1,B22,B22B1,B20,B26B2,B22B2,ID,TOPoint,N1MCMx")


# show_view "SMES-RTD2","View1","Performance.v",0,0,1280,1024

#*************MULTI RATING SETUP*************************

if getCV("Multiple") == 1:

	if getCV("B27") == 1:
		set_channel("ID", 1)

	else:
		if getCV("B26") == 1:
			set_channel("ID", 2)

		else:
			if getCV("B24") == 1:
				set_channel("ID", 3)

			else:
				if getCV("B24B1") == 1:
					set_channel("ID", 4)

				else:
					if getCV("B22") == 1:
						set_channel("ID", 5)

					else:
						if getCV("B22B1") == 1:
							set_channel("ID", 6)

						else:
							if getCV("B20") == 1:
								set_channel("ID", 7)

							else:
								if getCV("B26B2") == 1:
									set_channel("ID", 8)
									pass
								pass
							pass
						pass
					pass
				pass
			pass
		pass
	pass

#*********N1 MOD LEVEL RESET*********************************
instruction("press NEXT to reset all previously recorded Take-Off Modifier Levels, or SKIP", SKIP)


if not skipgv:
	set_channel("N1ModReset", 1)

	delay(3)

	set_channel("N1ModReset", 0)

	pass

set_channel("TO_Pnt", 0)

set_channel("HoldFNK3", 0)

set_channel("TOPoint", 0)

#************TEST START********************************************
if gectCV("Eng_On") = 0:
    instruction("Start engine and Stabilize at Idle for 5 minutes")
    
    call_tps("04Start")

    wait("GIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Did not reach GI in 30 s ")

    pass
    

Warmup = prompt_boo("Has the engine been warmed up at MI for 5 minutes?")

if not

    instruction("Stabilize engine at MI for 5 minutes")
    
    wait("GIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Did not reach GI in 30 s ")
    
    wait("tAtGI > 300", 300, 2, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Time at GI has not reached 300 s ")
    pass
    

#*************OIL CONS & ACCEL CHECK*****************

OilConsNow = prompt_boo("Start oil consumption check?")

if 
    call_tps("14StartOilCons")
    pass
    
    
SlamNow = prompt_boo("Start Slam Acceleration check?")   

if
    call_tps("12Acceleration") 
    pass



set_channel("ID_N1MCMx",getCV("ID"))

result("N1 MC warmup target is: {} +\- 10 rpm ".format(getCV("N1MCWarmup")))

instruction("Warm up engine at MC power for 8 minutes.")

wait("N1K ="+str(getCV("N1MCWarmup")), 120, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 120 s.")

delay(300)

delay(180)

instruction("Record fullset")

do_fullset(10, "Perf Point: MC warmup for Derivative ID="&getCV("ID_N1TOMx"), "MC_WarmUp")


# --------------------- B27 ------------------------------------
instruction("Set power to B27 Take-off , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0
set_channel("TO_Pnt", 0)

if getCV("B27") == 1:
	if not skipgv:
		set_channel("ID", 1)

		set_channel("TOPoint", 1)

		delay(2)

		result("B27 TO N1 Target = {} +\- 10 rpm ".format(getCV("N1TO")))

		wait("N1K ="+ str(getCV("N1TO")) ,30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 s.")

		
		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(290)

		else:
			result("Operator skipped stable timer for B27 ")

			pass
		
		set_channel("HoldFNK3", 1)

		set_channel("TO_Pnt", 1)

		delay(5)

		instruction("Record fullset")

		do_fullset(10, "Perf Point: Take-Off", "Take_Off_B27")

		set_channel("TO_Pnt", 0)

		delay(5)

		
		set_channel("WFK3_TO", getFV("WFK3"))

		set_channel("SFC_TO", getFV("SFCK3"))

		set_channel("SFCMrg_TO", getFV("SFCMrg"))

		set_channel("N2HD_TO", getFV("N2CC3"))

		set_channel("N2HDMrg_TO", getFV("N2HDMrg"))

		set_channel("EGTHDMMrg_TO", getFV("EGTHDMMrg"))

		set_channel("N2HDMMrg_TO", getFV("N2HDMMrg"))

		set_channel("EGTK3_TO", getFV("EGTK3"))

		set_channel("EGTHDM_TO", getFV("EGTHDM"))

		set_channel("FNK3_TO", getFV("FNK3"))

		set_channel("FNMrg_TO", getFV("FNMrgPC"))

		set_channel("N1RTO", getFV("N1R"))

		set_channel("N2K3_TO", getFV("N2K3"))

		set_channel("EGTHD_TO", getFV("EGTHD"))

# capture N1ModLvlB27 by setting TO_Pnt to 1
# set_channel TO_Pnt, 1
# release held value of FNK3 (used for N1 Mod Level calc)
		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
	else:
		result("B27 TO Performance point was skipped by operator ")


		pass
else:
	result("B27 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# --------------------- B26B2 ------------------------------------
instruction("Set power to B26B2 Take-off , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0
set_channel("TO_Pnt", 0)

if getCV("B26B2") == 1:
	if not skipgv:
		set_channel("ID", 8)

		set_channel("TOPoint", 1)

		delay(2)

		result("B26B2 TO N1 Target = {} +\- 10 rpm ".format(getCV("N1TO")))

		wait("N1K ="+ str(getCV("N1TO")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 s.")

		
		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(290)

		else:
			result("Operator skipped stable timer for B26B2 ")

			pass
		
		set_channel("HoldFNK3", 1)


		set_channel("TO_Pnt", 1)

		delay(5)

		instruction("Record fullset")

		do_fullset(10, "Perf Point: Take-Off", "Take_Off_B26B2")


		set_channel("TO_Pnt", 0)

		delay(5)

		
		set_channel("WFK3_TO", getFV("WFK3"))

		set_channel("SFC_TO", getFV("SFCK3"))

		set_channel("SFCMrg_TO", getFV("SFCMrg"))

		set_channel("N2HD_TO", getFV("N2CC3"))

		set_channel("N2HDMrg_TO", getFV("N2HDMrg"))

		set_channel("EGTHDMMrg_TO", getFV("EGTHDMMrg"))

		set_channel("N2HDMMrg_TO", getFV("N2HDMMrg"))

		set_channel("EGTK3_TO", getFV("EGTK3"))

		set_channel("EGTHDM_TO", getFV("EGTHDM"))

		set_channel("FNK3_TO", getFV("FNK3"))

		set_channel("FNMrg_TO", getFV("FNMrgPC"))

		set_channel("N1RTO", getFV("N1R"))

		set_channel("N2K3_TO", getFV("N2K3"))

		set_channel("EGTHD_TO", getFV("EGTHD"))

# capture N1ModLvlB26B2 by setting TO_Pnt to 1
# V1.04 set_channel TO_Pnt, 1
# release held value of FNK3 (used for N1 Mod Level calc)
		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
	else:
		result("B26B2 TO Performance point was skipped by operator ")

# End If - skip this power setting
		pass
else:
	result("B26B2 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# --------------------- B26 ------------------------------------
instruction("Set power to B26 Take-off , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0
set_channel("TO_Pnt", 0)

if getCV("B26") == 1:
	if not skipgv:
		set_channel("ID", 2)

		set_channel("TOPoint", 1)

		delay(2)

		result("B26 TO N1 Target = {} +\- 10 rpm ".format(getCV("N1TO") ))

		wait("N1K ="+ str(getCV("N1TO")), 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 s.")

		
		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(290)

		else:
			result("Operator skipped stable timer for B26 ")

			pass
		
		set_channel("HoldFNK3", 1)


		set_channel("TO_Pnt", 1)

		delay(5)

		instruction("Record fullset")

		do_fullset(10, "Perf Point: Take-Off", "Take_Off_B26")


		set_channel("TO_Pnt", 0)

		delay(5)

		
		set_channel("WFK3_TO", getFV("WFK3"))

		set_channel("SFC_TO", getFV("SFCK3"))

		set_channel("SFCMrg_TO", getFV("SFCMrg"))

		set_channel("N2HD_TO", getFV("N2CC3"))

		set_channel("N2HDMrg_TO", getFV("N2HDMrg"))

		set_channel("EGTHDMMrg_TO", getFV("EGTHDMMrg"))

		set_channel("N2HDMMrg_TO", getFV("N2HDMMrg"))

		set_channel("EGTK3_TO", getFV("EGTK3"))

		set_channel("EGTHDM_TO", getFV("EGTHDM"))

		set_channel("FNK3_TO", getFV("FNK3"))

		set_channel("FNMrg_TO", getFV("FNMrgPC"))

		set_channel("N1RTO", getFV("N1R"))

		set_channel("N2K3_TO", getFV("N2K3"))

		set_channel("EGTHD_TO", getFV("EGTHD"))

# capture N1ModLvlB26 by setting TO_Pnt to 1
# set_channel TO_Pnt, 1
# release held value of FNK3 (used for N1 Mod Level calc)
		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
	else:
		result("B26 TO Performance point was skipped by operator ")


		pass
else:
	result("B26 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# --------------------- B27MC ------------------------------------
instruction("Set power to B27 Max Con , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0

if getCV("B27") == 1:
	if not skipgv:
		set_channel("ID", 1)

		delay(2)

		result("B27 MC N1 Target = {} +\- 10 rpm ".format(getCV("N1MC")))

		wait("N1K = " + str(getCV("N1MC")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 30 s.")

		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(270)

		else:
			result("Operator skipped stable timer for B27 ")

			pass
		

		instruction("Record fullset")

		do_fullset(10, "Perf Point: MAX CONT", "MAX_CONT_B27")

		delay(5)

		set_channel("WFK3_MC", getFV("WFK3"))

		set_channel("SFC_MC", getFV("SFCK3"))

		set_channel("N2HD_MC", getFV("N2CC3"))

		set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

		set_channel("EGTK3_MC", getFV("EGTK3"))

		set_channel("EGTHDM_MC", getFV("EGTHDM"))

		set_channel("FNK3_MC", getFV("FNK3"))

		set_channel("FNMrg_MC", getFV("FNMrgPC"))

		set_channel("N1RMC", getFV("N1R"))

		set_channel("N2K3_MC", getFV("N2K3"))

		set_channel("EGTHD_MC", getFV("EGTHD"))

		
	else:
		result("B27 MC Performance point was skipped by operator ")

# End If - skip this power setting
		pass
else:
	result("B27 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# ------------------End B27 ------------------------------------
# --------------------- B26MC ------------------------------------
instruction("Set power to B26 Max Con , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0
# V1.04 set_channel TO_Pnt, 0
if getCV("B26") == 1:
	if not skipgv:
		set_channel("ID", 2)

		delay(2)

		result("B26 MC N1 Target = {} +\- 10 rpm ".format(getCV("N1MC")))

		wait("N1K = " + str(getCV("N1MC")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 30 s.")

		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(270)

		else:
			result("Operator skipped stable timer for B26 ")

			pass
		
# V1.00 set_channel HoldFNK3, 1
		instruction("Record fullset")

		do_fullset(10, "Perf Point: MAX CONT", "MAX_CONT_B26")

		delay(5)

		set_channel("WFK3_MC", getFV("WFK3"))

		set_channel("SFC_MC", getFV("SFCK3"))

		set_channel("N2HD_MC", getFV("N2CC3"))

		set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

		set_channel("EGTK3_MC", getFV("EGTK3"))

		set_channel("EGTHDM_MC", getFV("EGTHDM"))

		set_channel("FNK3_MC", getFV("FNK3"))

		set_channel("FNMrg_MC", getFV("FNMrgPC"))

		set_channel("N1RMC", getFV("N1R"))

		set_channel("N2K3_MC", getFV("N2K3"))

		set_channel("EGTHD_MC", getFV("EGTHD"))

		
	else:
		result("B26 MC Performance point was skipped by operator ")

		pass
else:
	result("B26 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# ------------------End B26 ------------------------------------
# --------------------- B24B1 ------------------------------------
instruction("Set power to B24B1 Take-off , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0
set_channel("TO_Pnt", 0)

if getCV("B24B1") == 1:
	if not skipgv:
		set_channel("ID", 4)

		set_channel("TOPoint", 1)

		delay(2)

		result("B24B1 TO N1 Target = {} +\- 10 rpm ".format(getCV("N1TO")))

		wait("N1K ="+ str(getCV("N1TO")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 s.")

		
		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(290)

		else:
			result("Operator skipped stable timer for B24B1 ")

			pass
		
		set_channel("HoldFNK3", 1)

		set_channel("TO_Pnt", 1)

		delay(5)

		instruction("Record fullset")

		do_fullset(10, "Perf Point: Take-Off", "Take_Off_B24B1")

		set_channel("TO_Pnt", 0)

		delay(5)

		
		set_channel("WFK3_TO", getFV("WFK3"))

		set_channel("SFC_TO", getFV("SFCK3"))

		set_channel("SFCMrg_TO", getFV("SFCMrg"))

		set_channel("N2HD_TO", getFV("N2CC3"))

		set_channel("N2HDMrg_TO", getFV("N2HDMrg"))

		set_channel("EGTHDMMrg_TO", getFV("EGTHDMMrg"))

		set_channel("N2HDMMrg_TO", getFV("N2HDMMrg"))

		set_channel("EGTK3_TO", getFV("EGTK3"))

		set_channel("EGTHDM_TO", getFV("EGTHDM"))

		set_channel("FNK3_TO", getFV("FNK3"))

		set_channel("FNMrg_TO", getFV("FNMrgPC"))

		set_channel("N1RTO", getFV("N1R"))

		set_channel("N2K3_TO", getFV("N2K3"))

		set_channel("EGTHD_TO", getFV("EGTHD"))

# capture N1ModLvlB24B1 by setting TO_Pnt to 1
# set_channel TO_Pnt, 1
# release held value of FNK3 (used for N1 Mod Level calc)
		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
	else:
		result("B24B1 TO Performance point was skipped by operator ")


		pass
else:
	result("B24B1 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# --------------------- B24 ------------------------------------
instruction("Set power to B24 Take-off , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0
set_channel("TO_Pnt", 0)

if getCV("B24") == 1:
	if not skipgv:
		set_channel("ID", 3)

		set_channel("TOPoint", 1)

		delay(2)

		result("B24 TO N1 Target = {} +\- 10 rpm ".format(getCV("N1TO")))

		wait("N1K ="+ str(getCV("N1TO")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 s.")

		
		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(290)

		else:
			result("Operator skipped stable timer for B24 ")

			pass
		
		set_channel("HoldFNK3", 1)

		set_channel("TO_Pnt", 1)

		delay(5)

		instruction("Record fullset")

		do_fullset(10, "Perf Point: Take-Off", "Take_Off_B24")

		set_channel("TO_Pnt", 0)

		delay(5)

		
		set_channel("WFK3_TO", getFV("WFK3"))

		set_channel("SFC_TO", getFV("SFCK3"))

		set_channel("SFCMrg_TO", getFV("SFCMrg"))

		set_channel("N2HD_TO", getFV("N2CC3"))

		set_channel("N2HDMrg_TO", getFV("N2HDMrg"))

		set_channel("EGTHDMMrg_TO", getFV("EGTHDMMrg"))

		set_channel("N2HDMMrg_TO", getFV("N2HDMMrg"))

		set_channel("EGTK3_TO", getFV("EGTK3"))

		set_channel("EGTHDM_TO", getFV("EGTHDM"))

		set_channel("FNK3_TO", getFV("FNK3"))

		set_channel("FNMrg_TO", getFV("FNMrgPC"))

		set_channel("N1RTO", getFV("N1R"))

		set_channel("N2K3_TO", getFV("N2K3"))

		set_channel("EGTHD_TO", getFV("EGTHD"))

# capture N1ModLvlB24 by setting TO_Pnt to 1
# set_channel TO_Pnt, 1
# release held value of FNK3 (used for N1 Mod Level calc)
		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
	else:
		result("B24 TO Performance point was skipped by operator ")

		pass
else:
	result("B24 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# --------------------- B26B2MC ------------------------------------
instruction("Set power to B26B2 Max Con , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0
# V1.04 set_channel TO_Pnt, 0
if getCV("B26B2") == 1:
	if not skipgv:
		set_channel("ID", 8)

		delay(2)

		result("B26B2 MC N1 Target = {} +\- 10 rpm ".format(getCV("N1MC") ))

		wait("N1K = " + str(getCV("N1MC")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 30 s.")

		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(270)

		else:
			result("Operator skipped stable timer for B26B2 ")

			pass
		

		instruction("Record fullset")

		do_fullset(10, "Perf Point: MAX CONT", "MAX_CONT_B26B2")

		delay(5)

		set_channel("WFK3_MC", getFV("WFK3"))

		set_channel("SFC_MC", getFV("SFCK3"))

		set_channel("N2HD_MC", getFV("N2CC3"))

		set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

		set_channel("EGTK3_MC", getFV("EGTK3"))

		set_channel("EGTHDM_MC", getFV("EGTHDM"))

		set_channel("FNK3_MC", getFV("FNK3"))

		set_channel("FNMrg_MC", getFV("FNMrgPC"))

		set_channel("N1RMC", getFV("N1R"))

		set_channel("N2K3_MC", getFV("N2K3"))

		set_channel("EGTHD_MC", getFV("EGTHD"))

		
	else:
		result("B26B2 MC Performance point was skipped by operator ")

		pass
else:
	result("B26B2 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# ------------------End B26B2 ------------------------------------
# --------------------- B24MC ------------------------------------
instruction("Set power to B24 Max Con , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0
# V1.04 set_channel TO_Pnt, 0
if getCV("B24") == 1:
	if not skipgv:
		set_channel("ID", 3)

		delay(2)

		result("B24 MC N1 Target = {} +\- 10 rpm ".format(getCV("N1MC") ))

		wait("N1K = " + str(getCV("N1MC")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 30 s.")

		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(270)

		else:
			result("Operator skipped stable timer for B24 ")

			pass
		
		instruction("Record fullset")

		do_fullset(10, "Perf Point: MAX CONT", "MAX_CONT_B24")

		delay(5)

		set_channel("WFK3_MC", getFV("WFK3"))

		set_channel("SFC_MC", getFV("SFCK3"))

		set_channel("N2HD_MC", getFV("N2CC3"))

		set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

		set_channel("EGTK3_MC", getFV("EGTK3"))

		set_channel("EGTHDM_MC", getFV("EGTHDM"))

		set_channel("FNK3_MC", getFV("FNK3"))

		set_channel("FNMrg_MC", getFV("FNMrgPC"))

		set_channel("N1RMC", getFV("N1R"))

		set_channel("N2K3_MC", getFV("N2K3"))

		set_channel("EGTHD_MC", getFV("EGTHD"))

		
	else:
		result("B24 MC Performance point was skipped by operator ")

		pass
else:
	result("B24 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# ------------------End B24 ------------------------------------
# --------------------- B24B1MC ------------------------------------
instruction("Set power to B24B1 Max Con , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0
# V1.04 set_channel TO_Pnt, 0
if getCV("B24B1") == 1:
	if not skipgv:
		set_channel("ID", 4)

		delay(2)

		result("B24B1 MC N1 Target = {} +\- 10 rpm ".format(getCV("N1MC")))

		wait("N1K = " + str(getCV("N1MC")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 30 s.")

		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(270)

		else:
			result("Operator skipped stable timer for B24B1 ")

			pass
		
		instruction("Record fullset")

		do_fullset(10, "Perf Point: MAX CONT", "MAX_CONT_B24B1")

		delay(5)

		set_channel("WFK3_MC", getFV("WFK3"))

		set_channel("SFC_MC", getFV("SFCK3"))

		set_channel("N2HD_MC", getFV("N2CC3"))

		set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

		set_channel("EGTK3_MC", getFV("EGTK3"))

		set_channel("EGTHDM_MC", getFV("EGTHDM"))

		set_channel("FNK3_MC", getFV("FNK3"))

		set_channel("FNMrg_MC", getFV("FNMrgPC"))

		set_channel("N1RMC", getFV("N1R"))

		set_channel("N2K3_MC", getFV("N2K3"))

		set_channel("EGTHD_MC", getFV("EGTHD"))

		
	else:
		result("B24B1 MC Performance point was skipped by operator ")

		pass
else:
	result("B24B1 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# ------------------End B24B1 ------------------------------------

# --------------------- B22B1 ------------------------------------
instruction("Set power to B22B1 Take-off , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0
set_channel("TO_Pnt", 0)

if getCV("B22B1") == 1:
	if not skipgv:
		set_channel("ID", 6)

		set_channel("TOPoint", 1)

		delay(2)

		result("B22B1 TO N1 Target = {} +\- 10 rpm ".format(getCV("N1TO")))

		wait("N1K ="+ str(getCV("N1TO")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 s.")

		
		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(290)

		else:
			result("Operator skipped stable timer for B22B1 ")

			pass
		
		set_channel("HoldFNK3", 1)

		set_channel("TO_Pnt", 1)

		delay(5)

		instruction("Record fullset")

		do_fullset(10, "Perf Point: Take-Off", "Take_Off_B22B1")

		set_channel("TO_Pnt", 0)

		delay(5)

		
		set_channel("WFK3_TO", getFV("WFK3"))

		set_channel("SFC_TO", getFV("SFCK3"))

		set_channel("SFCMrg_TO", getFV("SFCMrg"))

		set_channel("N2HD_TO", getFV("N2CC3"))

		set_channel("N2HDMrg_TO", getFV("N2HDMrg"))

		set_channel("EGTHDMMrg_TO", getFV("EGTHDMMrg"))

		set_channel("N2HDMMrg_TO", getFV("N2HDMMrg"))

		set_channel("EGTK3_TO", getFV("EGTK3"))

		set_channel("EGTHDM_TO", getFV("EGTHDM"))

		set_channel("FNK3_TO", getFV("FNK3"))

		set_channel("FNMrg_TO", getFV("FNMrgPC"))

		set_channel("N1RTO", getFV("N1R"))

		set_channel("N2K3_TO", getFV("N2K3"))

		set_channel("EGTHD_TO", getFV("EGTHD"))

# capture N1ModLvlB22B1 by setting TO_Pnt to 1
# set_channel TO_Pnt, 1
# release held value of FNK3 (used for N1 Mod Level calc)
		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
	else:
		result("B22B1 TO Performance point was skipped by operator ")

		pass
else:
	result("B22B1 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# --------------------- B22 ------------------------------------
instruction("Set power to B22 Take-off , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0
set_channel("TO_Pnt", 0)

if getCV("B22") == 1:
	if not skipgv:
		set_channel("ID", 5)

		set_channel("TOPoint", 1)

		delay(2)

		result("B22 TO N1 Target = {} +\- 10 rpm ".format(getCV("N1TO")))

		wait("N1K ="+ str(getCV("N1TO")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 s.")

		
		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(290)

		else:
			result("Operator skipped stable timer for B22 ")

			pass
		
		set_channel("HoldFNK3", 1)

		set_channel("TO_Pnt", 1)

		delay(5)

		instruction("Record fullset")

		do_fullset(10, "Perf Point: Take-Off", "Take_Off_B22")

		set_channel("TO_Pnt", 0)

		delay(5)

		
		set_channel("WFK3_TO", getFV("WFK3"))

		set_channel("SFC_TO", getFV("SFCK3"))

		set_channel("SFCMrg_TO", getFV("SFCMrg"))

		set_channel("N2HD_TO", getFV("N2CC3"))

		set_channel("N2HDMrg_TO", getFV("N2HDMrg"))

		set_channel("EGTHDMMrg_TO", getFV("EGTHDMMrg"))

		set_channel("N2HDMMrg_TO", getFV("N2HDMMrg"))

		set_channel("EGTK3_TO", getFV("EGTK3"))

		set_channel("EGTHDM_TO", getFV("EGTHDM"))

		set_channel("FNK3_TO", getFV("FNK3"))

		set_channel("FNMrg_TO", getFV("FNMrgPC"))

		set_channel("N1RTO", getFV("N1R"))

		set_channel("N2K3_TO", getFV("N2K3"))

		set_channel("EGTHD_TO", getFV("EGTHD"))

# capture N1ModLvlB22 by setting TO_Pnt to 1
# set_channel TO_Pnt, 1
# release held value of FNK3 (used for N1 Mod Level calc)
		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
	else:
		result("B22 TO Performance point was skipped by operator ")

		pass
else:
	result("B22 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass

# --------------------- B22B1MC ------------------------------------
instruction("Set power to B22B1 Max Con , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0
if getCV("B22B1") == 1:
	if not skipgv:
		set_channel("ID", 6)

		delay(2)

		result("B22B1 MC N1 Target = {} +\- 10 rpm ".format(getCV("N1MC")))

		wait("N1K = " + str(getCV("N1MC")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 30 s.")

		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(270)

		else:
			result("Operator skipped stable timer for B22B1 ")

			pass
		
		instruction("Record fullset")

		do_fullset(10, "Perf Point: MAX CONT", "MAX_CONT_B22B1")

		delay(5)

		set_channel("WFK3_MC", getFV("WFK3"))

		set_channel("SFC_MC", getFV("SFCK3"))

		set_channel("N2HD_MC", getFV("N2CC3"))

		set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

		set_channel("EGTK3_MC", getFV("EGTK3"))

		set_channel("EGTHDM_MC", getFV("EGTHDM"))

		set_channel("FNK3_MC", getFV("FNK3"))

		set_channel("FNMrg_MC", getFV("FNMrgPC"))

		set_channel("N1RMC", getFV("N1R"))

		set_channel("N2K3_MC", getFV("N2K3"))

		set_channel("EGTHD_MC", getFV("EGTHD"))

		
	else:
		result("B22B1 MC Performance point was skipped by operator ")

		pass
else:
	result("B22B1 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# ------------------End B22B1 ------------------------------------
# --------------------- B22MC ------------------------------------
instruction("Set power to B22 Max Con , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0

if getCV("B22") == 1:
	if not skipgv:
		set_channel("ID", 5)

		delay(2)

		result("B22 MC N1 Target = {} +\- 10 rpm ".format(getCV("N1MC")))

		wait("N1K = " + str(getCV("N1MC")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 30 s.")

		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(270)

		else:
			result("Operator skipped stable timer for B22 ")

			pass
		
		instruction("Record fullset")

		do_fullset(10, "Perf Point: MAX CONT", "MAX_CONT_B22")

		delay(5)

		set_channel("WFK3_MC", getFV("WFK3"))

		set_channel("SFC_MC", getFV("SFCK3"))

		set_channel("N2HD_MC", getFV("N2CC3"))

		set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

		set_channel("EGTK3_MC", getFV("EGTK3"))

		set_channel("EGTHDM_MC", getFV("EGTHDM"))

		set_channel("FNK3_MC", getFV("FNK3"))

		set_channel("FNMrg_MC", getFV("FNMrgPC"))

		set_channel("N1RMC", getFV("N1R"))

		set_channel("N2K3_MC", getFV("N2K3"))

		set_channel("EGTHD_MC", getFV("EGTHD"))

		
	else:
		result("B22 MC Performance point was skipped by operator ")

		pass
else:
	result("B22 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# ------------------End B22 ------------------------------------
# --------------------- B20 ------------------------------------
instruction("Set power to B20 Take-off , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0
set_channel("TO_Pnt", 0)

if getCV("B20") == 1:
	if not skipgv:
		set_channel("ID", 7)

		set_channel("TOPoint", 1)

		delay(2)

		result("B20 TO N1 Target = {} +\- 10 rpm ".format(getCV("N1TO")))

		wait("N1K ="+ str(getCV("N1TO")), 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 s.")

		
		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(290)

		else:
			result("Operator skipped stable timer for B20 ")

			pass
		
		set_channel("HoldFNK3", 1)

		set_channel("TO_Pnt", 1)

		delay(5)

		instruction("Record fullset")

		do_fullset(10, "Perf Point: Take-Off", "Take_Off_B20")

		set_channel("TO_Pnt", 0)

		delay(5)

		
		set_channel("WFK3_TO", getFV("WFK3"))

		set_channel("SFC_TO", getFV("SFCK3"))

		set_channel("SFCMrg_TO", getFV("SFCMrg"))

		set_channel("N2HD_TO", getFV("N2CC3"))

		set_channel("N2HDMrg_TO", getFV("N2HDMrg"))

		set_channel("EGTHDMMrg_TO", getFV("EGTHDMMrg"))

		set_channel("N2HDMMrg_TO", getFV("N2HDMMrg"))

		set_channel("EGTK3_TO", getFV("EGTK3"))

		set_channel("EGTHDM_TO", getFV("EGTHDM"))

		set_channel("FNK3_TO", getFV("FNK3"))

		set_channel("FNMrg_TO", getFV("FNMrgPC"))

		set_channel("N1RTO", getFV("N1R"))

		set_channel("N2K3_TO", getFV("N2K3"))

		set_channel("EGTHD_TO", getFV("EGTHD"))

# capture N1ModLvlB20 by setting TO_Pnt to 1
# set_channel TO_Pnt, 1
# release held value of FNK3 (used for N1 Mod Level calc)
		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
	else:
		result("B20 TO Performance point was skipped by operator ")

		pass
else:
	result("B20 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass

# --------------------- B20MC ------------------------------------
instruction("Set power to B20 Max Con , or press SKIP", SKIP)

# hold previous N1 Mod Level by setting TO_Pnt to 0

if getCV("B20") == 1:
	if not skipgv:
		set_channel("ID", 7)

		delay(2)

		result("B20 MC N1 Target = {} +\- 10 rpm ".format(getCV("N1MC")))

		wait("N1K = " + str(getCV("N1MC")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 30 s.")

		instruction("Stabilize for 5 minutes or press SKIP if already stable", SKIP)

		if not skipgv:
			delay(270)

		else:
			result("Operator skipped stable timer for B20 ")

			pass
		
		instruction("Record fullset")

		do_fullset(10, "Perf Point: MAX CONT", "MAX_CONT_B20")

		delay(5)

		set_channel("WFK3_MC", getFV("WFK3"))

		set_channel("SFC_MC", getFV("SFCK3"))

		set_channel("N2HD_MC", getFV("N2CC3"))

		set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

		set_channel("EGTK3_MC", getFV("EGTK3"))

		set_channel("EGTHDM_MC", getFV("EGTHDM"))

		set_channel("FNK3_MC", getFV("FNK3"))

		set_channel("FNMrg_MC", getFV("FNMrgPC"))

		set_channel("N1RMC", getFV("N1R"))

		set_channel("N2K3_MC", getFV("N2K3"))

		set_channel("EGTHD_MC", getFV("EGTHD"))

		
	else:
		result("B20 MC Performance point was skipped by operator ")

		pass
else:
	result("B20 Derivative was not enabled on the Test Info Page - cannot record this power setting ")

	pass
# ------------------End B20 ------------------------------------

instruction("Decelerate slowly to MI in 2 minutes.")

set_channel("FIFB", 0)

note("Stabilize the engine for 7 minutes at MI.")

wait("GIFlag = 1", 120, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, SKIP, "Failed to reach AI in 120 s")

delay(300)

delay(120)

instruction("Record fullset")

do_fullset(10, "Perf Point: GI", "Perf_GI")



OilConYes = prompt_boo("Do you want to complete Oil Consuption Check?")

if OilConYes:
	auto_start("15EndOilCons")

	pass
