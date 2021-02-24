import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 98Performance_Multi.py
#********************************************************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:REFERANCE: CFM56-5B ENGINE MANUAL 72-00-00, TESTING 003,
#*  Performance Test - Multi-Derivative
#*
#*  DATE: 12/10/2020 
#*
#*  MODIFICATIONS:
#*  REV    	DATE         	WHO  	NCR    DESCRIPTION
#*
#*  ----	--------	---	---	--------------------------------------------------------------------------
#*  
#*
#*******************************************************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
OilConYes = None
Done = None
AutoStaYES = None
HighPower = None
SkipAcc = None
TestYes = None
OilConsNow = None
B1N1mod = None
B2N1mod = None
B3N1mod = None
B5N1mod = None
B6N1mod = None
B9N1mod = None
SlamNow = None


# Channel Registration
channel("B1,B2,B3,B4,B5,B6,B7,B8,B9,EGTHD,EGTHD_MC,EGTHD_TO,EGTHDM,EGTHDM_MC,AIFlag,EGTHDM_TO,EGTHDMMrg,EGTHDMMrg_MC,EGTHDMMrg_TO,EGTK3_MC,EGTK3,EGTK3_TO,Eng_On,FNK3,FNK3_MC,FNK3_TO,FNMrg_MC,FNMrg_TO,FNMrgPC,N1ModLvl_Alt,GIFlag,HoldFNK3,ID,MultiDevTest,N1MC,N1MCB1,N1MCB2,N1MCB3,N1MCB4,N1MCB5,N1MCB6,N1MCB7,N1MCB8,N1MCB9,N1ModReset,N1K,N1R,N1RMC,N1RTO,N1TO,N1TO15,N1TOB1,N1TOB2,N1TOB3,N1TOB4,N1TOB5,N1TOB6,N1TOB7,N1TOB8,N1TOB9,N2CC3,N2HD_MC,N2HD_TO,N2HDMMrg,N2HDMMrg_TO,N2HDMrg,N2HDMrg_TO,N2K3,N2K3_MC,N2K3_TO,SFC_MC,SFC_TO,SFCK3,SFCMrg,SFCMrg_TO,tAcc1,tAtGI,TO_Pnt,TOPoint,TransReset,WFK3,WFK3_MC,WFK3_TO")


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
instruction("Start engine and Stabilize at Idle for 5 minutes")

wait("GIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Did not reach GI in 30 s ")

wait("tAtGI > 300", 300, 2, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Time at GI has not reached 300 s ")





#*  SEQUENCE# 2
if getCV("GIFlag") == 1:
	instruction("Stabilize at MIN IDLE for 5 min. ")

	wait("GIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Did not reach GI in 30 s ")

	delay(300)

	pass


#**************HIGH POWER CHECK*********************
HighPower = prompt_boo("Was the engine warmed up for five minutes at high power? ")


if not HighPower:
	instruction("Slowly accelerate (2 min) to Max Cont for 5 min.")

	wait("N1K ="+str(getCV("N1MC")) , 60, 5, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Did not reach Max Cont in 60 s ")

	delay(300)

	instruction("Slowly decelerate (30 sec) to GI and stabilize for 5 minutes. ")

	wait("GIFlag = 1", 80, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine did not reach GI in 80 s ")

	delay(300)

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


#********8 MIN WARMUP AT MC*********************************


instruction("Stabilize Engine at MC N1 Speed +\- 10 rpm for 8 minutes")

wait("N1K = "+str(getCV("N1MC")), 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B3 Max Cont rpm in 10 s.")

	
if skipgv:
		result("Operator skipped MC warm up point {} Performance MC Warmup ".format(REPORT))

		pass
	
delay(300)

delay(180)

do_fullset(10, "Perf Point: MC warmup","MC_WarmUp")

delay(5)

Done = 1
	


#*****************B3 TO RATING****************
if getCV("B3") == 1:

    set_channel("ID", 3)
	
	set_channel("TO_Pnt", 0)

	set_channel("TOPoint", 1)

	
	note("B3 TO perf point")

	instruction("Stabilize to B3 Take Off N1 rating +\- 10 rpm for 5 minutes")

	wait("N1K = "+str(getCV("N1TOB3")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B3 Take Off in 10 s.")

	
	if skipgv:
		result("Operator skipped B3 TO point {} Performance B3 TO ".format(REPORT))

		pass
	
	delay(270)

	set_channel("HoldFNK3", 1)


	delay(2)

	do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

	delay(3)

	if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
		set_channel("N1ModLvl_Alt", 0)

		pass
	if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
		set_channel("N1ModLvl_Alt", 1)

		pass
	if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
		set_channel("N1ModLvl_Alt", 2)

		pass
	if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
		set_channel("N1ModLvl_Alt", 3)

		pass
	if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
		set_channel("N1ModLvl_Alt", 4)

		pass
	if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
		set_channel("N1ModLvl_Alt", 5)

		pass
	if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
		set_channel("N1ModLvl_Alt", 6)

		pass
	if getFV("FNMrgPC") >= 4.4:
		set_channel("N1ModLvl_Alt", 7)

		pass
        
    B3N1mod = getCV("N1ModLvl_Alt")
    
	delay(5)


	set_channel("TO_Pnt", 1)

	

	if getCV("MultiDevTest") == 0:
		do_fullset(10, "Perf Point: TO B3 Derivative","Take_Off")

	else:
		do_fullset(10, "Perf Point: TO B3 Derivative","Take_Off_B3")

		pass


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

	
	set_channel("TO_Pnt", 1)

	set_channel("HoldFNK3", 0)

	set_channel("TOPoint", 0)

	
	Done = 1
	
	pass
    
    
#*****************B2 TO RATING****************
if getCV("B2") == 1:
	
	set_channel("ID", 2)

	
	if Done == 1:
		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		note("B2 TO perf point after B3")

		instruction("Stabilize to B2 Take Off N1 rating +\- 10 rpm for 4 minutes")

		wait("N1K = "+str(getCV("N1TOB2")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B2 Take Off in 10 s.")

		
		if skipgv:
			result("Operator skipped B2 TO point {} Performance B2 TO ".format(REPORT))

			pass
		
		delay(220)

		
		set_channel("HoldFNK3", 1)



		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)

			pass
        
        B2N1mod = getCV("N1ModLvl_Alt")        
        
		delay(5)


		set_channel("TO_Pnt", 1)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: TO B2 Derivative","Take_Off")

		else:
			do_fullset(10, "Perf Point: TO B2 Derivative","Take_Off_B2")

			pass

		
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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
	else:
		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		note("B2 TO perf point")

		instruction("Stabilize to B2 Take Off N1 rating +\- 10 rpm for 5 minutes")

		wait("N1K = "+str(getCV("N1TOB2")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B2 Take Off in 10 s.")

		
		if skipgv:
			result("Operator skipped B2 TO point {} Performance B2 TO ".format(REPORT))

			pass
		
		delay(270)

		
		set_channel("HoldFNK3", 1)


		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)
            
			pass
            
            
        B2N1mod = getCV("N1ModLvl_Alt")
            
		delay(5)


		set_channel("TO_Pnt", 1)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: TO B2 Derivative","Take_Off")

		else:
			do_fullset(10, "Perf Point: TO B2 Derivative","Take_Off_B2")

			pass

		
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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
		Done = 1
		
		pass
	
	pass


#*****************B1 TO RATING****************
if getCV("B1") == 1:
	
	set_channel("ID", 1)

	
	if Done == 1:
		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		note("B1 TO perf point after B3 or B2")

		instruction("Stabilize to B1 Take Off N1 rating +\- 10 rpm for 4 minutes")

		wait("N1K = "+str(getCV("N1TOB1")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B1 Take Off in 10 s.")

		
		if skipgv:
			result("Operator skipped B1 TO point {} Performance B1 TO ".format(REPORT))

			pass
		
		delay(220)

		
		set_channel("HoldFNK3", 1)


		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)

			pass
            
        B1N1mod = getCV("N1ModLvl_Alt")
        
        
		delay(5)


		set_channel("TO_Pnt", 1)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: TO B1 Derivative","Take_Off")

		else:
			do_fullset(10, "Perf Point: TO B1 Derivative","Take_Off_B1")

			pass

		
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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
	else:
		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		note("B1 TO Perf Point")

		instruction("Stabilize to B1 Take Off N1 rating  +\- 10 rpm for 5 minutes")

		wait("N1K = "+str(getCV("N1TOB1")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B1 Take Off in 10 s.")

		
		if skipgv:
			result("Operator skipped B2 TO point {} Performance B1 TO ".format(REPORT))

			pass
		
		delay(270)

		
		set_channel("HoldFNK3", 1)


		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)

			pass
            
        B1N1mod = getCV("N1ModLvl_Alt")
        
		delay(5)


		set_channel("TO_Pnt", 1)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: TO B1 Derivative","Take_Off")

		else:
			do_fullset(10, "Perf Point: TO B1 Derivative","Take_Off_B1")

			pass

		
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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
		Done = 1
		
		pass
	
	pass


#*****************B1 B2 B3 MC RATINGS****************
if getCV("B3") == 1 or getCV("B2") == 1 or getCV("B1") == 1:
	
	note("B3 B2 B1 MC perf point")

	instruction("Stabilize to B3\B2\B1 Max Cont N1 rating +\- 10 rpm for 4 minutes")

	wait("N1K = "+str(getCV("N1MCB1")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B3\B2\B1 Max Cont in 10 s.")

	
	if skipgv:
		result("Operator skipped B1 MC point {} Performance B3 B2 B1 MC ".format(REPORT))

		pass
	
	delay(240)

	

	if getCV("MultiDevTest") == 0:
		do_fullset(10, "Perf Point: MC","MAX_CONT")

	else:
		if getCV("B3") == 1:
        
            set_channel("N1ModLvl_Alt",B3N1mod)  
			do_fullset(10, "Perf Point: MC B3 Derivative","MAX_CONT_B3")

			pass
		
		if getCV("B2") == 1:
        
            set_channel("N1ModLvl_Alt",B2N1mod) 
			do_fullset(10, "Perf Point: MC B2 Derivative","MAX_CONT_B2")

			pass
		
		if getCV("B1") == 1:
        
            set_channel("N1ModLvl_Alt",B1N1mod) 
			do_fullset(10, "Perf Point: MC B1 Derivative","MAX_CONT_B1")

			pass
		pass


	delay(5)

	set_channel("WFK3_MC", getFV("WFK3"))

	set_channel("SFC_MC", getFV("SFCK3"))

	set_channel("N2HD_MC", getFV("N2CC3"))

	set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

	set_channel("EGTK3_MC", getFV("EGTK3"))

	set_channel("EGTHDM_MC", getFV("EGTHDM"))

	set_channel("FNK3_MC", getFV("FNK3"))

	set_channel("FNMrg_MC", getFV("FNMrgPC"))

	set_channel("N1RMC", getFV("N1K"))

	set_channel("N2K3_MC", getFV("N2K3"))

	set_channel("EGTHD_MC", getFV("EGTHD"))

	Done = 1
	
	pass

#*****************B4 & B7 RATING****************
if getCV("B4") == 1 or getCV("B7") == 1:
	
	set_channel("ID", 4)

	
	if Done == 1:
		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		note("B4 and B7 TO perf point after other perf point")

		instruction("Stabilize to B4\B7 Take Off N1 rating +\- 10 rpm for 4 minutes")

		wait("N1K = "+str(getCV("N1TOB4")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B4\B7 Take Off in 10 s.")

		
		if skipgv:
			result("Operator skipped B4 TO point {} Performance B4 B7 TO ".format(REPORT))

			pass
		
		delay(220)

		
		set_channel("HoldFNK3", 1)


		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)

			pass
		delay(5)


		set_channel("TO_Pnt", 1)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: Take Off","Take_Off")

		else:
			if getCV("B4") == 1:
				
				do_fullset(10, "Perf Point: Take Off B4 Derivative","Take_Off_B4")

				pass
			
			if getCV("B7") == 1:
				do_fullset(10, "Perf Point: Take Off B7 Derivative","Take_Off_B7")

				pass
			pass

		
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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
		instruction("Stabilize to B4\B7 Max Cont N1 rating +\- 10 rpm for 4 minutes")

		wait("N1K = "+str(getCV("N1MCB4")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B4\B7 Max Cont in 10 s.")

		
		if skipgv:
			result("Operator skipped B4 MC point {} Performance B4 B7 MC ".format(REPORT))

			pass
		
		delay(240)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: MAX_CONT","MAX_CONT")

		else:
			if getCV("B4") == 1:
				do_fullset(10, "Perf Point: MC B4 Derivative","MAX_CONT_B4")

				pass
			
			if getCV("B7") == 1:
				do_fullset(10, "Perf Point: MC B7 Derivative","MAX_CONT_B7")

				pass
			pass

		
		delay(5)

		set_channel("WFK3_MC", getFV("WFK3"))

		set_channel("SFC_MC", getFV("SFCK3"))

		set_channel("N2HD_MC", getFV("N2CC3"))

		set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

		set_channel("EGTK3_MC", getFV("EGTK3"))

		set_channel("EGTHDM_MC", getFV("EGTHDM"))

		set_channel("FNK3_MC", getFV("FNK3"))

		set_channel("FNMrg_MC", getFV("FNMrgPC"))

		set_channel("N1RMC", getFV("N1K"))

		set_channel("N2K3_MC", getFV("N2K3"))

		set_channel("EGTHD_MC", getFV("EGTHD"))

		
	else:
		
		note("B4 and B7 MC perf points")

		instruction("Stabilize to B4\B7 Max Cont N1 rating +\- 10 rpm for 10 minutes")

		wait("N1K = "+str(getCV("N1MCB4")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B4 Max Cont in 10 s.")

		
		if skipgv:
			result("Operator skipped B4 MC point {} Performance B4 B7 MC Warmup ".format(REPORT))

			pass
		
		delay(300)

		delay(300)

		
		do_fullset(10, "Perf Point: MC B4 Derivative","MC_WarmUp")

		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		note("B4 B7 TO perf Point")

		instruction("Stabilize to B4\B7 Take Off N1 rating +\- 10 rpm for 5 minutes")

		wait("N1K = "+str(getCV("N1TOB4")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B4\B7 Take Off in 10 s.")

		
		if skipgv:
			result("Operator skipped B4 TO point {} Performance B4 B7 TO ".format(REPORT))

			pass
		
		delay(270)

		
		set_channel("HoldFNK3", 1)


		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)

			pass
		delay(5)


		set_channel("TO_Pnt", 1)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: Take Off","Take_Off")

		else:
			if getCV("B4") == 1:
				do_fullset(10, "Perf Point: Take Off B4 Derivative","Take_Off_B4")

				pass
			
			if getCV("B7") == 1:
				do_fullset(10, "Perf Point: Take Off B7 Derivative","Take_Off_B7")

				pass
			pass


		
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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
		instruction("Stabilize to B4\B7 Max Cont N1 rating +\- 10 rpm for 4 minutes")

		wait("N1K = "+str(getCV("N1MCB4")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B4\B7 Max Cont in 10 s.")

		
		if skipgv:
			result("Operator skipped B4 MC point {} Performance B4 B7 MC ".format(REPORT))

			pass
		
		note("B4 B7 MC Perf point")

		delay(240)

		
		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: MAX_CONT","MAX_CONT")

		else:
			if getCV("B4") == 1:
				do_fullset(10, "Perf Point: MC B4 Derivative","MAX_CONT_B4")

				pass
			
			if getCV("B7") == 1:
				do_fullset(10, "Perf Point: MC B7 Derivative","MAX_CONT_B7")

				pass
			pass

		
		delay(5)

		set_channel("WFK3_MC", getFV("WFK3"))

		set_channel("SFC_MC", getFV("SFCK3"))

		set_channel("N2HD_MC", getFV("N2CC3"))

		set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

		set_channel("EGTK3_MC", getFV("EGTK3"))

		set_channel("EGTHDM_MC", getFV("EGTHDM"))

		set_channel("FNK3_MC", getFV("FNK3"))

		set_channel("FNMrg_MC", getFV("FNMrgPC"))

		set_channel("N1RMC", getFV("N1K"))

		set_channel("N2K3_MC", getFV("N2K3"))

		set_channel("EGTHD_MC", getFV("EGTHD"))

		Done = 1
		
		pass
	
	pass

#*****************B6 TO RATING****************
if getCV("B6") == 1:
	
	set_channel("ID", 6)

	
	if Done == 1:
		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		note("B6 TO perf point after other Perf")

		instruction("Stabilize to B6 Take Off N1 rating +\-10 rpm for 4 minutes")

		wait("N1K = "+str(getCV("N1TOB6")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B6 Take Off in 10 s.")

		
		if skipgv:
			result("Operator skipped B4 TO point {} Performance B6 TO ".format(REPORT))

			pass
		
		delay(220)

		
		set_channel("HoldFNK3", 1)


		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)

			pass
            
        B6N1mod = getCV("N1ModLvl_Alt")   
            
		delay(5)


		set_channel("TO_Pnt", 1)

		
		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: Take Off","Take_Off")

		else:
			do_fullset(10, "Perf Point: TO B6 Derivative","Take_Off_B6")

			pass

		
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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
	else:
		
		note("B6 MC Perf point")

		instruction("Stabilize to B6 Max Cont N1 rating +\- 10 rpm for 10 minutes")

		wait("N1K = "+str(getCV("N1MCB6")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B6 Max Cont in 10 s.")

		
		if skipgv:
			result("Operator skipped B6 MC point {} Performance B6 MC Warmup ".format(REPORT))

			pass
		
		delay(300)

		delay(300)

		do_fullset(10, "Perf Point: MC B6 Derivative","MC_WarmUp")

		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		instruction("Stabilize to B6 Take Off N1 rating +\- 10 rpm for 5 minutes")

		wait("N1K = "+str(getCV("N1TOB6")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B6 Take Off in 10 s.")

		
		if skipgv:
			result("Operator skipped B4 TO point {} Performance B6 TO ".format(REPORT))

			pass
		
		note("TO B6 Perf Point")

		delay(270)

		
		set_channel("HoldFNK3", 1)


		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)

			pass
		delay(5)


		set_channel("TO_Pnt", 1)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: Take Off","Take_Off")

		else:
			do_fullset(10, "Perf Point: TO B6 Derivative","Take_Off_B6")

			pass

		
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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
		Done = 1
		
		pass
	
	pass

#*****************B9 RATING****************
if getCV("B9") == 1:
	
	set_channel("ID", 9)

	
	if Done == 1:
		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		note("B9 TO perf point after other Perf")

		instruction("Stabilize to B9 Take Off Ni rating +\- 10 rpm for 4 minutes")

		wait("N1K = "+str(getCV("N1TOB9")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B9 Take Off in 10 s.")

		if skipgv:
			result("Operator skipped B9 TO point {} Performance B9 TO ".format(REPORT))

			pass
		delay(220)

		
		set_channel("HoldFNK3", 1)


		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)

			pass
        
        B9N1mod = getCV("N1ModLvl_Alt")        
        
		delay(5)


		set_channel("TO_Pnt", 1)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: Take Off","Take_Off")

		else:
			do_fullset(10, "Perf Point: TO B9 Derivative","Take_Off_B9")

			pass


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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
	else:
		
		note("B9 MC Perf point")

		instruction("Stabilize to B9 Max Cont N1 rating +\- 10 rpm for 10 minutes")

		wait("N1K = "+str(getCV("N1MCB9")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B Max Cont in 10 s.")

		
		if skipgv:
			result("Operator skipped B9 MC point {} Performance B9 MC warmup ".format(REPORT))

			pass
		
		delay(300)

		delay(300)

		do_fullset(10, "Perf Point: MC B9 Derivative","MC_WarmUp")

		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		instruction("Stabilize to B9 Take Off N1 rating +\- 10 rpm for 5 minutes")

		wait("N1K = "+str(getCV("N1TOB9")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B9 Take Off in 10 s.")

		
		if skipgv:
			result("Operator skipped B9 TO point {} Performance B9 TO ".format(REPORT))

			pass
		
		note("TO B9 Perf Point")

		delay(270)

		
		set_channel("HoldFNK3", 1)


		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)

			pass
		delay(5)


		set_channel("TO_Pnt", 1)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: Take Off","Take_Off")

		else:
			do_fullset(10, "Perf Point: TO B9 Derivative","Take_Off_B9")

			pass

		
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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
		Done = 1
		
		pass
	
	pass


#*****************B5 RATING****************
if getCV("B5") == 1:
	
	set_channel("ID", 5)

	
	if Done == 1:
		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		note("B5 TO perf point after other Perf")

		instruction("Stabilize to B5 Take Off N1 rating +\- 10 rpm for 4 minutes")

		wait("N1K = "+str(getCV("N1TOB5")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B5 Take Off in 10 s.")

		
		if skipgv:
			result("Operator skipped B5 TO point {} Performance B5 TO ".format(REPORT))

			pass
		
		delay(220)

		
		set_channel("HoldFNK3", 1)


		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)

			pass
        
        B5N1mod = getCV("N1ModLvl_Alt")        
        
		delay(5)


		set_channel("TO_Pnt", 1)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: Take Off","Take_Off")

		else:
			do_fullset(10, "Perf Point: TO B5 Derivative","Take_Off_B5")

			pass


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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
	else:
		
		note("B5 MC Perf point")

		instruction("Stabilize to B5 Max Cont N1 rating +\- 10 rpm for 10 minutes")

		wait("N1K = "+str(getCV("N1MCB5")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B5 Max Cont in 10 s.")

		
		if skipgv:
			result("Operator skipped B5 MC point {} Performance B5 MC Warmup ".format(REPORT))

			pass
		
		delay(300)

		delay(300)

		do_fullset(10, "Perf Point: MC B5 Derivative","MC_WarmUp")

		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		instruction("Stabilize to B5 Take Off N1 rating +\- 10 rpm for 5 minutes")

		wait("N1K = "+str(getCV("N1TOB5")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B5 Take Off in 10 s.")

		
		if skipgv:
			result("Operator skipped B5 TO point {} Performance B5 TO ".format(REPORT))

			pass
		
		note("TO B5 Perf Point")

		delay(270)

		
		set_channel("HoldFNK3", 1)


		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)

			pass
		delay(5)


		set_channel("TO_Pnt", 1)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: Take Off","Take_Off")

		else:
			do_fullset(10, "Perf Point: TO B5 Derivative","Take_Off_B5")

			pass

		
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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
		Done = 1
		
		pass
	
	pass

#*****************B5 B6 B9 MC RATING****************
if getCV("B6") == 1 or getCV("B9") == 1 or getCV("B5") == 1:
	
	note("B6 B9 B5 MC Perf point")

	instruction("Stabilize to B5\B6\B9 Max Cont N1 rating +\- 10 rpm for 4 minutes")

	wait("N1K = "+str(getCV("N1MCB6")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B5\B6\B9 Max Cont in 10 s.")

	
	if skipgv:
		result("Operator skipped B6 MC point {} Performance B6 B9 B5 MC ".format(REPORT))

		pass
	
	delay(240)

	

	if getCV("MultiDevTest") == 0:
		do_fullset(10, "Perf Point: MC","MAX_CONT")

	else:
		if getCV("B6") == 1:
            set_channel("N1ModLvl_Alt",B6N1mod)  
			do_fullset(10, "Perf Point: MC B6 Derivative","MAX_CONT_B6")

			pass
            
            		
		if getCV("B9") == 1:
            set_channel("N1ModLvl_Alt",B9N1mod)
			do_fullset(10, "Perf Point: MC B9 Derivative","MAX_CONT_B9")

			pass
		
		if getCV("B5") == 1:
            set_channel("N1ModLvl_Alt",B5N1mod)
			do_fullset(10, "Perf Point: MC B5 Derivative","MAX_CONT_B5")

			pass
		pass

	
	delay(5)

	set_channel("WFK3_MC", getFV("WFK3"))

	set_channel("SFC_MC", getFV("SFCK3"))

	set_channel("N2HD_MC", getFV("N2CC3"))

	set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

	set_channel("EGTK3_MC", getFV("EGTK3"))

	set_channel("EGTHDM_MC", getFV("EGTHDM"))

	set_channel("FNK3_MC", getFV("FNK3"))

	set_channel("FNMrg_MC", getFV("FNMrgPC"))

	set_channel("N1RMC", getFV("N1K"))

	set_channel("N2K3_MC", getFV("N2K3"))

	set_channel("EGTHD_MC", getFV("EGTHD"))

	Done = 1
	
	pass

#***************B8 RATING****************
if getCV("B8") == 1:
	
	set_channel("ID", 8)

	
	if Done == 1:
		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		note("B8 TO perf point after other Perf")

		instruction("Stabilize to B8 Take Off N1 rating +\- 10 rpm for 4 minutes")

		wait("N1K = "+str(getCV("N1TOB8")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B8 Take Off in 10 s.")

		
		if skipgv:
			result("Operator skipped B8 TO point {} Performance B8 TO ".format(REPORT))

			pass
		
		delay(220)

		
		set_channel("HoldFNK3", 1)


		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)

			pass
		delay(5)


		set_channel("TO_Pnt", 1)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: Take Off","Take_Off")

		else:
			do_fullset(10, "Perf Point: TO B8 Derivative","Take_Off_B8")

			pass

		
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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
		instruction("Stabilize to B8 Max Cont N1 rating +\- 10 rpm for 4 minutes")

		wait("N1K = "+str(getCV("N1MCB8")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B8 Max Cont in 10 s.")

		
		if skipgv:
			result("Operator skipped B8 MC point {} Performance B8 MC ".format(REPORT))

			pass
		
		note("B8 Mc perf point after other Perf")

		delay(240)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: MAX CONT","MAX_CONT")

		else:
			do_fullset(10, "Perf Point: MC B8 Derivative","MAX_CONT_B8")

			pass

		
		delay(5)

		set_channel("WFK3_MC", getFV("WFK3"))

		set_channel("SFC_MC", getFV("SFCK3"))

		set_channel("N2HD_MC", getFV("N2CC3"))

		set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

		set_channel("EGTK3_MC", getFV("EGTK3"))

		set_channel("EGTHDM_MC", getFV("EGTHDM"))

		set_channel("FNK3_MC", getFV("FNK3"))

		set_channel("FNMrg_MC", getFV("FNMrgPC"))

		set_channel("N1RMC", getFV("N1K"))

		set_channel("N2K3_MC", getFV("N2K3"))

		set_channel("EGTHD_MC", getFV("EGTHD"))

		
	else:
		
		note("B8 MC perf point")

		instruction("Stabilize to B8 Max Cont N1 rating +\- 10 rpm for 10 minutes")

		wait("N1K = "+str(getCV("N1MCB8")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B8 Max Cont in 10 s.")

		
		if skipgv:
			result("Operator skipped B8 MC point {} Performance B8 MC Warmup ".format(REPORT))

			pass
		
		delay(300)

		delay(300)

		do_fullset(10, "Perf Point: MC B8 Derivative","MC_WarmUp")

		
		set_channel("TO_Pnt", 0)

		set_channel("TOPoint", 1)

		
		instruction("Stabilize to B8 Take Off N1 rating +\- 10 rpm for 5 minutes")

		wait("N1K = "+str(getCV("N1TOB8")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B8 Take Off in 10 s.")

		
		if skipgv:
			result("Operator skipped B8 TO point {} Performance B8 TO ".format(REPORT))

			pass
		
		note("B8 TO perf point")

		delay(270)

		
		set_channel("HoldFNK3", 1)


		delay(2)

		do_fullset(10, "Perf Point: N1 Modidier", "N1_Modifier")

		delay(3)

		if getFV("FNMrgPC") >= 0 and getFV("FNMrgPC") < 1.4:
			set_channel("N1ModLvl_Alt", 0)

			pass
		if getFV("FNMrgPC") >= 1.4 and getFV("FNMrgPC") < 1.8:
			set_channel("N1ModLvl_Alt", 1)

			pass
		if getFV("FNMrgPC") >= 1.8 and getFV("FNMrgPC") < 2.2:
			set_channel("N1ModLvl_Alt", 2)

			pass
		if getFV("FNMrgPC") >= 2.2 and getFV("FNMrgPC") < 2.6:
			set_channel("N1ModLvl_Alt", 3)

			pass
		if getFV("FNMrgPC") >= 2.6 and getFV("FNMrgPC") < 3.0:
			set_channel("N1ModLvl_Alt", 4)

			pass
		if getFV("FNMrgPC") >= 3.0 and getFV("FNMrgPC") < 3.6:
			set_channel("N1ModLvl_Alt", 5)

			pass
		if getFV("FNMrgPC") >= 3.6 and getFV("FNMrgPC") < 4.4:
			set_channel("N1ModLvl_Alt", 6)

			pass
		if getFV("FNMrgPC") >= 4.4:
			set_channel("N1ModLvl_Alt", 7)

			pass
		delay(5)


		set_channel("TO_Pnt", 1)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: Take Off","Take_Off")

		else:
			do_fullset(10, "Perf Point: TO B8 Derivative","Take_Off_B8")

			pass

		
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

		
		set_channel("TO_Pnt", 1)

		set_channel("HoldFNK3", 0)

		set_channel("TOPoint", 0)

		
		instruction("Stabilize to B8 Max Cont N1 rating +\- 10 rpm for 4 minutes")

		wait("N1K = "+str(getCV("N1MCB8")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B8 Max Cont in 10 s.")

		
		if skipgv:
			result("Operator skipped B8 MC point {} Performance B8 MC ".format(REPORT))

			pass
		
		note("B8 MC perf point")

		delay(240)

		

		if getCV("MultiDevTest") == 0:
			do_fullset(10, "Perf Point: MAX CONT","MAX_CONT")

		else:
			do_fullset(10, "Perf Point: MC B8 Derivative","MAX_CONT_B8")

			pass

		
		delay(5)

		set_channel("WFK3_MC", getFV("WFK3"))

		set_channel("SFC_MC", getFV("SFCK3"))

		set_channel("N2HD_MC", getFV("N2CC3"))

		set_channel("EGTHDMMrg_MC", getFV("EGTHDMMrg"))

		set_channel("EGTK3_MC", getFV("EGTK3"))

		set_channel("EGTHDM_MC", getFV("EGTHDM"))

		set_channel("FNK3_MC", getFV("FNK3"))

		set_channel("FNMrg_MC", getFV("FNMrgPC"))

		set_channel("N1RMC", getFV("N1K"))

		set_channel("N2K3_MC", getFV("N2K3"))

		set_channel("EGTHD_MC", getFV("EGTHD"))

		Done = 1
		
		pass
	
	pass

instruction("Decelerate slowly to APPROACH IDLE in 2 minutes.")

note("Stabilize the engine for 5 min.")

wait("AIFlag = 1", 120, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, SKIP, "Failed to reach GI in 120 s")

delay(300)


instruction("Record fullset")

do_fullset(10, "Perf Point: AI", "Perf_AI")



instruction("Decelerate slowly to MIN IDLE in 2 minutes.")

note("Stabilize the engine for 7 min.")

wait("GIFlag = 1", 120, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, SKIP, "Failed to reach GI in 120 s")

delay(300)

delay(120)


instruction("Record fullset")

do_fullset(10, "Perf Point: GI", "Perf_GI")


OilConYes = prompt_boo("Do you want to complete Oil Consuption Check?")

if OilConYes:
	auto_start("15EndOilCons")

	pass
